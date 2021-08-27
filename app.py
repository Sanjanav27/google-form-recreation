from flask import Flask, render_template, request, jsonify,flash, redirect, url_for
from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()



app = Flask(__name__)
MONGO_URI       = os.getenv("MONGO_URI")
cluster=MongoClient(MONGO_URI)
db=cluster["Google-recreation"]
admin=db["admin1234"]


@app.route("/", methods = ["GET","POST"])
def Log():
    return render_template("login.html")


@app.route("/home",methods=["GET","POST"])
def Login():
    l_id = request.form["logname"]
    l_pass  = request.form["logpass"]

    tab=l_id+l_pass
    print(tab)
    # print(db)

    # for collec in db.list_collection_names():
    #     print(collec)
    #     if tab == collec:
    #         # collection=db[tab]
    #         print(db[tab])
    return render_template("home.html",tab="admin1234")
        
    # return render_template('invalid.html',invalid='Please enter a valid data')

    

@app.route("/featurethon",methods=["POST","GET"])
def featurethon():
    return render_template("form.html")

@app.route("/submit",methods=["POST","GET"])
def submit():
    data={
    "name" : request.form["name"],
    "email" : request.form["email"],
    "college": request.form["college"],
    #"study": request.form["study"],
    "team_name": request.form["team_name"],
    "member2":request.form["member2"],
    "member3":request.form["member3"],
    "city":request.form["city"],
    #"media":request.form["media"]

    }

    print(data)

    admin.insert_one(data)
    return render_template("form.html")


@app.route("/response",methods=["POST","GET"])
def response():
    
    name=[]
    only_names=[]
    only_email=[]
    only_college=[]
    only_team_name=[]
    only_member2=[]
    only_member3=[]
    only_city=[]
    count=0
    try:
        for all in admin.find({},{ "_id": 0}):
            print(all)
            only_names.append(all["name"])

            only_email.append(all["email"])
            only_college.append(all["college"])
            only_team_name.append(all["team_name"])
            only_member2.append(all["member2"])
            only_member3.append(all["member3"])
            only_city.append(all["city"])
            count=count+1
        
        print(only_names)
        return render_template("response.html",name=only_names,email=only_email,college=only_college,team_name=only_team_name,member2=only_member2,member3=only_member3,city=only_city,count=count)
    except:
        return render_template("response.html",name=only_names,email=only_email,college=only_college,team_name=only_team_name,member2=only_member2,member3=only_member3,city=only_city,count=count)

@app.route("/individual",methods=["POST","GET"])
def individual():
    all_data=[]
    count=0
    for all in admin.find({},{ "_id": 0}):
        print(all)
        all_data.append(all)
        count=count+1
    return render_template("individual.html",all=all_data,count=count)


if __name__ == '__main__':
    app.run(port=5000,debug=True)