from flask_wtf import FlaskForm
from wtforms import *
from wtforms.validators import *

class MyForm(FlaskForm):
    size = IntegerField('Размер мира', default=25, validators=[NumberRange(min=1, max=30), DataRequired()])
    submit = SubmitField("Создать жизнь")