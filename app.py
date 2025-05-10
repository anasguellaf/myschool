from flask import Flask, render_template
from forms import StudentForm
from peewee import *
from datetime import datetime


# create flask app

app = Flask(__name__)
app.secret_key = "code secret"

# create database

db = SqliteDatabase("myschool.db")


class Student(db.Model):
    fullname = CharField()
    tel = CharField()
    email = CharField(unique=True)
    joining_date = DateTimeField(default=datetime.now, formats='%Y-%m-%d %H:%M:%S')
    
    class Meta:
        database = db
        

def initialize_database():
    db.connect()
    db.create_tables([Student])
    db.close()


with app.app_context():
    initialize_database()


# creating the first route for index page
@app.route("/", methods=['GET', 'POST'])
def home():
    return render_template('index.html')


# creating the student route
@app.route("/student", methods=['GET', 'POST'])
def student_list():
    return render_template('student.html')

# add new student route

@app.route('/student/new')
def add_student():
    # create a variable with StudentForm() value
    form = StudentForm()
    return render_template('student_new.html',form=form)


if __name__ == '__main__':
    app.run(debug=True)