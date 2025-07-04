from flask import Flask, render_template, flash, redirect, url_for, request
from forms import StudentForm, TeacherForm
from peewee import *
from datetime import datetime
from werkzeug.utils import secure_filename
import os




UPLOAD_FOLDER = os.path.join('static','uploads')

# create flask app

app = Flask(__name__)
app.secret_key = "code secret"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


# create database

db = SqliteDatabase("myschool.db")



class Group(db.Model):
    name = CharField(unique=True)
    created_at = DateTimeField(default=datetime.now, formats='%Y-%m-%d %H:%M')
    
    class Meta:
        database = db
        
        
class Student(db.Model):
    fullname = CharField()
    tel = CharField()
    email = CharField(unique=True)
    avatar = CharField(null=True)
    joining_date = DateTimeField(default=datetime.now, formats='%Y-%m-%d %H:%M:%S')
    group = ForeignKeyField(Group, backref='students', null=True)
    
    class Meta:
        database = db
        

class Teacher(db.Model):
    fullname = CharField()
    tel = CharField()
    email = CharField(unique=True)
    experience = IntegerField()
    subject = CharField()
    joining_date = DateTimeField(default=datetime.now, formats='%Y-%m-%d')
    avatar = CharField(null=True)
    class Meta:
        database = db


    



def initialize_database():
    db.connect()
    db.create_tables([Student, Teacher, Group])
    db.close()


with app.app_context():
    initialize_database()


# creating the first route for index page
@app.route("/", methods=['GET', 'POST'])
def home():
    student_count = Student.select().count()
    teacher_count = Teacher.select().count()
    return render_template('index.html',student_count=student_count, teacher_count=teacher_count)


# creating the student route
@app.route("/student", methods=['GET', 'POST'])
def student_list():
    students = Student.select()
    counter = students.count()
    return render_template('student.html',students=students, counter = counter)

# add new student route

@app.route('/student/new', methods=['GET', 'POST'])
def add_student():
    # create a variable with StudentForm() value
    form = StudentForm()
    if request.method == 'POST' and form.validate_on_submit():
        # when the submit button is pressed
        fullname = form.fullname.data
        tel = form.tel.data
        email = form.email.data
        avatar = form.avatar.data
        filename = None
        
        if avatar:
            filename = secure_filename(avatar.filename)
            avatar_path = os.path.join(app.config['UPLOAD_FOLDER'],filename)
            avatar.save(avatar_path)

        student = Student.create(
            fullname = fullname,
            tel = tel,
            email = email,
            avatar = filename
        )
        flash('Student added successfully', 'success')
        return redirect(url_for('student_list'))    
    return render_template('student_new.html',form=form)


@app.route('/showdeleteconfirm/<student_id>')
def show_confirmation(student_id):
    # Get student by it's ID
    student = Student.get_by_id(student_id)
    return render_template('delete_confirmation.html',student=student)


@app.route('/student/delete/<student_id>')
def delete_student(student_id):
    # delete student from database
    student = Student.get_by_id(student_id)
    student.delete_instance()
    flash('Student deleted successfully', 'success')
    return redirect(url_for('student_list'))

# Decorator 
@app.route('/teacher')
def teachers_list():   
    # selecting teachers
    query = Teacher.select()
    counter = query.count()
    return render_template('teacher.html', teachers = query, counter = counter)


@app.route('/teacher/new', methods=['POST','GET'])
def add_teacher():
    form = TeacherForm()
    if request.method == 'POST' and form.validate_on_submit():
        
        avatar  = form.avatar.data        
        filename = None
        
        if avatar:
            filename = secure_filename(avatar.filename)
            avatar_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            avatar.save(avatar_path)
        
        
        
        Teacher.create(
            fullname = form.fullname.data,
            tel = form.tel.data,
            email = form.email.data,
            experience = form.experience.data,
            subject = form.subject.data,
            avatar = filename,
        )
        flash('Teacher has been added successfully!', 'success')
        return redirect(url_for('teachers_list'))
    
    return render_template('teacher_new.html', form = form)


@app.route('/delete-teacher-confirmation/<int:teacher_id>')
def teacherDeleteConfirmation(teacher_id):
    # Returns Teacher with id = teacher_id.
    teacher = Teacher.get_by_id(teacher_id)  
    return render_template('teacher_delete_confirmation.html', teacher=teacher)


@app.route('/delete/teacher/<int:teacher_id>')
def delete_teacher(teacher_id):
    # Delete the teacher with the id teacher_id from the Database
    teacher = Teacher.get_by_id(teacher_id)
    teacher.delete_instance()
    flash("Teacher was deleted successfully","success")
    return redirect(url_for('teachers_list'))

@app.route('/teacher/<int:teacher_id>')
def teacher_info(teacher_id):
    # get the teacher from the database where id = teacher_id
    teacher = Teacher.get_by_id(teacher_id)
    return render_template('teacher_view.html', teacher=teacher)


@app.route('/schedual')
def schedual():
    return render_template('scheduals.html')













if __name__ == '__main__':
    app.run(debug=True)