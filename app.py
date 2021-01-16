import flask 
from flask import request, jsonify
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from sqlalchemy import Column, Integer, String, Float
import os

app = flask.Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))



app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir,'app.db')
db = SQLAlchemy(app)
ma = Marshmallow(app)

class Student(db.Model):

    __tablename__ = 'students'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    branch = db.Column(db.String(120))
    college = db.Column(db.String(128))
    batch = db.Column(db.String(120))
    program = db.Column(db.String(120))
    course = db.Column(db.String(120)) 
    first_language = db.Column(db.String(120))

class StudentSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ("id", "name", "branch","college","batch","program","course","first_langauge")

    


student_schema = StudentSchema()
students_schema = StudentSchema(many=True)


@app.cli.command('db_create')
def db_create():
    db.create_all()

    print("db created")
@app.cli.command('db_seed')
def db_seed():
    prem = Student(name ="prem",
    course="computer science",
    branch="cse", 
    college="mcit",
    batch="fall 2020",
    first_language="telugu",program="Advanced programming" )


    abhisheksingh = Student(name ="abhisheksingh",
    course="computer science",
    branch="cse", 
    college="mcit",
    batch="fall 2020",
    first_language="telugu",program="Advanced programming" )
    karandeep = Student(name ="karandeep",
    course="computer science",
    branch="cse", 
    college="mcit",
    batch="fall 2020",
    first_language="telugu",program="Advanced programming" )
    harjant = Student(name ="harjant",
    course="computer science",
    branch="cse", 
    college="mcit",
    batch="fall 2020",
    first_language="telugu",program="Advanced programming" )
    harmansing = Student(name ="harmansing",
    course="computer science",
    branch="cse", 
    college="mcit",
    batch="fall 2020",
    first_language="telugu",program="Advanced programming" )
    kamaljeet = Student(name ="kamaljeet",
    course="computer science",
    branch="cse", 
    college="mcit",
    batch="fall 2020",
    first_language="telugu",program="Advanced programming" )
    imran = Student(name ="imran",
    course="computer science",
    branch="cse", 
    college="mcit",
    batch="fall 2020",
    first_language="telugu",program="Advanced programming" )
    kulveer = Student(name ="kulveer",
    course="computer science",
    branch="cse", 
    college="mcit",
    batch="fall 2020",
    first_language="telugu",program="Advanced programming" )
    harsh = Student(name ="harsh",
    course="computer science",
    branch="cse", 
    college="mcit",
    batch="fall 2020",
    first_language="telugu",program="Advanced programming" )
    divya = Student(name ="divya",
    course="computer science",
    branch="cse", 
    college="mcit",
    batch="fall 2020",
    first_language="telugu",program="Advanced programming" )
    nisha = Student(name ="nisha",
    course="computer science",
    branch="cse", 
    college="mcit",
    batch="fall 2020",
    first_language="telugu",program="Advanced programming" )
    rajender = Student(name ="rajender",
    course="computer science",
    branch="cse", 
    college="mcit",
    batch="fall 2020",
    first_language="telugu",program="Advanced programming" )
    rakshat = Student(name ="rakshat",
    course="computer science",
    branch="cse", 
    college="mcit",
    batch="fall 2020",
    first_language="telugu",program="Advanced programming" )
    anubhav = Student(name ="anubhav",
    course="computer science",
    branch="cse", 
    college="mcit",
    batch="fall 2020",
    first_language="telugu",program="Advanced programming" )
    anmol = Student(name ="anmol",
    course="computer science",
    branch="cse", 
    college="mcit",
    batch="fall 2020",
    first_language="telugu",program="Advanced programming" )
    nipun = Student(name ="nipun",
    course="computer science",
    branch="cse", 
    college="mcit",
    batch="fall 2020",
    first_language="telugu",program="Advanced programming" )
    karan = Student(name ="karan",
    course="computer science",
    branch="cse", 
    college="mcit",
    batch="fall 2020",
    first_language="telugu",program="Advanced programming" )
    sidhu = Student(name ="sidhu",
    course="computer science",
    branch="cse", 
    college="mcit",
    batch="fall 2020",
    first_language="telugu",program="Advanced programming" )
    jasmeet = Student(name ="jasmeet",
    course="computer science",
    branch="cse", 
    college="mcit",
    batch="fall 2020",
    first_language="telugu",program="Advanced programming" )
    manprit = Student(name ="manprit",
    course="computer science",
    branch="cse", 
    college="mcit",
    batch="fall 2020",
    first_language="telugu",program="Advanced programming" )
    tanveer = Student(name ="tanveer",
    course="computer science",
    branch="cse", 
    college="mcit",
    batch="fall 2020",
    first_language="telugu",program="Advanced programming" )
    anchal = Student(name ="anchal",
    course="computer science",
    branch="cse", 
    college="mcit",
    batch="fall 2020",
    first_language="telugu",program="Advanced programming" )
    vikram = Student(name ="vikram",
    course="computer science",
    branch="cse", 
    college="mcit",
    batch="fall 2020",
    first_language="telugu",program="Advanced programming" )
    praveen = Student(name ="praveen",
    course="computer science",
    branch="cse", 
    college="mcit",
    batch="fall 2020",
    first_language="telugu",program="Advanced programming" )
    vikrant = Student(name ="vikrant",
    course="computer science",
    branch="cse", 
    college="mcit",
    batch="fall 2020",
    first_language="telugu",program="Advanced programming" )


    db.session.add(prem) 
    db.session.add(abhisheksingh)
    db.session.add(karandeep)
    db.session.add(harjant)
    db.session.add(harmansing)
    db.session.add(kamaljeet)
    db.session.add(imran)
    db.session.add(kulveer)
    db.session.add(harsh)
    db.session.add(divya)
    db.session.add(nisha)
    db.session.add(rajender)
    db.session.add(rakshat)
    db.session.add(anubhav)
    db.session.add(anmol)
    db.session.add(nipun)
    db.session.add(karan)
    db.session.add(sidhu)
    db.session.add(jasmeet)
    db.session.add(manprit)
    db.session.add(tanveer)
    db.session.add(anchal)
    db.session.add(vikram)
    db.session.add(praveen)
    db.session.add(vikrant)
    db.session.commit()
@app.route('/mcit/cst-students/all',methods=['Get'])
def students():
    students_list = Student.query.all()
    print(students_list)
    result = StudentSchema(many=True).dump(students_list)
    return jsonify(result)

app.run()