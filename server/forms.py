from flask_wtf import Form
from wtforms import TextField, IntegerField, TextAreaField, SubmitField, RadioField,SelectField

from wtforms import validators, ValidationError

class ContactForm(Form):
    Gender = RadioField('Gender', choices = [('M','Male'),('F','Female')])
    Age = IntegerField("age")
    Number_of_sexual_partners = TextAreaField("Number of sexual partners")
    First_sexual_intercourse = IntegerField("First sexual intercourse")
    num_of_pregnancies = IntegerField("Num of pregnancies")
    Smokes = SelectField('Smokes', choices= [('0', 'No'), ('1', 'Yes')])
    Smokes_years = IntegerField('smokes_years')
    Smokes_packs = IntegerField('smokes_packs')
    Smokes = SelectField('Smokes', choices= [('0', 'No'), ('1', 'Yes')])
    Hormonal_contraceptives = SelectField('Hormonal_contraceptives', choices= [('0', 'No'), ('1', 'Yes')])



    submit = SubmitField("Send")