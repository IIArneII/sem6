from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, IntegerField, SubmitField, EmailField, BooleanField, DateTimeLocalField, DateTimeField, DateField
from wtforms.validators import DataRequired, NumberRange


class RegisterForm(FlaskForm):
    name = StringField('Имя', validators=[DataRequired()])
    surname = StringField('Фамилия', validators=[DataRequired()])
    age = IntegerField('Возраст', validators=[DataRequired(), NumberRange(min=1)])
    position = StringField('Должность', validators=[DataRequired()])
    speciality = StringField('Профессия', validators=[DataRequired()])
    address = StringField('Адрес', validators=[DataRequired()])
    email = EmailField('Почта', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    password_again = PasswordField('Повторите пароль', validators=[DataRequired()])
    submit = SubmitField('Регистрация')


class LoginForm(FlaskForm):
    email = EmailField('Почта', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    remember = BooleanField('Запомнить меня')
    submit = SubmitField('Вход')


class JobForm(FlaskForm):
    description = StringField('Описание', validators=[DataRequired()])
    work_size = IntegerField('Объем работ', validators=[DataRequired(), NumberRange(min=0)])
    collaborators = StringField('Участники (почта, через запятую)', validators=[DataRequired()])
    categories = StringField('Категории (название, через запятую)', validators=[DataRequired()])
    start_date = DateTimeLocalField('Дата начала', validators=[DataRequired()], format='%Y-%m-%dT%H:%M')
    end_date = DateTimeLocalField('Дата окончания', format='%Y-%m-%dT%H:%M')
    is_finished = BooleanField('Завершена')
    submit = SubmitField('Сохранить')
