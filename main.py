import flask
from flask import request, url_for

app = flask.Flask(__name__)


@app.route("/")
def home():
    return "Миссия колонизации Марса"


@app.route("/index")
def index():
    return "И на Марсе яблони будут цвести!"


@app.route("/promotion")
def promotion():
    return """Человечество рождается из детства<br>
Человечеству мала одна планета<br>
Мы сделаем обитаемыми безжизненные пока планеты<br>
И начнём с Марса!<br>
Присоединяйся!"""


@app.route("/image_mars")
def image_mars():
    return """
<!doctype html>
<html lang="en">
    <head>
        <meta charset="utf-8">
    </head>
    <body>
        <h1>Жди нас, Марс!</h1><br>
        <img src="https://w7.pngwing.com/pngs/16/806/png-transparent-planet-mars-illustration-earth-terrestrial-planet-mars-solar-system-mars-sphere-venus-astronomical-object-thumbnail.png" alt="Картинка Марса"><br>
        <p>Вот она какая, красная планета</p>
    </body>
</html>
"""


@app.route("/promotion_image")
def promotion_image():
    return """
<!doctype html>
<html lang="en">
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <title>Bootstrap demo</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha2/dist/css/bootstrap.min.css" rel="stylesheet"
        integrity="sha384-aFq/bzH65dt+w6FI2ooMVUpc+21e0SRygnTpmBvdBgSdnuTN7QbdgL+OapgHtvPp" crossorigin="anonymous">
    </head>
    <body>
        <h1>Жди нас, Марс!</h1><br>
        <img src="https://w7.pngwing.com/pngs/16/806/png-transparent-planet-mars-illustration-earth-terrestrial-planet-mars-solar-system-mars-sphere-venus-astronomical-object-thumbnail.png" alt="Картинка Марса"><br>
        <div class="alert alert-primary" role="alert">
            Человечество вырастает из детства.
        </div>
        <div class="alert alert-secondary" role="alert">
            Человечеству мала одна планета.
        </div>
        <div class="alert alert-success" role="alert">
            Мы сделаем обитаемыми безжизненные пока планеты.
        </div>
        <div class="alert alert-danger" role="alert">
            И начнём с Марса!
        </div>
        <div class="alert alert-warning" role="alert">
            Присоединяйся!
        </div>
    </body>
</html>
"""


@app.route("/astronaut_selection", methods=["POST", "GET"])
def astronaut_selection():
    if request.method == "GET":
        return f"""
<!doctype html>
<html>
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <title>Отбор астронавтов</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha2/dist/css/bootstrap.min.css" rel="stylesheet"
        integrity="sha384-aFq/bzH65dt+w6FI2ooMVUpc+21e0SRygnTpmBvdBgSdnuTN7QbdgL+OapgHtvPp" crossorigin="anonymous">
        <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}"/>
    </head>
    <body>
        <div>
            <form class="login_form">
                <h1>Анкета претендента</h1>
                <h2>на участие в миссии</h2>
                <input type="text" class="form-control" id="name" placeholder="Имя" name="name">
                <input type="text" class="form-control" id="surname" placeholder="Фамилия" name="surname">
                <input type="email" class="form-control" id="email aria-describedby="emailHelp" placeholder="Адрес электронной почты" name="email">
                <div class="form-group">
                    <label for="classSelect">Образование</label>
                    <select class="form-control" id="education" name="education">
                      <option>Начальное</option>
                      <option>Среднее</option>
                      <option>Специалитет</option>
                      <option>Бакалавриат</option>
                      <option>Магистратура</option>
                    </select>
                 </div>
                 <div class="form-group form-check">
                    <label for="from-group form-check">Образование</label>
                    <input type="checkbox" class="form-check-input" id="engineerResearcher" name="engineerResearcher">
                    <label class="form-check-label" for="engineerResearcher">Инженер-исследователь</label>
                    <br>
                    <input type="checkbox" class="form-check-input" id="pilot" name="pilot">
                    <label class="form-check-label" for="pilot">Пилот</label>
                    <br>
                    <input type="checkbox" class="form-check-input" id="builder" name="builder">
                    <label class="form-check-label" for="builder">Строитель</label>
                    <br>
                    <input type="checkbox" class="form-check-input" id="exobiologist" name="exobiologist">
                    <label class="form-check-label" for="exobiologist">"Экзобиолог"</label>
                    <br>
                    <input type="checkbox" class="form-check-input" id="doctor" name="doctor">
                    <label class="form-check-label" for="doctor">"Врач"</label>
                    <br>
                    <input type="checkbox" class="form-check-input" id="terraformEngineer" name="terraformEngineer">
                    <label class="form-check-label" for="terraformEngineer">"Инженер по терраформированию"</label>
                    <br>
                    <input type="checkbox" class="form-check-input" id="climatologist" name="climatologist">
                    <label class="form-check-label" for="climatologist">"Климатолог"</label>
                    <br>
                    <input type="checkbox" class="form-check-input" id="radioactiveProtectionSpecialist" name="radioactiveProtectionSpecialist">
                    <label class="form-check-label" for="radioactiveProtectionSpecialist">"Специалист по радиоактивной защите"</label>
                    <br>
                    <input type="checkbox" class="form-check-input" id="аstrogeologist" name="аstrogeologist">
                    <label class="form-check-label" for="аstrogeologist">"Астрогеолог"</label>
                    <br>
                    <input type="checkbox" class="form-check-input" id="glacialGeologist" name="glacialGeologist">
                    <label class="form-check-label" for="glacialGeologist">"Гляциолог"</label>
                    <br>
                    <input type="checkbox" class="form-check-input" id="lifeSupportEngineer" name="lifeSupportEngineer">
                    <label class="form-check-label" for="lifeSupportEngineer">"Инженер жизнеобеспечения"</label>
                    <br>
                    <input type="checkbox" class="form-check-input" id=meteorologist" name="meteorologist">
                    <label class="form-check-label" for="meteorologist">"Метеоролог"</label>
                    <br>
                    <input type="checkbox" class="form-check-input" id="roverOperator" name="roverOperator">
                    <label class="form-check-label" for="roverOperator">"Оператор марсохода"</label>
                    <br>
                    <input type="checkbox" class="form-check-input" id="cyberEngineer" name="cyberEngineer">
                    <label class="form-check-label" for="cyberEngineer">"Киберинженер"</label>
                    <br>
                    <input type="checkbox" class="form-check-input" id="navigator" name="navigator">
                    <label class="form-check-label" for="navigator">"Штурман"</label>
                    <br>
                    <input type="checkbox" class="form-check-input" id="dronePilot" name="dronePilot">
                    <label class="form-check-label" for="dronePilot">"Пилот дронов"</label>
                 </div>
                 <div class="form-group">
                    <label for="form-check">Пол</label>
                    <div class="form-check">
                      <input class="form-check-input" type="radio" name="sex" id="male" value="male" checked>
                      <label class="form-check-label" for="male">
                        Мужской
                      </label>
                    </div>
                    <div class="form-check">
                      <input class="form-check-input" type="radio" name="sex" id="female" value="female">
                      <label class="form-check-label" for="female">
                        Женский
                      </label>
                    </div>
                </div>
                <div class="form-group">
                    <label for="about">Немного о себе</label>
                    <textarea class="form-control" id="about" rows="3" name="about"></textarea>
                </div>
                <div class="form-group">
                    <label for="photo">Приложите фотографию</label>
                    <input type="file" class="form-control-file" id="photo" name="file">
                </div>
            </form>
        </div>
    </body>
</html>
"""
    else:
        pass


if __name__ == "__main__":
    app.run(port=8080, host="127.0.0.1")
