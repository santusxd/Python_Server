from flask import Flask, render_template, request
import sys
import os
from hashing import hashing
from user import User
app = Flask(__name__)
users = set()


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
    for user in users:

        if request.args.get("username") == user.name:
            if hashing(request.args.get("password")) == hashing(user.password):
                # return "Hola {}".format(user.name)
                return str(users)

            return "jajaja, fallaste"


def create_user(name, password):
    user = User(name, password)

    users.add(user)


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
create_user("Santi", "loco")

app.run(host="0.0.0.0", port=port, debug=False)
