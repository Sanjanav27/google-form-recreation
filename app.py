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
    

    for collec in db.collection_names():
        if tab==collec:
            source = db["admin1234"]
            destination = db[tab]

            # Remove all documents, or make modifications. 
            destination.delete_many({}) 

            # Restore documents from the source collection.  
            for doc in source.find({}): 
                print(doc)
                destination.insert(doc)
            collection=db[tab]
            return render_template("home.html",tab=tab)
    
    return render_template('invalid.html',invalid='Please enter a valid data')

    

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
    for collec in db.collection_names():
        db[collec].insert_one(data)
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


@app.route("/register",methods=["POST","GET"])
def register():
    return render_template("signup.html")

@app.route("/regsuccess",methods=["POST","GET"])
def regsuccess():
    l_id = request.form["logname"]
    l_pass  = request.form["logpass"]

    tab=l_id+l_pass
    for collec in db.collection_names():
        if tab==collec:
            return render_template("signup.html",a="Username and password are already taken. Try another.") 
    collection=db[tab]
    data={}
    collection.insert_one(data)
    return render_template("signup.html",a="successfully registered")    

@app.route("/ques",methods=["POST","GET"])
def ques():
    return render_template("question.html")

@app.route("/detail",methods=["POST","GET"])
def detail():
    detail=request.form["name"]
    print(detail)
    return render_template("question.html")

if __name__ == '__main__':
    app.run(port=5000,debug=True)