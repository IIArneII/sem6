from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, SelectField, BooleanField, FileField, SubmitField, TextAreaField, RadioField


class Form(FlaskForm):
    last_name = StringField('Фамилия')
    first_name = StringField('Имя')
    email = EmailField('Почта')
    education = SelectField('Образование', choices=['Начальное', 'Основное (общее)',
                                                    'Среднее (полное) общее', 'Среднее профессиональное',
                                                    'Высшее'])
    profession = SelectField('Основная профессия',
                             choices=['Инженер - исследователь', 'Пилот', 'Строитель', 'Экзобиолог', 'Врач',
                                      'Инженер по терраформированию', 'Климатолог', 'Специалист по радиационной защите',
                                      'Астрогеолог', 'Гляциолог', 'Инженер жизнеобеспечения', 'Метеоролог',
                                      'Оператор марсохода', 'Киберинженер', 'Щтурман', 'Пилот дронов'])
    sex = RadioField('Пол', choices=['Мужской', 'Женский'])
    motivation = TextAreaField('Мотивация')
    stay = BooleanField('Готовы ли остаться на Марсе?')
    photo = FileField('Фото')
    submit = SubmitField('Отправить')
