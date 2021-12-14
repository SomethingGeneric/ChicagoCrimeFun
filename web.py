# stdlib
import os, webbrowser

# pip
from flask import *

# local
from ChicagoCrimeFun import *

print_info("-- Initializing backend --")
print_info("1 - Loading data")
ccf = ChicagoCrimeFun()
print_info("2 - Building location tree")
ccf.build_loc_priority()
print_info("3 - Loading type priority tree")
ccf.build_crime_priority()


app = Flask(__name__)

if not os.path.exists("maps"):
    print("Generating maps. Please wait")
    # ccf.map_all_types()


@app.route("/")
def index():
    return render_template("base.html",page_title="Home", leftc="<p>Left</p>", rightc="<p>Right</p>")


@app.route("/map/<filename>")
def map(filename):
    if not os.path.exists("maps" + os.sep + filename):
        abort(404)
    return send_file("maps" + os.sep + filename)


if __name__ == "__main__":
    webbrowser.open_new_tab("http://localhost:5000")
    app.run(debug=True)