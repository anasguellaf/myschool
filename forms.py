from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, DateField, SubmitField
from wtforms.validators import DataRequired, Email


class StudentForm(FlaskForm):
    fullname = StringField('Fullname',validators=[DataRequired()])
    tel = StringField('Tel Number',validators=[DataRequired()])
    email = EmailField('Email',validators=[DataRequired(),Email()])
    joining_date = DateField('Join Date',validators=[DataRequired()])
    btn_submit = SubmitField('Add Student')