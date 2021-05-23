from flask import Flask, render_template, request, jsonify,flash
import pymongo
from pymongo import MongoClient
from flask import Flask, redirect, url_for
cluster=MongoClient("mongodb+srv://sanju:1234@cluster0.wllvz.mongodb.net/sanju?retryWrites=true&w=majority")
db=cluster["sentiment_meter"]
collection=db["words"]

mydb = cluster["sentiment_meter"]

mycol = mydb["customers"]




app = Flask(__name__)
@app.route("/", methods = ["GET","POST"])
def Log():
    return render_template("login.html")


@app.route("/home",methods=["GET","POST"])
def Login():
    return render_template("home.html")

@app.route("/featurethon",methods=["POST","GET"])
def featurethon():
    return render_template("form.html")

@app.route("/register",methods=["POST","GET"])
def register():
    return render_template("signup.html")
if __name__ == '__main__':
    app.run(port=5500,debug=True)