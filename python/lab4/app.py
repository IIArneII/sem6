from flask import Flask, request, render_template, json
from form import Form
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication


app = Flask(__name__)
app.config['SECRET_KEY'] = 'my_secret_key'


@app.route('/favicon.ico')
def favicon():
    return 'favicon'


@app.route('/')
def main_page():
    return index()


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Добро пожаловать!')


@app.route('/')
@app.route('/list_prof/<li>')
def list_prof(li):
    param = {'title': 'Список профессий',
             'li': li,
             'prof_list': [
                 'Оператор марсохода',
                 'Щтурман',
                 'Киберинженер',
                 'Метеоролог',
                 'Гляциолог',
                 'Астрогеолог',
                 'Климатолог',
                 'Врач',
                 'Экзобиолог',
                 'Строитель',
                 'Строитель',
                 'Пилот',
             ]}
    return render_template('list_prof.html', **param)


@app.route('/')
@app.route('/distribution')
def distribution():
    with open('static/members/crew.json', encoding='utf8') as js:
        crew = json.load(js)['crew']
        return render_template('distribution.html', title='Распределение', crew=crew)


@app.route('/')
@app.route('/member/<int:number>')
def member(number):
    with open('static/members/crew.json', encoding='utf8') as js:
        crew = json.load(js)['crew']
        return render_template('member.html', title='Член экипажа', crew=crew, number=number)


@app.route('/')
@app.route('/member/random')
def member_random():
    return member('random')


@app.route('/')
@app.route('/room/<sex>/<int:age>')
def room(sex, age):
    return render_template('room.html', title='Каюты', sex=sex, age=age)


@app.route('/')
@app.route('/astronaut_selection', methods=['GET', 'POST'])
def astronaut_selection():
    if request.method == 'GET':
        form = Form()
        return render_template('astronaut_selection.html', title='Подать заявку', form=form)
    else:
        form = str(dict(request.form))
        file = request.files['photo'].read()

        mail_sender = 'alefbetforpython@gmail.com'
        mail_receiver = request.form['email']
        username = 'alefbetforpython@gmail.com'
        password = '*********'
        server = smtplib.SMTP('smtp.gmail.com:587')

        subject = 'Данные формы'
        msg = MIMEMultipart()
        msg['From'] = mail_sender
        msg['To'] = mail_receiver
        msg['Subject'] = subject

        msg.attach(MIMEText(form))

        part = MIMEApplication(file, Name=request.files['photo'].filename)
        part['Content-Disposition'] = f'''attachment; filename="{request.files['photo'].filename}"'''
        msg.attach(part)

        server.starttls()
        server.ehlo()
        server.login(username, password)
        server.sendmail(mail_sender, mail_receiver, msg.as_string())
        server.quit()

        return 'Отправлено'


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
