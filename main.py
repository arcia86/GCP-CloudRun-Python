import os

from flask import Flask
from flask import request

app = Flask(__name__)


@app.route("/")
def hello_world():
    name = os.environ.get("NAME", "World")
    geo = request.headers.get('X-Client-Geo-Location')
    if geo == None:
        geo = "No country"
        return "Hello {}!".format(name) + "I am come from =" + geo
    else:
        return "Hello {}!".format(name) + "I am come from =" + geo 
@app.route("/deny")
def deny():
    return "You have been denied by Cloud Armor"

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("HTTP_PORT")))
    """app.run(debug=True, host="127.0.0.1", port=9000)"""