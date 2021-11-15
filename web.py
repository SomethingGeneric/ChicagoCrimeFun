# stdlib
import os

# pip
from flask import *

# local
# from ChicagoCrime import ChicagoCrimeFun

# print("Loading data")
# ccf = ChicagoCrimeFun()

app = Flask(__name__)

if not os.path.exists("maps"):
    print("Generating maps. Please wait")
    # ccf.map_all_types()


@app.route("/")
def index():
    html = """
<html>
<head>
<title>Chicago Crime</title>
</head>
<body>
<h1>Chicago Crime</h1>
<ul>
$STUFF$
</li>
</body>
</html>    
"""
    insert = ""
    for fn in os.listdir("maps"):
        insert += "<li><a href='/map/" + fn + "'>" + fn + "</a></li>"
    return html.replace("$STUFF$", insert)


@app.route("/map/<filename>")
def map(filename):
    if not os.path.exists("maps" + os.sep + filename):
        abort(404)
    return send_file("maps" + os.sep + filename)


if __name__ == "__main__":
    app.run(debug=True)
