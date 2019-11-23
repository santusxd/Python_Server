from flask import Flask, render_template
import sys
import os

app = Flask(__name__)


@app.route("/index.html")
def index():
    return "Welcome to the best python server"


@app.route("/login")
def login():
   # file = open("public_html/santi/login.html", "r")
   # contents = file.read()
   # contents = contents.replace("rgba(255, 100, 0, 0.5)", "orange")
   # file.close()
   # return contents
    return render_template("login.html", bg_colour="red", url="/santi/login-data")


@app.route("/login-data")
def login_dat():
    return "Hi. Great thing."


print(sys.argv)
if "--port" in sys.argv:
    try:
        port = int(sys.argv[sys.argv.index("--port") + 1])
    except ValueError:
        print("An invalid port number was given.")
        exit()
else:
    print("No port aregument was given")
    exit()

os.system("python3 public_html/santi/create_htacess.py --port {}".format(port))

app.run(host="0.0.0.0", port=port, debug=False)
