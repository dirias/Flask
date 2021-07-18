from flask_wtf import FlaskForm
from flask_wtf.recaptcha import validators
from wtforms.fields import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, data_required

class LoginForm(FlaskForm):
    username = StringField('Nombre de Usuario', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Enviar')

class TodoForm(FlaskForm):
    description = StringField('Description', validators=[DataRequired()])
    submit = SubmitField('Crear')

class DeleteTodoForm(FlaskForm):
    submit = SubmitField('Borrar')

class UpdateTodoForm(FlaskForm):
    submit = SubmitField('Actualizar')