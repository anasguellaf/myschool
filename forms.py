from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, DateField, SubmitField, IntegerField, FileField
from wtforms.validators import DataRequired, Email
from flask_wtf.file import FileAllowed


class StudentForm(FlaskForm):
    fullname = StringField('Fullname',validators=[DataRequired()])
    tel = StringField('Tel Number',validators=[DataRequired()])
    email = EmailField('Email',validators=[DataRequired(),Email()])
    avatar = FileField('Profil picture', validators=[FileAllowed(['jpg','png','jpeg'], 'Images only!')])
    joining_date = DateField('Join Date',validators=[DataRequired()])
    btn_submit = SubmitField('Add Student')
    
class TeacherForm(FlaskForm):
    fullname = StringField('Teacher Fullname', validators=[DataRequired()])
    tel = StringField('Teacher Phone Number', validators=[DataRequired()])
    email = EmailField('Teacher Email', validators=[DataRequired(),Email()])
    experience = IntegerField('Teacher Experience Years', validators=[DataRequired()])
    subject = StringField('Subject', validators=[DataRequired()])
    avatar = FileField('Profil Picture', validators=[FileAllowed(['jpg','jpeg', 'png'], 'Images Only')])
    btn_submit = SubmitField('Add Teacher')
