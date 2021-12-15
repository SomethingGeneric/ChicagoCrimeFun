###########
# Imports #
###########
# Python standard library modules
import os, webbrowser, random, string, shutil

# PIP Packages (community libaries & frameworks)
from flask import *

# Other code local to this project
from ChicagoCrimeFun import *
# The above import defines ChicagoCrimeFun,
# and the print_info, print_warn, etc functions used below
# and in some of the flask routes defined later in the file.

#######################
# Deployment settings #
#######################
SERVE_URL = "0.0.0.0"
SERVE_PORT = 6969 # blame Ramon for this. It was 5000 previously I swear. - Matt

##################################
# Setup of dataset and AVL Trees #
##################################
print_info("-- Initializing backend --")
print_info("1 - Loading data")
ccf = ChicagoCrimeFun()

print_info("2 - Building location tree")
ccf.build_loc_priority()
print_info("3 - Loading type priority tree")
ccf.build_crime_priority()

print_info("4 - Adding random cases")
ccf.add_random_case(20)

print_info("4 - Constructing crime priority list")
ccf.construct_crime_priority_list()

################################################
# Generate heatmaps of previous crime reports, #
# if not previously done. This could lock up   #
# the loaing process for a while.              #
################################################
if not os.path.exists("heatmaps"):
    print("Generating maps. Please wait")
    ccf.map_all_types()

##############################################################
# This dir is used to store the maps that the webUI displays #
# after the user asks for a new dispatch location            #
##############################################################
if not os.path.exists("dispatch_maps"):
    os.makedirs("dispatch_maps")

###############################
# Cleaning up any stale files #
###############################
nuke_these = ["map.html", "dispatch_history.txt", ".dpurl"]

for something in nuke_these:
    if os.path.exists(something):
        os.remove(something)

#################################
# Initalizing the web framework #
#################################
app = Flask(__name__)

############################################################################
# In Flask, routes are certain sub-urls that the program will respond to.  #
# For example, the "/" endpoint below is the main page of the application. #
# The exact functions that each endpoint/route uses will be explained      #
############################################################################


@app.route("/")
def index():
    """Build the main page of the app (contains most user-facing functions)"""

    # .dpurl is intended to set up the map to display a previous result if the
    # user refreshes the page. It doesn't work quite right. In theory this
    # should be done with cookies. We didn't have time to learn how to properly
    # implement client-side first-party cookies, and do it safely. That would be
    # the proper way to go about this in production, on a deployment not run locally
    if os.path.exists(".dpurl"):
        ifr = open(".dpurl").read()
        os.remove(".dpurl")
    else:
        ifr = "/empty"

    # The render_template function takes in an html document from the 'templates/' directory,
    # and subs in given values as requested. Here, we also use sub-templates 'home_left' and 'home_right'
    # so that we can make more of the content dynamic. To reduce the number of comments in each endpoint,
    # we're going to describe these variables in more detail within the templates themselves.
    return render_template(
        "base.html",
        page_title="Home",
        leftc=render_template("home_left.html", ifr=ifr),
        rightc=render_template("home_right.html", sf=ccf.scaling_factor),
        onload_func="refreshLiveData()",
    )

@app.route("/setscale/<val>")
def setscale(val):
    ccf.scaling_factor = val
    return "Done"

@app.route("/getscale")
def getscale():
    return str(ccf.scaling_factor)


@app.route("/put_dispatch", methods=["POST"])
def put_dispatch():
    
    new_request = request.get_json()

    if new_request is not None:
        new_request = new_request['new_request']

    if new_request == 'None':
        new_request = None

    fn = "".join(random.choices(string.ascii_lowercase + string.digits, k=64)) + ".html"

    result = str(ccf.decide_next_patrol(new_request, map_it=True, log_it=True))

    EX = ""
    if os.path.exists(".pred"):
        os.remove(".pred")
        EX = "---PRED"

    if os.path.exists("map.html"):
        shutil.move("map.html", "dispatch_maps" + os.sep + fn)
        if result == "No location data":
            return "ERROR---ERROR"
        else:
            with open(".dpurl", "w") as f:
                f.write(fn)
            return result + "---" + fn + EX
    else:
        return "ERROR---ERROR"

# TODO: This one is borken because the Heap code is borked.
@app.route("/pending")
def pending():
    list_of_stuff = []
    while ccf.dispatch_queue.size != 0:
        i, ds = ccf.dispatch_queue.remove()
        list_of_stuff.append(ds)
        ccf.dispatch_queue.insert(i,ds)
    return "\n".join(list_of_stuff)


@app.route("/past_patrols")
def past_patrols():
    if os.path.exists("dispatch_history.txt"):
        with open("dispatch_history.txt") as f:
            return f.read()
    else:
        return ""


@app.route("/heatmaps")
def heatmaps():
    hm_html = "<ul>"
    for filename in os.listdir("heatmaps"):
        hm_html += (
            "<li><a target='_blank' href='heatmaps/"
            + filename
            + "'>"
            + filename.replace(".html", "")
            + "</a></li>"
        )
    hm_html += "</ul>"
    return render_template(
        "base.html", page_title="Heatmaps", leftc="<h2>Historical Trends</h2>" + hm_html
    )


@app.route("/heatmaps/<filename>")
def hmap(filename):
    if not os.path.exists("heatmaps" + os.sep + filename):
        abort(404)
    return send_file("heatmaps" + os.sep + filename)


@app.route("/dispatch/maps/<filename>")
def dmap(filename):
    if not os.path.exists("dispatch_maps" + os.sep + filename):
        abort(404)
    return send_file("dispatch_maps" + os.sep + filename)


# There's definitely a better way to satisfy the iframe default
@app.route("/empty")
def empty():
    return render_template("empty.html")

@app.route("/update")
def git():
    os.system("git pull")
    sys.exit(0)

if __name__ == "__main__":
    webbrowser.open_new_tab("http://" + SERVE_URL + ":" + str(SERVE_PORT))
    app.run(host=SERVE_URL, port=SERVE_PORT, debug=True)
