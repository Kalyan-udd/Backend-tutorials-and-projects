# the multi page funcionality of Flask...
from flask import Flask

app = Flask(__name__)
@app.route("/")
def selection():
    return "<h1>please select a page home or user to go with other things.."
@app.route("/home")
def Home():
    name = input("enter your name here: ")
    return f"Hello!.. {name} Welcome to home page."
@app.route("/User")
def User():
    User = {
        "kalyan":"sai$2006",
        "jithu" : "Uniquenoone@163."
    }
    name = input("please enter your name.. ").lower()
    password = input("please enter your password: ")
    if User[name] == password:
        return f"your authentication has been perfectly verified Mr.{name.upper()}, you can enjoy using the website..."
    elif User[name] != password:
        return "False password."
    elif name not in User:
        return "Person doesnt exist."
    else:
        return ""

app.run(host="0.0.0.0", port="8080", debug=True)