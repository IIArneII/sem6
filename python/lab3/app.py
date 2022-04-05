from flask import Flask, url_for, request

app = Flask(__name__)


@app.route('/favicon.ico')
def favicon():
    return 'favicon'


@app.route('/')
def main_page():
    return 'Миссия колонизации Марса'


@app.route('/')
@app.route('/index')
def index():
    return 'И на Марсе будут яблони цвести!'


@app.route('/')
@app.route('/promotion')
def promotion():
    return """Человечество вырастает из детства.<br>
              Человечеству мала одна планета.<br>
              Мы сделаем обитаемыми безжизненные пока планеты.<br>
              И начнем с Марса!<br>
              Присоединяйся!"""


@app.route('/')
@app.route('/image_mars')
def image_mars():
    return f"""<!doctype html>
    <html>
        <head>
            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='stylesheet/stylesheet.css')}"/>
            <title>Привет, Марс!</title>
        </head>
        <body>
            <h1>Жди нас, Марс!</h1>
            <img src="{url_for('static', filename='img/mars.jpg')}" alt="Картинка Марса не нашлась">
        </body>
    <html>
    """


@app.route('/')
@app.route('/astronaut_selection', methods=['POST', 'GET'])
def astronaut_selection():
    if request.method == 'POST':
        for i, j in request.form.items():
            print(f'{i}: {j}')
    with open('./static/pages/astronaut_selection.html', 'r', encoding='utf-8') as p:
        return ''.join(p.readlines())


@app.route('/')
@app.route('/results/<nickname>/<int:level>/<float:rating>')
def results(nickname, level, rating):
    return f"nickname: {nickname}, level: {level}, rating: {rating}"


@app.route('/')
@app.route('/photo/<nickname>', methods=['POST', 'GET'])
def photo(nickname):
    if request.method == 'POST':
        f = request.files['file']
        f.save(f'./stati/img/{nickname}.png')
        return 'Фото отправлено'
    if request.method == 'GET':
        return f"""<!DOCTYPE html>
                    <html>
                        <head>
                            <title>
                                Загрузить фото
                            </title>
                        </head>
                        <body>
                            <img src="{url_for('stati', filename=f'img/{nickname}.png')}">
                            <form name="form" method="post" enctype="multipart/form-data">
                                <div>
                                    <input type="file" id="file" name="file">
                                </div>
                                <div>
                                    <input type="submit" value="Отправить">
                                </div>
                            </form>
                        </body>
                        </html>"""


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
