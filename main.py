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


@app.route("/choice/<planet_name>")
def choice(planet_name):
    if planet_name == "Меркурий":
        return """
<!doctype html>
<html>
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Меркурий</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha2/dist/css/bootstrap.min.css" rel="stylesheet"
    integrity="sha384-aFq/bzH65dt+w6FI2ooMVUpc+21e0SRygnTpmBvdBgSdnuTN7QbdgL+OapgHtvPp" crossorigin="anonymous">
    <link rel="stylesheet" type="text/css" href="../static/css/style.css"/>
</head>
<body>
    <div class="table">
    <div class="row">
    <div class="col">
    <table class="infobox" style="width:27em;" data-name="Планета"><tbody><tr><th colspan="2" scope="colgroup" class="infobox-above" style="">Меркурий <span data-wikidata-property-id="P367" class="no-wikidata"><a href="//commons.wikimedia.org/wiki/File:Mercury_symbol_(bold).svg?uselang=ru" class="image"><img alt="Mercury symbol (bold).svg" src="//upload.wikimedia.org/wikipedia/commons/thumb/a/af/Mercury_symbol_%28bold%29.svg/20px-Mercury_symbol_%28bold%29.svg.png" decoding="async" width="20" height="20" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/a/af/Mercury_symbol_%28bold%29.svg/30px-Mercury_symbol_%28bold%29.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/a/af/Mercury_symbol_%28bold%29.svg/40px-Mercury_symbol_%28bold%29.svg.png 2x" data-file-width="15" data-file-height="15"></a></span></th></tr><tr><td colspan="2" class="" style="text-align:center;"><a href="/wiki/%D0%9F%D0%BB%D0%B0%D0%BD%D0%B5%D1%82%D0%B0" title="Планета">Планета</a></td></tr><tr><td colspan="2" class="infobox-image" style=""> <span data-wikidata-property-id="P18" class="no-wikidata"><a href="//commons.wikimedia.org/wiki/File:Mercury_in_color_-_Prockter07_centered.jpg?uselang=ru" class="image" title="Меркурий (снимок «Мессенджера»). У правого края в южном полушарии виден кратер Толстой"><img alt="Меркурий (снимок «Мессенджера»). У правого края в южном полушарии виден кратер Толстой" src="//upload.wikimedia.org/wikipedia/commons/thumb/3/30/Mercury_in_color_-_Prockter07_centered.jpg/280px-Mercury_in_color_-_Prockter07_centered.jpg" decoding="async" width="280" height="278" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/3/30/Mercury_in_color_-_Prockter07_centered.jpg/420px-Mercury_in_color_-_Prockter07_centered.jpg 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/3/30/Mercury_in_color_-_Prockter07_centered.jpg/560px-Mercury_in_color_-_Prockter07_centered.jpg 2x" data-file-width="1991" data-file-height="1974"></a><br><span data-wikidata-qualifier-id="P2096" class="media-caption" style="display:block">Меркурий (снимок «<a href="/wiki/%D0%9C%D0%B5%D1%81%D1%81%D0%B5%D0%BD%D0%B4%D0%B6%D0%B5%D1%80_(%D0%90%D0%9C%D0%A1)" title="Мессенджер (АМС)">Мессенджера</a>»). У правого края в южном полушарии виден <a href="/wiki/%D0%A2%D0%BE%D0%BB%D1%81%D1%82%D0%BE%D0%B9_(%D0%BA%D1%80%D0%B0%D1%82%D0%B5%D1%80)" title="Толстой (кратер)">кратер Толстой</a></span></span> </td></tr>
<tr>
<th colspan="2" scope="colgroup" class="infobox-header" style="">Открытие</th>
</tr>
<tr>
<th scope="row" class="plainlist">Первооткрыватель</th>
<td class="plainlist">
<span data-wikidata-claim-id="Q308$3a050991-4ff2-9215-9adf-0c89ea197aea" class="wikidata-claim" data-wikidata-property-id="P61"><span class="wikidata-snak wikidata-main-snak"><i>неизвестно</i></span></span></td>
</tr>
<tr>
<th scope="row" class="plainlist">Дата открытия</th>
<td class="plainlist">
<span data-wikidata-claim-id="Q308$4ca866c1-42a7-8573-ec18-330f544c6184" class="wikidata-claim" data-wikidata-property-id="P575"><span class="wikidata-snak wikidata-main-snak"><i>неизвестно</i></span></span></td>
</tr>
<tr>
<th colspan="2" scope="colgroup" class="infobox-header" style="">Орбитальные характеристики<sup id="cite_ref-solarsystem_1-0" class="reference"><a href="#cite_note-solarsystem-1">[1]</a></sup></th>
</tr>
<tr>
<td colspan="2" class="plainlist" style="text-align:center;">
<a href="/wiki/%D0%AD%D0%BF%D0%BE%D1%85%D0%B0_(%D0%B0%D1%81%D1%82%D1%80%D0%BE%D0%BD%D0%BE%D0%BC%D0%B8%D1%8F)" title="Эпоха (астрономия)">Эпоха</a>: <a href="/wiki/J2000.0" title="J2000.0">J2000.0</a></td>
</tr>
<tr>
<th scope="row" class="plainlist"><a href="/wiki/%D0%9F%D0%B5%D1%80%D0%B8%D0%B3%D0%B5%D0%BB%D0%B8%D0%B9" title="Перигелий">Перигелий</a></th>
<td class="plainlist">
<span data-wikidata-property-id="P2244" class="no-wikidata">46&nbsp;001&nbsp;009 км<br>0,30749951 а.е.</span></td>
</tr>
<tr>
<th scope="row" class="plainlist"><a href="/wiki/%D0%90%D1%84%D0%B5%D0%BB%D0%B8%D0%B9" title="Афелий">Афелий</a></th>
<td class="plainlist">
<span data-wikidata-property-id="P2243" class="no-wikidata">69&nbsp;817&nbsp;445 км<br>0,46670079 <a href="/wiki/%D0%90%D1%81%D1%82%D1%80%D0%BE%D0%BD%D0%BE%D0%BC%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B0%D1%8F_%D0%B5%D0%B4%D0%B8%D0%BD%D0%B8%D1%86%D0%B0" title="Астрономическая единица">а.е.</a></span></td>
</tr>
<tr>
<th scope="row" class="plainlist"><a href="/wiki/%D0%91%D0%BE%D0%BB%D1%8C%D1%88%D0%B0%D1%8F_%D0%BF%D0%BE%D0%BB%D1%83%D0%BE%D1%81%D1%8C" title="Большая полуось">Большая полуось</a>&nbsp;(<style data-mw-deduplicate="TemplateStyles:r117753614">.mw-parser-output .ts-math{white-space:nowrap;font-family:times,serif,palatino linotype,new athena unicode,athena,gentium,code2000;font-size:120%}</style><span class="ts-math"><i>a</i></span>)</th>
<td class="plainlist">
<span data-wikidata-property-id="P2233" class="no-wikidata">57&nbsp;909&nbsp;227 км<br>0,38709927 а.е.</span></td>
</tr>
<tr>
<th scope="row" class="plainlist"><a href="/wiki/%D0%AD%D0%BA%D1%81%D1%86%D0%B5%D0%BD%D1%82%D1%80%D0%B8%D1%81%D0%B8%D1%82%D0%B5%D1%82_%D0%BE%D1%80%D0%B1%D0%B8%D1%82%D1%8B" title="Эксцентриситет орбиты">Эксцентриситет орбиты</a>&nbsp;(<link rel="mw-deduplicated-inline-style" href="mw-data:TemplateStyles:r117753614"><span class="ts-math"><i>e</i></span>)</th>
<td class="plainlist">
<span data-wikidata-property-id="P1096" class="no-wikidata">0,20563593</span></td>
</tr>
<tr>
<th scope="row" class="plainlist"><a href="/wiki/%D0%A1%D0%B8%D0%B4%D0%B5%D1%80%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B8%D0%B9_%D0%BF%D0%B5%D1%80%D0%B8%D0%BE%D0%B4" title="Сидерический период">Сидерический период</a> обращения</th>
<td class="plainlist">
<span data-wikidata-property-id="P2146" class="no-wikidata">87,969 дней<sup id="cite_ref-nasa_2-0" class="reference"><a href="#cite_note-nasa-2">[2]</a></sup></span></td>
</tr>
<tr>
<th scope="row" class="plainlist"><a href="/wiki/%D0%A1%D0%B8%D0%BD%D0%BE%D0%B4%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B8%D0%B9_%D0%BF%D0%B5%D1%80%D0%B8%D0%BE%D0%B4" title="Синодический период">Синодический период</a> обращения</th>
<td class="plainlist">
<span data-wikidata-property-id="P4341" class="no-wikidata">115,88 дней<sup id="cite_ref-nasa_2-1" class="reference"><a href="#cite_note-nasa-2">[2]</a></sup></span></td>
</tr>
<tr>
<th scope="row" class="plainlist"><a href="/wiki/%D0%9E%D1%80%D0%B1%D0%B8%D1%82%D0%B0%D0%BB%D1%8C%D0%BD%D0%B0%D1%8F_%D1%81%D0%BA%D0%BE%D1%80%D0%BE%D1%81%D1%82%D1%8C" title="Орбитальная скорость">Орбитальная скорость</a>&nbsp;(<link rel="mw-deduplicated-inline-style" href="mw-data:TemplateStyles:r117753614"><span class="ts-math"><i>v</i></span>)</th>
<td class="plainlist">
47,36 км/с (средняя)<sup id="cite_ref-nasa_2-2" class="reference"><a href="#cite_note-nasa-2">[2]</a></sup></td>
</tr>
<tr>
<th scope="row" class="plainlist"><a href="/wiki/%D0%A1%D1%80%D0%B5%D0%B4%D0%BD%D1%8F%D1%8F_%D0%B0%D0%BD%D0%BE%D0%BC%D0%B0%D0%BB%D0%B8%D1%8F" class="mw-redirect" title="Средняя аномалия">Средняя аномалия</a>&nbsp;(<link rel="mw-deduplicated-inline-style" href="mw-data:TemplateStyles:r117753614"><span class="ts-math"><i>M<sub>o</sub></i></span>)</th>
<td class="plainlist">
174,795884°</td>
</tr>
<tr>
<th scope="row" class="plainlist"><a href="/wiki/%D0%9A%D0%B5%D0%BF%D0%BB%D0%B5%D1%80%D0%BE%D0%B2%D1%8B_%D1%8D%D0%BB%D0%B5%D0%BC%D0%B5%D0%BD%D1%82%D1%8B_%D0%BE%D1%80%D0%B1%D0%B8%D1%82%D1%8B#Наклонение" title="Кеплеровы элементы орбиты">Наклонение</a>&nbsp;(<link rel="mw-deduplicated-inline-style" href="mw-data:TemplateStyles:r117753614"><span class="ts-math"><i>i</i></span>)</th>
<td class="plainlist">
<span data-wikidata-property-id="P2045" class="no-wikidata">7,00° относительно плоскости эклиптики<br>3,38° относительно солнечного экватора<br>6,34° отн. инвариантной плоскости<sup id="cite_ref-meanplane_3-0" class="reference"><a href="#cite_note-meanplane-3">[3]</a></sup></span></td>
</tr>
<tr>
<th scope="row" class="plainlist"><a href="/wiki/%D0%94%D0%BE%D0%BB%D0%B3%D0%BE%D1%82%D0%B0_%D0%B2%D0%BE%D1%81%D1%85%D0%BE%D0%B4%D1%8F%D1%89%D0%B5%D0%B3%D0%BE_%D1%83%D0%B7%D0%BB%D0%B0" class="mw-redirect" title="Долгота восходящего узла">Долгота восходящего узла</a>&nbsp;(<link rel="mw-deduplicated-inline-style" href="mw-data:TemplateStyles:r117753614"><span class="ts-math">Ω</span>)</th>
<td class="plainlist">
<span data-wikidata-property-id="P2213" class="no-wikidata">48,33167°<sup id="cite_ref-nasa_2-3" class="reference"><a href="#cite_note-nasa-2">[2]</a></sup></span></td>
</tr>
<tr>
<th scope="row" class="plainlist"><a href="/wiki/%D0%90%D1%80%D0%B3%D1%83%D0%BC%D0%B5%D0%BD%D1%82_%D0%BF%D0%B5%D1%80%D0%B8%D1%86%D0%B5%D0%BD%D1%82%D1%80%D0%B0" class="mw-redirect" title="Аргумент перицентра">Аргумент перицентра</a>&nbsp;(<link rel="mw-deduplicated-inline-style" href="mw-data:TemplateStyles:r117753614"><span class="ts-math">ω</span>)</th>
<td class="plainlist">
<span data-wikidata-property-id="P2248" class="no-wikidata">29,124279°</span></td>
</tr>
<tr>
<th scope="row" class="plainlist">Чей спутник</th>
<td class="plainlist">
<span data-wikidata-claim-id="q308$60B920D3-7AAE-46E2-869E-F54BCDCB6413" class="wikidata-claim" data-wikidata-property-id="P397"><span class="wikidata-snak wikidata-main-snak"><a href="/wiki/%D0%A1%D0%BE%D0%BB%D0%BD%D1%86%D0%B5" title="Солнце">Солнце</a></span></span></td>
</tr>
<tr>
<th scope="row" class="plainlist">Спутники</th>
<td class="plainlist">
<span data-wikidata-property-id="P398" class="no-wikidata">нет</span></td>
</tr>
<tr>
<th colspan="2" scope="colgroup" class="infobox-header" style="">Физические характеристики<sup id="cite_ref-solarsystem_1-1" class="reference"><a href="#cite_note-solarsystem-1">[1]</a></sup></th>
</tr>
<tr>
<th scope="row" class="plainlist">Полярное сжатие</th>
<td class="plainlist">
<span data-wikidata-property-id="P1102" class="no-wikidata">0<sup id="cite_ref-nasa_2-4" class="reference"><a href="#cite_note-nasa-2">[2]</a></sup></span></td>
</tr>
<tr>
<th scope="row" class="plainlist"><a href="/wiki/%D0%AD%D0%BA%D0%B2%D0%B0%D1%82%D0%BE%D1%80" title="Экватор">Экваториальный</a> радиус</th>
<td class="plainlist">
2439,7 км<sup id="cite_ref-nasa_2-5" class="reference"><a href="#cite_note-nasa-2">[2]</a></sup></td>
</tr>
<tr>
<th scope="row" class="plainlist"><a href="/wiki/%D0%93%D0%B5%D0%BE%D0%B3%D1%80%D0%B0%D1%84%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B8%D0%B9_%D0%BF%D0%BE%D0%BB%D1%8E%D1%81" title="Географический полюс">Полярный</a> радиус</th>
<td class="plainlist">
2439,7 км<sup id="cite_ref-nasa_2-6" class="reference"><a href="#cite_note-nasa-2">[2]</a></sup></td>
</tr>
<tr>
<th scope="row" class="plainlist">Средний радиус</th>
<td class="plainlist">
2439,7 ± 1,0 км (0,3829 земного)<sup id="cite_ref-nasa_2-7" class="reference"><a href="#cite_note-nasa-2">[2]</a></sup></td>
</tr>
<tr>
<th scope="row" class="plainlist">Окружность большого круга</th>
<td class="plainlist">
15&nbsp;329,1 км</td>
</tr>
<tr>
<th scope="row" class="plainlist">Площадь поверхности&nbsp;(<link rel="mw-deduplicated-inline-style" href="mw-data:TemplateStyles:r117753614"><span class="ts-math"><i>S</i></span>)</th>
<td class="plainlist">
7,48⋅10<sup>7</sup> км<sup>2</sup><br>0,147 земной</td>
</tr>
<tr>
<th scope="row" class="plainlist">Объём&nbsp;(<link rel="mw-deduplicated-inline-style" href="mw-data:TemplateStyles:r117753614"><span class="ts-math"><i>V</i></span>)</th>
<td class="plainlist">
6,083⋅10<sup>10</sup> км<sup>3</sup><br>0,056 земного<sup id="cite_ref-nasa_2-8" class="reference"><a href="#cite_note-nasa-2">[2]</a></sup></td>
</tr>
<tr>
<th scope="row" class="plainlist">Масса&nbsp;(<link rel="mw-deduplicated-inline-style" href="mw-data:TemplateStyles:r117753614"><span class="ts-math"><i>m</i></span>)</th>
<td class="plainlist">
<span data-wikidata-property-id="P2067" class="no-wikidata">3,33022⋅10<sup>23</sup> кг<br>0,055274 земной<sup id="cite_ref-Язев_4-0" class="reference"><a href="#cite_note-Язев-4">[4]</a></sup><sup id="cite_ref-galspace_5-0" class="reference"><a href="#cite_note-galspace-5">[5]</a></sup></span></td>
</tr>
<tr>
<th scope="row" class="plainlist">Средняя <a href="/wiki/%D0%9F%D0%BB%D0%BE%D1%82%D0%BD%D0%BE%D1%81%D1%82%D1%8C" title="Плотность">плотность</a>&nbsp;(<link rel="mw-deduplicated-inline-style" href="mw-data:TemplateStyles:r117753614"><span class="ts-math">ρ</span>)</th>
<td class="plainlist">
5,427 г/см<sup>3</sup><br>0,984 земной<sup id="cite_ref-nasa_2-9" class="reference"><a href="#cite_note-nasa-2">[2]</a></sup></td>
</tr>
<tr>
<th scope="row" class="plainlist"><a href="/wiki/%D0%A3%D1%81%D0%BA%D0%BE%D1%80%D0%B5%D0%BD%D0%B8%D0%B5_%D1%81%D0%B2%D0%BE%D0%B1%D0%BE%D0%B4%D0%BD%D0%BE%D0%B3%D0%BE_%D0%BF%D0%B0%D0%B4%D0%B5%D0%BD%D0%B8%D1%8F" title="Ускорение свободного падения">Ускорение свободного падения</a> на экваторе&nbsp;(<link rel="mw-deduplicated-inline-style" href="mw-data:TemplateStyles:r117753614"><span class="ts-math"><i>g</i></span>)</th>
<td class="plainlist">
3,7 м/с<sup>2</sup><br>0,377 <a href="/wiki/%D0%A3%D1%81%D0%BA%D0%BE%D1%80%D0%B5%D0%BD%D0%B8%D0%B5_%D1%81%D0%B2%D0%BE%D0%B1%D0%BE%D0%B4%D0%BD%D0%BE%D0%B3%D0%BE_%D0%BF%D0%B0%D0%B4%D0%B5%D0%BD%D0%B8%D1%8F" title="Ускорение свободного падения">g</a><sup id="cite_ref-nasa_2-10" class="reference"><a href="#cite_note-nasa-2">[2]</a></sup></td>
</tr>
<tr>
<th scope="row" class="plainlist"><a href="/wiki/%D0%9F%D0%B5%D1%80%D0%B2%D0%B0%D1%8F_%D0%BA%D0%BE%D1%81%D0%BC%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B0%D1%8F_%D1%81%D0%BA%D0%BE%D1%80%D0%BE%D1%81%D1%82%D1%8C" title="Первая космическая скорость">Первая космическая скорость</a>&nbsp;(<link rel="mw-deduplicated-inline-style" href="mw-data:TemplateStyles:r117753614"><span class="ts-math"><i>v</i></span><sub>1</sub>)</th>
<td class="plainlist">
3,1 км/с</td>
</tr>
<tr>
<th scope="row" class="plainlist"><a href="/wiki/%D0%92%D1%82%D0%BE%D1%80%D0%B0%D1%8F_%D0%BA%D0%BE%D1%81%D0%BC%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B0%D1%8F_%D1%81%D0%BA%D0%BE%D1%80%D0%BE%D1%81%D1%82%D1%8C" title="Вторая космическая скорость">Вторая космическая скорость</a>&nbsp;(<link rel="mw-deduplicated-inline-style" href="mw-data:TemplateStyles:r117753614"><span class="ts-math"><i>v</i></span><sub>2</sub>)</th>
<td class="plainlist">
4,25 км/с</td>
</tr>
<tr>
<th scope="row" class="plainlist">Экваториальная скорость вращения</th>
<td class="plainlist">
10,892 км/ч (3,026 м/с) (на экваторе)</td>
</tr>
<tr>
<th scope="row" class="plainlist"><a href="/wiki/%D0%9F%D0%B5%D1%80%D0%B8%D0%BE%D0%B4_%D0%B2%D1%80%D0%B0%D1%89%D0%B5%D0%BD%D0%B8%D1%8F" title="Период вращения">Период вращения</a>&nbsp;(<link rel="mw-deduplicated-inline-style" href="mw-data:TemplateStyles:r117753614"><span class="ts-math"><i>T</i></span>)</th>
<td class="plainlist">
58,646 дня (1407,5 часа)<sup id="cite_ref-nasa_2-11" class="reference"><a href="#cite_note-nasa-2">[2]</a></sup></td>
</tr>
<tr>
<th scope="row" class="plainlist"><a href="/wiki/%D0%9D%D0%B0%D0%BA%D0%BB%D0%BE%D0%BD_%D0%BE%D1%81%D0%B8_%D0%B2%D1%80%D0%B0%D1%89%D0%B5%D0%BD%D0%B8%D1%8F" title="Наклон оси вращения">Наклон оси</a></th>
<td class="plainlist">
2,11′ ± 0,1′<sup id="cite_ref-Margot2007_6-0" class="reference"><a href="#cite_note-Margot2007-6">[6]</a></sup></td>
</tr>
<tr>
<th scope="row" class="plainlist"><a href="/wiki/%D0%9F%D1%80%D1%8F%D0%BC%D0%BE%D0%B5_%D0%B2%D0%BE%D1%81%D1%85%D0%BE%D0%B6%D0%B4%D0%B5%D0%BD%D0%B8%D0%B5" title="Прямое восхождение">Прямое восхождение</a> северного полюса&nbsp;(<link rel="mw-deduplicated-inline-style" href="mw-data:TemplateStyles:r117753614"><span class="ts-math">α</span>)</th>
<td class="plainlist">
18 ч 44 мин 2 с<br>281,01°<sup id="cite_ref-nasa_2-12" class="reference"><a href="#cite_note-nasa-2">[2]</a></sup></td>
</tr>
<tr>
<th scope="row" class="plainlist"><a href="/wiki/%D0%A1%D0%BA%D0%BB%D0%BE%D0%BD%D0%B5%D0%BD%D0%B8%D0%B5_(%D0%B0%D1%81%D1%82%D1%80%D0%BE%D0%BD%D0%BE%D0%BC%D0%B8%D1%8F)" title="Склонение (астрономия)">Склонение</a> северного полюса&nbsp;(<link rel="mw-deduplicated-inline-style" href="mw-data:TemplateStyles:r117753614"><span class="ts-math">δ</span>)</th>
<td class="plainlist">
61,45°<sup id="cite_ref-nasa_2-13" class="reference"><a href="#cite_note-nasa-2">[2]</a></sup></td>
</tr>
<tr>
<th scope="row" class="plainlist"><a href="/wiki/%D0%90%D0%BB%D1%8C%D0%B1%D0%B5%D0%B4%D0%BE" title="Альбедо">Альбедо</a></th>
<td class="plainlist">
0,068 (Бонд)<sup id="cite_ref-nasa_2-14" class="reference"><a href="#cite_note-nasa-2">[2]</a></sup><sup id="cite_ref-MallamaMercury_7-0" class="reference"><a href="#cite_note-MallamaMercury-7">[7]</a></sup><br>0,142 (геометрическое)<sup id="cite_ref-nasa_2-15" class="reference"><a href="#cite_note-nasa-2">[2]</a></sup><sup id="cite_ref-MallamaMercury_7-1" class="reference"><a href="#cite_note-MallamaMercury-7">[7]</a></sup></td>
</tr>
<tr>
<th scope="row" class="plainlist"><a href="/wiki/%D0%92%D0%B8%D0%B4%D0%B8%D0%BC%D0%B0%D1%8F_%D0%B7%D0%B2%D1%91%D0%B7%D0%B4%D0%BD%D0%B0%D1%8F_%D0%B2%D0%B5%D0%BB%D0%B8%D1%87%D0%B8%D0%BD%D0%B0" title="Видимая звёздная величина">Видимая звёздная величина</a></th>
<td class="plainlist">
<span data-wikidata-property-id="P1215" class="no-wikidata">от −2,6<sup>m</sup><sup id="cite_ref-MallamaSky_8-0" class="reference"><a href="#cite_note-MallamaSky-8">[8]</a></sup> до 5,7<sup>m</sup><sup id="cite_ref-nasa_2-16" class="reference"><a href="#cite_note-nasa-2">[2]</a></sup><sup id="cite_ref-ephemeris_9-0" class="reference"><a href="#cite_note-ephemeris-9">[9]</a></sup></span></td>
</tr>
<tr>
<th scope="row" class="plainlist"><a href="/wiki/%D0%90%D0%B1%D1%81%D0%BE%D0%BB%D1%8E%D1%82%D0%BD%D0%B0%D1%8F_%D0%B7%D0%B2%D1%91%D0%B7%D0%B4%D0%BD%D0%B0%D1%8F_%D0%B2%D0%B5%D0%BB%D0%B8%D1%87%D0%B8%D0%BD%D0%B0" title="Абсолютная звёздная величина">Абсолютная звёздная величина</a></th>
<td class="plainlist">
<span data-wikidata-property-id="P1457" class="no-wikidata">-0.01ᵐ</span></td>
</tr>
<tr>
<th scope="row" class="plainlist"><a href="/wiki/%D0%A3%D0%B3%D0%BB%D0%BE%D0%B2%D0%BE%D0%B9_%D0%B4%D0%B8%D0%B0%D0%BC%D0%B5%D1%82%D1%80" class="mw-redirect" title="Угловой диаметр">Угловой диаметр</a></th>
<td class="plainlist">
4,5–13"<sup id="cite_ref-nasa_2-17" class="reference"><a href="#cite_note-nasa-2">[2]</a></sup></td>
</tr>
<tr>
<th colspan="2" scope="colgroup" class="infobox-header" style="">Температура</th>
</tr>
<tr>
<th scope="row" class="plainlist">На поверхности</th>
<td class="plainlist">
от 80 до 700 К (от −190 до +430 °C)</td>
</tr>
<tr>
<th scope="row" class="plainlist">&nbsp;</th>
<td class="plainlist">
<table><tbody><tr style="font-weight:bold">
<td>мин.</td>
<td>сред.</td>
<td>макс.</td>
</tr></tbody></table></td>
</tr>
<tr>
<th scope="row" class="plainlist">0°N, 0°W<sup id="cite_ref-vasa_10-0" class="reference"><a href="#cite_note-vasa-10">[10]</a></sup></th>
<td class="plainlist">
<table><tbody><tr>
<td>100 K<br>(−173&nbsp;°C)</td>
<td>340 К<br>(67&nbsp;°C)</td>
<td>700 К<sup id="cite_ref-11" class="reference"><a href="#cite_note-11">[11]</a></sup><br>(427&nbsp;°C)</td>
</tr></tbody></table></td>
</tr>
<tr>
<th scope="row" class="plainlist">85°N, 0°W<sup id="cite_ref-vasa_10-1" class="reference"><a href="#cite_note-vasa-10">[10]</a></sup></th>
<td class="plainlist">
<table><tbody><tr>
<td>80 К<br>(−193&nbsp;°C)</td>
<td>200 К<br>(−73&nbsp;°C)</td>
<td>380 К<br>(107&nbsp;°C)</td>
</tr></tbody></table></td>
</tr>
<tr>
<th colspan="2" scope="colgroup" class="infobox-header" style=""><a href="/wiki/%D0%90%D1%82%D0%BC%D0%BE%D1%81%D1%84%D0%B5%D1%80%D0%B0" title="Атмосфера">Атмосфера</a><sup id="cite_ref-nasa_2-18" class="reference"><a href="#cite_note-nasa-2">[2]</a></sup></th>
</tr>
<tr>
<th scope="row" class="plainlist"><a href="/wiki/%D0%90%D1%82%D0%BC%D0%BE%D1%81%D1%84%D0%B5%D1%80%D0%BD%D0%BE%D0%B5_%D0%B4%D0%B0%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5" title="Атмосферное давление">Атмосферное давление</a></th>
<td class="plainlist">
≲ 5⋅10<sup>−15</sup> бар<sup id="cite_ref-nasa_2-19" class="reference"><a href="#cite_note-nasa-2">[2]</a></sup></td>
</tr>
<tr>
<td colspan="2" class="plainlist" style="text-align:center;">
<div style="text-align:left"><b>Состав:</b> <div style="margin-left:1em">42,0&nbsp;% <a href="/wiki/%D0%9A%D0%B8%D1%81%D0%BB%D0%BE%D1%80%D0%BE%D0%B4" title="Кислород">кислород</a><br>29,0&nbsp;% <a href="/wiki/%D0%9D%D0%B0%D1%82%D1%80%D0%B8%D0%B9" title="Натрий">натрий</a><br>22,0&nbsp;% <a href="/wiki/%D0%92%D0%BE%D0%B4%D0%BE%D1%80%D0%BE%D0%B4" title="Водород">водород</a><br>6,0&nbsp;% <a href="/wiki/%D0%93%D0%B5%D0%BB%D0%B8%D0%B9" title="Гелий">гелий</a><br>0,5&nbsp;% <a href="/wiki/%D0%9A%D0%B0%D0%BB%D0%B8%D0%B9" title="Калий">калий</a><br>0,5&nbsp;% остальные (<a href="/wiki/%D0%92%D0%BE%D0%B4%D0%B0" title="Вода">вода</a>, <a href="/wiki/%D0%9E%D0%BA%D1%81%D0%B8%D0%B4_%D1%83%D0%B3%D0%BB%D0%B5%D1%80%D0%BE%D0%B4%D0%B0(IV)" class="mw-redirect" title="Оксид углерода(IV)">углекислый газ</a>, <a href="/wiki/%D0%90%D0%B7%D0%BE%D1%82" title="Азот">азот</a>, <a href="/wiki/%D0%90%D1%80%D0%B3%D0%BE%D0%BD" title="Аргон">аргон</a>, <a href="/wiki/%D0%9A%D1%81%D0%B5%D0%BD%D0%BE%D0%BD" title="Ксенон">ксенон</a>, <a href="/wiki/%D0%9A%D1%80%D0%B8%D0%BF%D1%82%D0%BE%D0%BD" title="Криптон">криптон</a>, <a href="/wiki/%D0%9D%D0%B5%D0%BE%D0%BD" title="Неон">неон</a>, <a href="/wiki/%D0%9A%D0%B0%D0%BB%D1%8C%D1%86%D0%B8%D0%B9" title="Кальций">кальций</a>, <a href="/wiki/%D0%9C%D0%B0%D0%B3%D0%BD%D0%B8%D0%B9" title="Магний">магний</a>)<sup id="cite_ref-nasa_2-20" class="reference"><a href="#cite_note-nasa-2">[2]</a></sup><sup id="cite_ref-galspace_5-1" class="reference"><a href="#cite_note-galspace-5">[5]</a></sup></div></div></td>
</tr><tr><td colspan="2" class="infobox-below" style=";"><span data-wikidata-claim-id="q308$8529E207-64AA-4B0D-ADC7-212EE05B5A28" class="wikidata-claim" data-wikidata-property-id="P373"><span class="wikidata-snak wikidata-main-snak"><a href="https://commons.wikimedia.org/wiki/Category:Mercury_(planet)" title="commons:Category:Mercury (planet)"><img alt="Логотип Викисклада" src="//upload.wikimedia.org/wikipedia/commons/thumb/4/4a/Commons-logo.svg/15px-Commons-logo.svg.png" decoding="async" width="15" height="20" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/4/4a/Commons-logo.svg/23px-Commons-logo.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/4/4a/Commons-logo.svg/30px-Commons-logo.svg.png 2x" data-file-width="1024" data-file-height="1376"></a>&nbsp;<a href="https://commons.wikimedia.org/wiki/Category:Mercury_(planet)" class="extiw" title="commons:Category:Mercury (planet)">Медиафайлы на Викискладе</a></span></span></td></tr><tr><td colspan="2" class="infobox-below" style=";"><a href="https://www.wikidata.org/wiki/Special:ItemByTitle/ruwiki/%D0%9C%D0%B5%D1%80%D0%BA%D1%83%D1%80%D0%B8%D0%B9" title="d:Special:ItemByTitle/ruwiki/Меркурий"><img alt="Логотип Викиданных" src="//upload.wikimedia.org/wikipedia/commons/thumb/e/e4/Wikidata-logo_S.svg/18px-Wikidata-logo_S.svg.png" decoding="async" width="18" height="10" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/e/e4/Wikidata-logo_S.svg/27px-Wikidata-logo_S.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/e/e4/Wikidata-logo_S.svg/36px-Wikidata-logo_S.svg.png 2x" data-file-width="1050" data-file-height="590"></a> <a href="https://www.wikidata.org/wiki/d:Special:ItemByTitle/ruwiki/%D0%9C%D0%B5%D1%80%D0%BA%D1%83%D1%80%D0%B8%D0%B9" class="extiw" title="d:d:Special:ItemByTitle/ruwiki/Меркурий">Информация в Викиданных</a>&nbsp;<sup><style data-mw-deduplicate="TemplateStyles:r113275842">.mw-parser-output .ts-comment-commentedText{border-bottom:1px dotted;cursor:help}@media(hover:none){.mw-parser-output .ts-comment-commentedText:not(.rt-commentedText){border-bottom:0;cursor:auto}}</style><span class="ts-comment-commentedText" title="Элементы карточки, которых нет в окне редактирования статьи, редактируются в Викиданных">?</span></sup></td></tr>
</tbody></table>
</div>
<div class="col">
    <h2>Минусы</h2>
    <div class="alert alert-danger">Очень высокая температура</div>
    <div class="alert alert-danger">Далеко</div>
    <br><br>
    <div class="alert alert-info">Эта планета не подходит для колонизации</div>
</div>
</div>
</div>
</body>
</html>
"""
    if planet_name == "Венера":
        return """
<!doctype html>
<html>
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Венера</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha2/dist/css/bootstrap.min.css" rel="stylesheet"
    integrity="sha384-aFq/bzH65dt+w6FI2ooMVUpc+21e0SRygnTpmBvdBgSdnuTN7QbdgL+OapgHtvPp" crossorigin="anonymous">
    <link rel="stylesheet" type="text/css" href="../static/css/style.css"/>
</head>
<body>
    <div class="table">
    <div class="row">
    <div class="col">
    <table class="infobox infobox-dc537cc90b707c80" style="width:27em;" data-name="Планета"><tbody><tr><th colspan="2" scope="colgroup" class="infobox-above" style="">Венера <span data-wikidata-property-id="P367" class="no-wikidata"><a href="//commons.wikimedia.org/wiki/File:Venus_symbol_(bold).svg?uselang=ru" class="image"><img alt="Venus symbol (bold).svg" src="//upload.wikimedia.org/wikipedia/commons/thumb/0/00/Venus_symbol_%28bold%29.svg/20px-Venus_symbol_%28bold%29.svg.png" decoding="async" width="20" height="20" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/0/00/Venus_symbol_%28bold%29.svg/30px-Venus_symbol_%28bold%29.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/0/00/Venus_symbol_%28bold%29.svg/40px-Venus_symbol_%28bold%29.svg.png 2x" data-file-width="15" data-file-height="15"></a></span></th></tr><tr><td colspan="2" class="" style="text-align:center;"><a href="/wiki/%D0%9F%D0%BB%D0%B0%D0%BD%D0%B5%D1%82%D0%B0" title="Планета">Планета</a></td></tr><tr><td colspan="2" class="infobox-image" style=""> <table role="presentation" style="background-color:#FFFFFFu;border-collapse:collapse;border:0px solid black;width:280px;margin-left: auto; margin-right: auto;"><tbody><tr><td style="border-top:0;padding:2px 0 0 2px"><table role="presentation" style="background-color:#FFFFFFu;border-collapse:collapse"><tbody><tr><td style="border-top:0;padding:0 2px 2px 0"><a href="//commons.wikimedia.org/wiki/File:Venus_from_Mariner_10.jpg?uselang=ru" class="image"><img alt="Venus from Mariner 10.jpg" src="//upload.wikimedia.org/wikipedia/commons/thumb/0/08/Venus_from_Mariner_10.jpg/280px-Venus_from_Mariner_10.jpg" decoding="async" width="280" height="280" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/0/08/Venus_from_Mariner_10.jpg/420px-Venus_from_Mariner_10.jpg 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/0/08/Venus_from_Mariner_10.jpg/560px-Venus_from_Mariner_10.jpg 2x" data-file-width="1000" data-file-height="1000"></a></td></tr></tbody></table></td></tr></tbody></table>
<div style="font-size:smaller">Венера в видимом и ультрафиолетовом свете, снимок сделан <a href="/wiki/%D0%90%D0%B2%D1%82%D0%BE%D0%BC%D0%B0%D1%82%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B0%D1%8F_%D0%BC%D0%B5%D0%B6%D0%BF%D0%BB%D0%B0%D0%BD%D0%B5%D1%82%D0%BD%D0%B0%D1%8F_%D1%81%D1%82%D0%B0%D0%BD%D1%86%D0%B8%D1%8F" title="Автоматическая межпланетная станция">АМС</a> <a href="/wiki/%D0%9C%D0%B0%D1%80%D0%B8%D0%BD%D0%B5%D1%80-10" title="Маринер-10">Маринер-10</a> 7 февраля 1974 года</div> </td></tr>
<tr>
<th colspan="2" scope="colgroup" class="infobox-header" style="">Орбитальные характеристики</th>
</tr>
<tr>
<td colspan="2" class="plainlist" style="text-align:center;">
<a href="/wiki/%D0%AD%D0%BF%D0%BE%D1%85%D0%B0_(%D0%B0%D1%81%D1%82%D1%80%D0%BE%D0%BD%D0%BE%D0%BC%D0%B8%D1%8F)" title="Эпоха (астрономия)">Эпоха</a>: J2000.0</td>
</tr>
<tr>
<th scope="row" class="plainlist"><a href="/wiki/%D0%9F%D0%B5%D1%80%D0%B8%D0%B3%D0%B5%D0%BB%D0%B8%D0%B9" title="Перигелий">Перигелий</a></th>
<td class="plainlist">
<span data-wikidata-property-id="P2244" class="no-wikidata">107&nbsp;476&nbsp;259&nbsp;км<br>0,71843270&nbsp;<a href="/wiki/%D0%90%D1%81%D1%82%D1%80%D0%BE%D0%BD%D0%BE%D0%BC%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B0%D1%8F_%D0%B5%D0%B4%D0%B8%D0%BD%D0%B8%D1%86%D0%B0" title="Астрономическая единица">а.е.</a></span></td>
</tr>
<tr>
<th scope="row" class="plainlist"><a href="/wiki/%D0%90%D1%84%D0%B5%D0%BB%D0%B8%D0%B9" title="Афелий">Афелий</a></th>
<td class="plainlist">
<span data-wikidata-property-id="P2243" class="no-wikidata">108&nbsp;942&nbsp;109&nbsp;км<br>0,72823128&nbsp;<a href="/wiki/%D0%90%D1%81%D1%82%D1%80%D0%BE%D0%BD%D0%BE%D0%BC%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B0%D1%8F_%D0%B5%D0%B4%D0%B8%D0%BD%D0%B8%D1%86%D0%B0" title="Астрономическая единица">а.е.</a></span></td>
</tr>
<tr>
<th scope="row" class="plainlist"><a href="/wiki/%D0%91%D0%BE%D0%BB%D1%8C%D1%88%D0%B0%D1%8F_%D0%BF%D0%BE%D0%BB%D1%83%D0%BE%D1%81%D1%8C" title="Большая полуось">Большая полуось</a>&nbsp;(<style data-mw-deduplicate="TemplateStyles:r117753614">.mw-parser-output .ts-math{white-space:nowrap;font-family:times,serif,palatino linotype,new athena unicode,athena,gentium,code2000;font-size:120%}</style><span class="ts-math"><i>a</i></span>)</th>
<td class="plainlist">
<span data-wikidata-property-id="P2233" class="no-wikidata">108&nbsp;208&nbsp;930&nbsp;км<br>0,723332&nbsp;<a href="/wiki/%D0%90%D1%81%D1%82%D1%80%D0%BE%D0%BD%D0%BE%D0%BC%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B0%D1%8F_%D0%B5%D0%B4%D0%B8%D0%BD%D0%B8%D1%86%D0%B0" title="Астрономическая единица">а.е.</a></span></td>
</tr>
<tr>
<th scope="row" class="plainlist"><a href="/wiki/%D0%AD%D0%BA%D1%81%D1%86%D0%B5%D0%BD%D1%82%D1%80%D0%B8%D1%81%D0%B8%D1%82%D0%B5%D1%82_%D0%BE%D1%80%D0%B1%D0%B8%D1%82%D1%8B" title="Эксцентриситет орбиты">Эксцентриситет орбиты</a>&nbsp;(<link rel="mw-deduplicated-inline-style" href="mw-data:TemplateStyles:r117753614"><span class="ts-math"><i>e</i></span>)</th>
<td class="plainlist">
<span data-wikidata-property-id="P1096" class="no-wikidata">0,0068</span></td>
</tr>
<tr>
<th scope="row" class="plainlist"><a href="/wiki/%D0%A1%D0%B8%D0%B4%D0%B5%D1%80%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B8%D0%B9_%D0%BF%D0%B5%D1%80%D0%B8%D0%BE%D0%B4" title="Сидерический период">Сидерический период</a> обращения</th>
<td class="plainlist">
<span data-wikidata-property-id="P2146" class="no-wikidata">224,701&nbsp;<a href="/wiki/%D0%A1%D1%83%D1%82%D0%BA%D0%B8#Международная_система_единиц_(СИ)" title="Сутки">сут</a><sup id="cite_ref-1" class="reference"><a href="#cite_note-1">[1]</a></sup></span></td>
</tr>
<tr>
<th scope="row" class="plainlist"><a href="/wiki/%D0%A1%D0%B8%D0%BD%D0%BE%D0%B4%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B8%D0%B9_%D0%BF%D0%B5%D1%80%D0%B8%D0%BE%D0%B4" title="Синодический период">Синодический период</a> обращения</th>
<td class="plainlist">
<span data-wikidata-property-id="P4341" class="no-wikidata">583,92&nbsp;сут</span></td>
</tr>
<tr>
<th scope="row" class="plainlist"><a href="/wiki/%D0%9E%D1%80%D0%B1%D0%B8%D1%82%D0%B0%D0%BB%D1%8C%D0%BD%D0%B0%D1%8F_%D1%81%D0%BA%D0%BE%D1%80%D0%BE%D1%81%D1%82%D1%8C" title="Орбитальная скорость">Орбитальная скорость</a>&nbsp;(<link rel="mw-deduplicated-inline-style" href="mw-data:TemplateStyles:r117753614"><span class="ts-math"><i>v</i></span>)</th>
<td class="plainlist">
35,02&nbsp;км/с</td>
</tr>
<tr>
<th scope="row" class="plainlist"><a href="/wiki/%D0%9A%D0%B5%D0%BF%D0%BB%D0%B5%D1%80%D0%BE%D0%B2%D1%8B_%D1%8D%D0%BB%D0%B5%D0%BC%D0%B5%D0%BD%D1%82%D1%8B_%D0%BE%D1%80%D0%B1%D0%B8%D1%82%D1%8B#Наклонение" title="Кеплеровы элементы орбиты">Наклонение</a>&nbsp;(<link rel="mw-deduplicated-inline-style" href="mw-data:TemplateStyles:r117753614"><span class="ts-math"><i>i</i></span>)</th>
<td class="plainlist">
<span data-wikidata-property-id="P2045" class="no-wikidata">3,86° (относительно солнечного экватора);<br> 3,39458° (относительно эклиптики); <br> 2,5° (относительно инвариантной плоскости)</span></td>
</tr>
<tr>
<th scope="row" class="plainlist"><a href="/wiki/%D0%94%D0%BE%D0%BB%D0%B3%D0%BE%D1%82%D0%B0_%D0%B2%D0%BE%D1%81%D1%85%D0%BE%D0%B4%D1%8F%D1%89%D0%B5%D0%B3%D0%BE_%D1%83%D0%B7%D0%BB%D0%B0" class="mw-redirect" title="Долгота восходящего узла">Долгота восходящего узла</a>&nbsp;(<link rel="mw-deduplicated-inline-style" href="mw-data:TemplateStyles:r117753614"><span class="ts-math">Ω</span>)</th>
<td class="plainlist">
<span data-wikidata-property-id="P2213" class="no-wikidata">76,67069°</span></td>
</tr>
<tr>
<th scope="row" class="plainlist"><a href="/wiki/%D0%90%D1%80%D0%B3%D1%83%D0%BC%D0%B5%D0%BD%D1%82_%D0%BF%D0%B5%D1%80%D0%B8%D1%86%D0%B5%D0%BD%D1%82%D1%80%D0%B0" class="mw-redirect" title="Аргумент перицентра">Аргумент перицентра</a>&nbsp;(<link rel="mw-deduplicated-inline-style" href="mw-data:TemplateStyles:r117753614"><span class="ts-math">ω</span>)</th>
<td class="plainlist">
<span data-wikidata-property-id="P2248" class="no-wikidata">54,85229°</span></td>
</tr>
<tr>
<th scope="row" class="plainlist">Чей спутник</th>
<td class="plainlist">
<span data-wikidata-claim-id="q313$B762BBB9-861C-48F8-BB73-CDAF1C68C361" class="wikidata-claim" data-wikidata-property-id="P397"><span class="wikidata-snak wikidata-main-snak"><a href="/wiki/%D0%A1%D0%BE%D0%BB%D0%BD%D1%86%D0%B5" title="Солнце">Солнце</a></span></span></td>
</tr>
<tr>
<th scope="row" class="plainlist">Спутники</th>
<td class="plainlist">
<span data-wikidata-property-id="P398" class="no-wikidata"><a href="/wiki/%D0%A1%D0%BF%D1%83%D1%82%D0%BD%D0%B8%D0%BA%D0%B8_%D0%92%D0%B5%D0%BD%D0%B5%D1%80%D1%8B" title="Спутники Венеры">нет</a></span></td>
</tr>
<tr>
<th colspan="2" scope="colgroup" class="infobox-header" style="">Физические характеристики</th>
</tr>
<tr>
<th scope="row" class="plainlist">Полярное сжатие</th>
<td class="plainlist">
<span data-wikidata-property-id="P1102" class="no-wikidata">0</span></td>
</tr>
<tr>
<th scope="row" class="plainlist">Средний радиус</th>
<td class="plainlist">
<p>6051,8&nbsp;±&nbsp;1,0&nbsp;км<sup id="cite_ref-Archinal_2011_2-0" class="reference"><a href="#cite_note-Archinal_2011-2">[2]</a></sup>
</p>
0,9499 земных</td>
</tr>
<tr>
<th scope="row" class="plainlist">Площадь поверхности&nbsp;(<link rel="mw-deduplicated-inline-style" href="mw-data:TemplateStyles:r117753614"><span class="ts-math"><i>S</i></span>)</th>
<td class="plainlist">
4,60⋅10<sup>8</sup>&nbsp;км²<br>0,902&nbsp;земных</td>
</tr>
<tr>
<th scope="row" class="plainlist">Объём&nbsp;(<link rel="mw-deduplicated-inline-style" href="mw-data:TemplateStyles:r117753614"><span class="ts-math"><i>V</i></span>)</th>
<td class="plainlist">
9,38⋅10<sup>11</sup>&nbsp;км³<br>0,857&nbsp;земных</td>
</tr>
<tr>
<th scope="row" class="plainlist">Масса&nbsp;(<link rel="mw-deduplicated-inline-style" href="mw-data:TemplateStyles:r117753614"><span class="ts-math"><i>m</i></span>)</th>
<td class="plainlist">
<span data-wikidata-property-id="P2067" class="no-wikidata">4,8675⋅10<sup>24</sup>&nbsp;кг<sup id="cite_ref-nssdc_3-0" class="reference"><a href="#cite_note-nssdc-3">[3]</a></sup><br>0,815&nbsp;земных</span></td>
</tr>
<tr>
<th scope="row" class="plainlist">Средняя <a href="/wiki/%D0%9F%D0%BB%D0%BE%D1%82%D0%BD%D0%BE%D1%81%D1%82%D1%8C" title="Плотность">плотность</a>&nbsp;(<link rel="mw-deduplicated-inline-style" href="mw-data:TemplateStyles:r117753614"><span class="ts-math">ρ</span>)</th>
<td class="plainlist">
5,24&nbsp;г/см³<sup id="cite_ref-nssdc_3-1" class="reference"><a href="#cite_note-nssdc-3">[3]</a></sup></td>
</tr>
<tr>
<th scope="row" class="plainlist"><a href="/wiki/%D0%A3%D1%81%D0%BA%D0%BE%D1%80%D0%B5%D0%BD%D0%B8%D0%B5_%D1%81%D0%B2%D0%BE%D0%B1%D0%BE%D0%B4%D0%BD%D0%BE%D0%B3%D0%BE_%D0%BF%D0%B0%D0%B4%D0%B5%D0%BD%D0%B8%D1%8F" title="Ускорение свободного падения">Ускорение свободного падения</a> на экваторе&nbsp;(<link rel="mw-deduplicated-inline-style" href="mw-data:TemplateStyles:r117753614"><span class="ts-math"><i>g</i></span>)</th>
<td class="plainlist">
8,87&nbsp;м/с²<br>0,904&nbsp;<a href="/wiki/%D0%A3%D1%81%D0%BA%D0%BE%D1%80%D0%B5%D0%BD%D0%B8%D0%B5_%D1%81%D0%B2%D0%BE%D0%B1%D0%BE%D0%B4%D0%BD%D0%BE%D0%B3%D0%BE_%D0%BF%D0%B0%D0%B4%D0%B5%D0%BD%D0%B8%D1%8F" title="Ускорение свободного падения">g</a></td>
</tr>
<tr>
<th scope="row" class="plainlist"><a href="/wiki/%D0%9F%D0%B5%D1%80%D0%B2%D0%B0%D1%8F_%D0%BA%D0%BE%D1%81%D0%BC%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B0%D1%8F_%D1%81%D0%BA%D0%BE%D1%80%D0%BE%D1%81%D1%82%D1%8C" title="Первая космическая скорость">Первая космическая скорость</a>&nbsp;(<link rel="mw-deduplicated-inline-style" href="mw-data:TemplateStyles:r117753614"><span class="ts-math"><i>v</i></span><sub>1</sub>)</th>
<td class="plainlist">
7,328 км/с</td>
</tr>
<tr>
<th scope="row" class="plainlist"><a href="/wiki/%D0%92%D1%82%D0%BE%D1%80%D0%B0%D1%8F_%D0%BA%D0%BE%D1%81%D0%BC%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B0%D1%8F_%D1%81%D0%BA%D0%BE%D1%80%D0%BE%D1%81%D1%82%D1%8C" title="Вторая космическая скорость">Вторая космическая скорость</a>&nbsp;(<link rel="mw-deduplicated-inline-style" href="mw-data:TemplateStyles:r117753614"><span class="ts-math"><i>v</i></span><sub>2</sub>)</th>
<td class="plainlist">
10,363&nbsp;км/с</td>
</tr>
<tr>
<th scope="row" class="plainlist">Экваториальная скорость вращения</th>
<td class="plainlist">
6,52&nbsp;км/ч</td>
</tr>
<tr>
<th scope="row" class="plainlist"><a href="/wiki/%D0%9F%D0%B5%D1%80%D0%B8%D0%BE%D0%B4_%D0%B2%D1%80%D0%B0%D1%89%D0%B5%D0%BD%D0%B8%D1%8F" title="Период вращения">Период вращения</a>&nbsp;(<link rel="mw-deduplicated-inline-style" href="mw-data:TemplateStyles:r117753614"><span class="ts-math"><i>T</i></span>)</th>
<td class="plainlist">
243,023±0,002&nbsp;дней<sup id="cite_ref-4" class="reference"><a href="#cite_note-4">[4]</a></sup></td>
</tr>
<tr>
<th scope="row" class="plainlist"><a href="/wiki/%D0%9D%D0%B0%D0%BA%D0%BB%D0%BE%D0%BD_%D0%BE%D1%81%D0%B8_%D0%B2%D1%80%D0%B0%D1%89%D0%B5%D0%BD%D0%B8%D1%8F" title="Наклон оси вращения">Наклон оси</a></th>
<td class="plainlist">
177,36°<sup id="cite_ref-nssdc_3-2" class="reference"><a href="#cite_note-nssdc-3">[3]</a></sup></td>
</tr>
<tr>
<th scope="row" class="plainlist"><a href="/wiki/%D0%9F%D1%80%D1%8F%D0%BC%D0%BE%D0%B5_%D0%B2%D0%BE%D1%81%D1%85%D0%BE%D0%B6%D0%B4%D0%B5%D0%BD%D0%B8%D0%B5" title="Прямое восхождение">Прямое восхождение</a> северного полюса&nbsp;(<link rel="mw-deduplicated-inline-style" href="mw-data:TemplateStyles:r117753614"><span class="ts-math">α</span>)</th>
<td class="plainlist">
18&nbsp;ч 11&nbsp;мин 2&nbsp;с<br>272,76°<sup id="cite_ref-Archinal_2011_2-1" class="reference"><a href="#cite_note-Archinal_2011-2">[2]</a></sup></td>
</tr>
<tr>
<th scope="row" class="plainlist"><a href="/wiki/%D0%A1%D0%BA%D0%BB%D0%BE%D0%BD%D0%B5%D0%BD%D0%B8%D0%B5_(%D0%B0%D1%81%D1%82%D1%80%D0%BE%D0%BD%D0%BE%D0%BC%D0%B8%D1%8F)" title="Склонение (астрономия)">Склонение</a> северного полюса&nbsp;(<link rel="mw-deduplicated-inline-style" href="mw-data:TemplateStyles:r117753614"><span class="ts-math">δ</span>)</th>
<td class="plainlist">
67,16°<sup id="cite_ref-Archinal_2011_2-2" class="reference"><a href="#cite_note-Archinal_2011-2">[2]</a></sup></td>
</tr>
<tr>
<th scope="row" class="plainlist"><a href="/wiki/%D0%90%D0%BB%D1%8C%D0%B1%D0%B5%D0%B4%D0%BE" title="Альбедо">Альбедо</a></th>
<td class="plainlist">
0,67 (геометрическое),<br>0,77 (Бонда)<sup id="cite_ref-nssdc_3-3" class="reference"><a href="#cite_note-nssdc-3">[3]</a></sup></td>
</tr>
<tr>
<th scope="row" class="plainlist"><a href="/wiki/%D0%92%D0%B8%D0%B4%D0%B8%D0%BC%D0%B0%D1%8F_%D0%B7%D0%B2%D1%91%D0%B7%D0%B4%D0%BD%D0%B0%D1%8F_%D0%B2%D0%B5%D0%BB%D0%B8%D1%87%D0%B8%D0%BD%D0%B0" title="Видимая звёздная величина">Видимая звёздная величина</a></th>
<td class="plainlist">
<span data-wikidata-property-id="P1215" class="no-wikidata">−4,6<sup id="cite_ref-nssdc_3-4" class="reference"><a href="#cite_note-nssdc-3">[3]</a></sup></span></td>
</tr>
<tr>
<th scope="row" class="plainlist"><a href="/wiki/%D0%A3%D0%B3%D0%BB%D0%BE%D0%B2%D0%BE%D0%B9_%D0%B4%D0%B8%D0%B0%D0%BC%D0%B5%D1%82%D1%80" class="mw-redirect" title="Угловой диаметр">Угловой диаметр</a></th>
<td class="plainlist">
<span class="nowrap">9,7"–66,0"</span><sup id="cite_ref-nssdc_3-5" class="reference"><a href="#cite_note-nssdc-3">[3]</a></sup></td>
</tr>
<tr>
<th colspan="2" scope="colgroup" class="infobox-header" style="">Температура</th>
</tr>
<tr>
<th scope="row" class="plainlist">На поверхности</th>
<td class="plainlist">
737&nbsp;К<sup id="cite_ref-nssdc_3-6" class="reference"><a href="#cite_note-nssdc-3">[3]</a></sup><sup id="cite_ref-compare_5-0" class="reference"><a href="#cite_note-compare-5">[5]</a></sup><br>(464 °C)</td>
</tr>
<tr>
<th colspan="2" scope="colgroup" class="infobox-header" style=""><a href="/wiki/%D0%90%D1%82%D0%BC%D0%BE%D1%81%D1%84%D0%B5%D1%80%D0%B0" title="Атмосфера">Атмосфера</a><sup id="cite_ref-ESS_2014_Venus_atm_6-0" class="reference"><a href="#cite_note-ESS_2014_Venus_atm-6">[6]</a></sup></th>
</tr>
<tr>
<th scope="row" class="plainlist"><a href="/wiki/%D0%90%D1%82%D0%BC%D0%BE%D1%81%D1%84%D0%B5%D1%80%D0%BD%D0%BE%D0%B5_%D0%B4%D0%B0%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5" title="Атмосферное давление">Атмосферное давление</a></th>
<td class="plainlist">
9,3&nbsp;МПа (93 бар)</td>
</tr>
<tr>
<td colspan="2" class="plainlist" style="text-align:center;">
<div style="text-align:left"><b>Состав:</b> <div style="margin-left:1em">~96,5&nbsp;% <a href="/wiki/%D0%9E%D0%BA%D1%81%D0%B8%D0%B4_%D1%83%D0%B3%D0%BB%D0%B5%D1%80%D0%BE%D0%B4%D0%B0(IV)" class="mw-redirect" title="Оксид углерода(IV)">углекислый газ</a> (CO<sub>2</sub>)<br>~3,5&nbsp;% <a href="/wiki/%D0%90%D0%B7%D0%BE%D1%82" title="Азот">азот</a> (N<sub>2</sub>)<br>0,018&nbsp;% <a href="/wiki/%D0%9E%D0%BA%D1%81%D0%B8%D0%B4_%D1%81%D0%B5%D1%80%D1%8B(IV)" title="Оксид серы(IV)">диоксид серы</a> (SO<sub>2</sub>)<br>0,007&nbsp;% <a href="/wiki/%D0%90%D1%80%D0%B3%D0%BE%D0%BD" title="Аргон">аргон</a> (Ar)<br>0,003&nbsp;% <a href="/wiki/%D0%92%D0%BE%D0%B4%D0%B0" title="Вода">водяной пар</a> (H<sub>2</sub>O)<br>0,0017&nbsp;% <a href="/wiki/%D0%9E%D0%BA%D1%81%D0%B8%D0%B4_%D1%83%D0%B3%D0%BB%D0%B5%D1%80%D0%BE%D0%B4%D0%B0(II)" class="mw-redirect" title="Оксид углерода(II)">угарный газ</a> (CO)<br>0,0012&nbsp;% <a href="/wiki/%D0%93%D0%B5%D0%BB%D0%B8%D0%B9" title="Гелий">гелий</a> (He)<br>0,0007&nbsp;% <a href="/wiki/%D0%9D%D0%B5%D0%BE%D0%BD" title="Неон">неон</a> (Ne)<br>следы <a href="/wiki/%D0%A5%D0%BB%D0%BE%D1%80%D0%BE%D0%B2%D0%BE%D0%B4%D0%BE%D1%80%D0%BE%D0%B4" title="Хлороводород">хлороводорода</a> (HCl), <a href="/wiki/%D0%A4%D1%82%D0%BE%D1%80%D0%BE%D0%B2%D0%BE%D0%B4%D0%BE%D1%80%D0%BE%D0%B4" title="Фтороводород">фтороводорода</a> (HF), <a href="/wiki/%D0%9A%D1%80%D0%B8%D0%BF%D1%82%D0%BE%D0%BD" title="Криптон">криптона</a> (Kr), <a href="/wiki/%D0%9A%D1%81%D0%B5%D0%BD%D0%BE%D0%BD" title="Ксенон">ксенона</a> (Xe) и др.</div></div></td>
</tr><tr><td colspan="2" class="infobox-below" style=";"><span data-wikidata-claim-id="q313$901F0478-4824-4868-ADD3-CADEFDD14800" class="wikidata-claim" data-wikidata-property-id="P373"><span class="wikidata-snak wikidata-main-snak"><a href="https://commons.wikimedia.org/wiki/Category:Venus_(planet)" title="commons:Category:Venus (planet)"><img alt="Логотип Викисклада" src="//upload.wikimedia.org/wikipedia/commons/thumb/4/4a/Commons-logo.svg/15px-Commons-logo.svg.png" decoding="async" width="15" height="20" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/4/4a/Commons-logo.svg/23px-Commons-logo.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/4/4a/Commons-logo.svg/30px-Commons-logo.svg.png 2x" data-file-width="1024" data-file-height="1376"></a>&nbsp;<a href="https://commons.wikimedia.org/wiki/Category:Venus_(planet)" class="extiw" title="commons:Category:Venus (planet)">Медиафайлы на Викискладе</a></span></span></td></tr><tr><td colspan="2" class="infobox-below" style=";"><a href="https://www.wikidata.org/wiki/Special:ItemByTitle/ruwiki/%D0%92%D0%B5%D0%BD%D0%B5%D1%80%D0%B0" title="d:Special:ItemByTitle/ruwiki/Венера"><img alt="Логотип Викиданных" src="//upload.wikimedia.org/wikipedia/commons/thumb/e/e4/Wikidata-logo_S.svg/18px-Wikidata-logo_S.svg.png" decoding="async" width="18" height="10" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/e/e4/Wikidata-logo_S.svg/27px-Wikidata-logo_S.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/e/e4/Wikidata-logo_S.svg/36px-Wikidata-logo_S.svg.png 2x" data-file-width="1050" data-file-height="590"></a> <a href="https://www.wikidata.org/wiki/d:Special:ItemByTitle/ruwiki/%D0%92%D0%B5%D0%BD%D0%B5%D1%80%D0%B0" class="extiw" title="d:d:Special:ItemByTitle/ruwiki/Венера">Информация в Викиданных</a>&nbsp;<sup><style data-mw-deduplicate="TemplateStyles:r113275842">.mw-parser-output .ts-comment-commentedText{border-bottom:1px dotted;cursor:help}@media(hover:none){.mw-parser-output .ts-comment-commentedText:not(.rt-commentedText){border-bottom:0;cursor:auto}}</style><span class="ts-comment-commentedText" title="Элементы карточки, которых нет в окне редактирования статьи, редактируются в Викиданных">?</span></sup></td></tr>
</tbody></table>
</div>
    <div class="col">
        <h2>Плюсы</h2>
        <div class="alert alert-success">Близко</div>
        <h2>Минусы</h2>
        <div class="alert alert-danger">Экстремально Высокая температура</div>
        <br><br>
        <div class="alert alert-info">Эта планета не подходит для колонизации</div>
    </div>
</body>
</html>
"""
    if planet_name == "Земля":
        return """
<!doctype html>
<html>
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Земля</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha2/dist/css/bootstrap.min.css" rel="stylesheet"
    integrity="sha384-aFq/bzH65dt+w6FI2ooMVUpc+21e0SRygnTpmBvdBgSdnuTN7QbdgL+OapgHtvPp" crossorigin="anonymous">
    <link rel="stylesheet" type="text/css" href="../static/css/style.css"/>
</head>
<body>
    <div class="table">
    <div class="row">
    <div class="col">
    <table class="infobox infobox-d53683ff5e537834" style="width:27em;" data-name="Планета"><tbody><tr><th colspan="2" scope="colgroup" class="infobox-above" style="">Земля <span data-wikidata-property-id="P367" class="no-wikidata"><a href="//commons.wikimedia.org/wiki/File:Earth_symbol_(bold).svg?uselang=ru" class="image"><img alt="Earth symbol (bold).svg" src="//upload.wikimedia.org/wikipedia/commons/thumb/0/0a/Earth_symbol_%28bold%29.svg/20px-Earth_symbol_%28bold%29.svg.png" decoding="async" width="20" height="20" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/0/0a/Earth_symbol_%28bold%29.svg/30px-Earth_symbol_%28bold%29.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/0/0a/Earth_symbol_%28bold%29.svg/40px-Earth_symbol_%28bold%29.svg.png 2x" data-file-width="15" data-file-height="15"></a></span></th></tr><tr><td colspan="2" class="" style="text-align:center;"><a href="/wiki/%D0%9F%D0%BB%D0%B0%D0%BD%D0%B5%D1%82%D0%B0" title="Планета">Планета</a></td></tr><tr><td colspan="2" class="infobox-image" style=""> <span data-wikidata-property-id="P18" class="no-wikidata"><a href="//commons.wikimedia.org/wiki/File:Africa_and_Europe_from_a_Million_Miles_Away.png?uselang=ru" class="image" title="Фотография Земли, сделанная 29 июля 2015 года с борта космического аппарата Deep Space Climate Observatory"><img alt="Фотография Земли, сделанная 29 июля 2015 года с борта космического аппарата Deep Space Climate Observatory" src="//upload.wikimedia.org/wikipedia/commons/thumb/0/0d/Africa_and_Europe_from_a_Million_Miles_Away.png/270px-Africa_and_Europe_from_a_Million_Miles_Away.png" decoding="async" width="270" height="268" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/0/0d/Africa_and_Europe_from_a_Million_Miles_Away.png/405px-Africa_and_Europe_from_a_Million_Miles_Away.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/0/0d/Africa_and_Europe_from_a_Million_Miles_Away.png/540px-Africa_and_Europe_from_a_Million_Miles_Away.png 2x" data-file-width="1780" data-file-height="1768"></a><br><span data-wikidata-qualifier-id="P2096" class="media-caption" style="display:block">Фотография Земли, сделанная 29 июля 2015 года с борта космического аппарата <a href="/wiki/Deep_Space_Climate_Observatory" title="Deep Space Climate Observatory">Deep Space Climate Observatory</a></span></span> </td></tr>
<tr>
<th colspan="2" scope="colgroup" class="infobox-header" style="">Орбитальные характеристики</th>
</tr>
<tr>
<td colspan="2" class="plainlist" style="text-align:center;">
<a href="/wiki/%D0%AD%D0%BF%D0%BE%D1%85%D0%B0_(%D0%B0%D1%81%D1%82%D1%80%D0%BE%D0%BD%D0%BE%D0%BC%D0%B8%D1%8F)" title="Эпоха (астрономия)">Эпоха</a>: J2000.0</td>
</tr>
<tr>
<th scope="row" class="plainlist"><a href="/wiki/%D0%9F%D0%B5%D1%80%D0%B8%D0%B3%D0%B5%D0%BB%D0%B8%D0%B9" title="Перигелий">Перигелий</a></th>
<td class="plainlist">
<span data-wikidata-property-id="P2244" class="no-wikidata">147 098 290 км <br> 0,98329134 <a href="/wiki/%D0%90%D1%81%D1%82%D1%80%D0%BE%D0%BD%D0%BE%D0%BC%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B0%D1%8F_%D0%B5%D0%B4%D0%B8%D0%BD%D0%B8%D1%86%D0%B0" title="Астрономическая единица">а.е.</a><sup id="cite_ref-note_1-0" class="reference"><a href="#cite_note-note-1">[комм. 1]</a></sup></span></td>
</tr>
<tr>
<th scope="row" class="plainlist"><a href="/wiki/%D0%90%D1%84%D0%B5%D0%BB%D0%B8%D0%B9" title="Афелий">Афелий</a></th>
<td class="plainlist">
<span data-wikidata-property-id="P2243" class="no-wikidata">152 098 232 км <br>1,01671388 а.е.<sup id="cite_ref-note_1-1" class="reference"><a href="#cite_note-note-1">[комм. 1]</a></sup></span></td>
</tr>
<tr>
<th scope="row" class="plainlist"><a href="/wiki/%D0%91%D0%BE%D0%BB%D1%8C%D1%88%D0%B0%D1%8F_%D0%BF%D0%BE%D0%BB%D1%83%D0%BE%D1%81%D1%8C" title="Большая полуось">Большая полуось</a>&nbsp;(<style data-mw-deduplicate="TemplateStyles:r117753614">.mw-parser-output .ts-math{white-space:nowrap;font-family:times,serif,palatino linotype,new athena unicode,athena,gentium,code2000;font-size:120%}</style><span class="ts-math"><i>a</i></span>)</th>
<td class="plainlist">
<span data-wikidata-property-id="P2233" class="no-wikidata">149 598 261 км <br> 1,00000261 а.е.<sup id="cite_ref-standish_williams_iau_2-0" class="reference"><a href="#cite_note-standish_williams_iau-2">[1]</a></sup></span></td>
</tr>
<tr>
<th scope="row" class="plainlist"><a href="/wiki/%D0%AD%D0%BA%D1%81%D1%86%D0%B5%D0%BD%D1%82%D1%80%D0%B8%D1%81%D0%B8%D1%82%D0%B5%D1%82_%D0%BE%D1%80%D0%B1%D0%B8%D1%82%D1%8B" title="Эксцентриситет орбиты">Эксцентриситет орбиты</a>&nbsp;(<link rel="mw-deduplicated-inline-style" href="mw-data:TemplateStyles:r117753614"><span class="ts-math"><i>e</i></span>)</th>
<td class="plainlist">
<span data-wikidata-property-id="P1096" class="no-wikidata">0,01671123<sup id="cite_ref-standish_williams_iau_2-1" class="reference"><a href="#cite_note-standish_williams_iau-2">[1]</a></sup><sup id="cite_ref-earthfact_3-0" class="reference"><a href="#cite_note-earthfact-3">[2]</a></sup></span></td>
</tr>
<tr>
<th scope="row" class="plainlist"><a href="/wiki/%D0%A1%D0%B8%D0%B4%D0%B5%D1%80%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B8%D0%B9_%D0%BF%D0%B5%D1%80%D0%B8%D0%BE%D0%B4" title="Сидерический период">Сидерический период</a> обращения</th>
<td class="plainlist">
<span data-wikidata-property-id="P2146" class="no-wikidata">365,256363004 дней <br>365&nbsp;<a href="/wiki/%D0%A1%D1%83%D1%82%D0%BA%D0%B8" title="Сутки">сут</a> 6&nbsp;<a href="/wiki/%D0%A7%D0%B0%D1%81" title="Час">ч</a> 9&nbsp;<a href="/wiki/%D0%9C%D0%B8%D0%BD%D1%83%D1%82%D0%B0" title="Минута">мин</a> 10&nbsp;<a href="/wiki/%D0%A1%D0%B5%D0%BA%D1%83%D0%BD%D0%B4%D0%B0" title="Секунда">с</a><sup id="cite_ref-IERS_4-0" class="reference"><a href="#cite_note-IERS-4">[3]</a></sup></span></td>
</tr>
<tr>
<th scope="row" class="plainlist"><a href="/wiki/%D0%9E%D1%80%D0%B1%D0%B8%D1%82%D0%B0%D0%BB%D1%8C%D0%BD%D0%B0%D1%8F_%D1%81%D0%BA%D0%BE%D1%80%D0%BE%D1%81%D1%82%D1%8C" title="Орбитальная скорость">Орбитальная скорость</a>&nbsp;(<link rel="mw-deduplicated-inline-style" href="mw-data:TemplateStyles:r117753614"><span class="ts-math"><i>v</i></span>)</th>
<td class="plainlist">
29,783 км/c<br>107 218 км/ч<sup id="cite_ref-earthfact_3-1" class="reference"><a href="#cite_note-earthfact-3">[2]</a></sup></td>
</tr>
<tr>
<th scope="row" class="plainlist"><a href="/wiki/%D0%A1%D1%80%D0%B5%D0%B4%D0%BD%D1%8F%D1%8F_%D0%B0%D0%BD%D0%BE%D0%BC%D0%B0%D0%BB%D0%B8%D1%8F" class="mw-redirect" title="Средняя аномалия">Средняя аномалия</a>&nbsp;(<link rel="mw-deduplicated-inline-style" href="mw-data:TemplateStyles:r117753614"><span class="ts-math"><i>M<sub>o</sub></i></span>)</th>
<td class="plainlist">
357,51716°<sup id="cite_ref-earthfact_3-2" class="reference"><a href="#cite_note-earthfact-3">[2]</a></sup></td>
</tr>
<tr>
<th scope="row" class="plainlist"><a href="/wiki/%D0%9A%D0%B5%D0%BF%D0%BB%D0%B5%D1%80%D0%BE%D0%B2%D1%8B_%D1%8D%D0%BB%D0%B5%D0%BC%D0%B5%D0%BD%D1%82%D1%8B_%D0%BE%D1%80%D0%B1%D0%B8%D1%82%D1%8B#Наклонение" title="Кеплеровы элементы орбиты">Наклонение</a>&nbsp;(<link rel="mw-deduplicated-inline-style" href="mw-data:TemplateStyles:r117753614"><span class="ts-math"><i>i</i></span>)</th>
<td class="plainlist">
<span data-wikidata-property-id="P2045" class="no-wikidata">7,155° (отн. солнечного экватора)<sup id="cite_ref-Allen294_5-0" class="reference"><a href="#cite_note-Allen294-5">[4]</a></sup>, 1,57869° (отн. инвариантной плоскости)<sup id="cite_ref-Allen294_5-1" class="reference"><a href="#cite_note-Allen294-5">[4]</a></sup></span></td>
</tr>
<tr>
<th scope="row" class="plainlist"><a href="/wiki/%D0%94%D0%BE%D0%BB%D0%B3%D0%BE%D1%82%D0%B0_%D0%B2%D0%BE%D1%81%D1%85%D0%BE%D0%B4%D1%8F%D1%89%D0%B5%D0%B3%D0%BE_%D1%83%D0%B7%D0%BB%D0%B0" class="mw-redirect" title="Долгота восходящего узла">Долгота восходящего узла</a>&nbsp;(<link rel="mw-deduplicated-inline-style" href="mw-data:TemplateStyles:r117753614"><span class="ts-math">Ω</span>)</th>
<td class="plainlist">
<span data-wikidata-property-id="P2213" class="no-wikidata">348,73936°<sup id="cite_ref-earthfact_3-3" class="reference"><a href="#cite_note-earthfact-3">[2]</a></sup></span></td>
</tr>
<tr>
<th scope="row" class="plainlist"><a href="/wiki/%D0%90%D1%80%D0%B3%D1%83%D0%BC%D0%B5%D0%BD%D1%82_%D0%BF%D0%B5%D1%80%D0%B8%D1%86%D0%B5%D0%BD%D1%82%D1%80%D0%B0" class="mw-redirect" title="Аргумент перицентра">Аргумент перицентра</a>&nbsp;(<link rel="mw-deduplicated-inline-style" href="mw-data:TemplateStyles:r117753614"><span class="ts-math">ω</span>)</th>
<td class="plainlist">
<span data-wikidata-property-id="P2248" class="no-wikidata">114,20783°<sup id="cite_ref-earthfact_3-4" class="reference"><a href="#cite_note-earthfact-3">[2]</a></sup></span></td>
</tr>
<tr>
<th scope="row" class="plainlist">Чей спутник</th>
<td class="plainlist">
<span data-wikidata-claim-id="q2$03594614-958A-45FB-8979-BA175F8F6574" class="wikidata-claim" data-wikidata-property-id="P397"><span class="wikidata-snak wikidata-main-snak"><a href="/wiki/%D0%A1%D0%BE%D0%BB%D0%BD%D1%86%D0%B5" title="Солнце">Солнце</a></span></span></td>
</tr>
<tr>
<th scope="row" class="plainlist">Спутники</th>
<td class="plainlist">
<span data-wikidata-property-id="P398" class="no-wikidata"><a href="/wiki/%D0%9B%D1%83%D0%BD%D0%B0" title="Луна">Луна</a> и более 8300 <a href="/wiki/%D0%98%D1%81%D0%BA%D1%83%D1%81%D1%81%D1%82%D0%B2%D0%B5%D0%BD%D0%BD%D1%8B%D0%B9_%D1%81%D0%BF%D1%83%D1%82%D0%BD%D0%B8%D0%BA_%D0%97%D0%B5%D0%BC%D0%BB%D0%B8" title="Искусственный спутник Земли">искусственных спутников</a><sup id="cite_ref-6" class="reference"><a href="#cite_note-6">[5]</a></sup></span></td>
</tr>
<tr>
<th colspan="2" scope="colgroup" class="infobox-header" style="">Физические характеристики</th>
</tr>
<tr>
<th scope="row" class="plainlist">Полярное сжатие</th>
<td class="plainlist">
<span data-wikidata-property-id="P1102" class="no-wikidata">0,0033528<sup id="cite_ref-earthfact_3-5" class="reference"><a href="#cite_note-earthfact-3">[2]</a></sup></span></td>
</tr>
<tr>
<th scope="row" class="plainlist"><a href="/wiki/%D0%AD%D0%BA%D0%B2%D0%B0%D1%82%D0%BE%D1%80" title="Экватор">Экваториальный</a> радиус</th>
<td class="plainlist">
6378,1 км<sup id="cite_ref-earthfact_3-6" class="reference"><a href="#cite_note-earthfact-3">[2]</a></sup></td>
</tr>
<tr>
<th scope="row" class="plainlist"><a href="/wiki/%D0%93%D0%B5%D0%BE%D0%B3%D1%80%D0%B0%D1%84%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B8%D0%B9_%D0%BF%D0%BE%D0%BB%D1%8E%D1%81" title="Географический полюс">Полярный</a> радиус</th>
<td class="plainlist">
6356,8 км<sup id="cite_ref-earthfact_3-7" class="reference"><a href="#cite_note-earthfact-3">[2]</a></sup></td>
</tr>
<tr>
<th scope="row" class="plainlist">Средний радиус</th>
<td class="plainlist">
6371,0 км<sup id="cite_ref-earthfact_3-8" class="reference"><a href="#cite_note-earthfact-3">[2]</a></sup></td>
</tr>
<tr>
<th scope="row" class="plainlist">Окружность большого круга</th>
<td class="plainlist">
40 075,017 км (<a href="/wiki/%D0%AD%D0%BA%D0%B2%D0%B0%D1%82%D0%BE%D1%80" title="Экватор">по экватору</a>)<br>40 007,863&nbsp;км&nbsp;(<a href="/wiki/%D0%9C%D0%B5%D1%80%D0%B8%D0%B4%D0%B8%D0%B0%D0%BD" title="Меридиан">по меридиану</a>)<sup id="cite_ref-WGS-84-2_7-0" class="reference"><a href="#cite_note-WGS-84-2-7">[6]</a></sup></td>
</tr>
<tr>
<th scope="row" class="plainlist">Площадь поверхности&nbsp;(<link rel="mw-deduplicated-inline-style" href="mw-data:TemplateStyles:r117753614"><span class="ts-math"><i>S</i></span>)</th>
<td class="plainlist">
510 072 000 км²<sup id="cite_ref-Pidwirny_2006_8-0" class="reference"><a href="#cite_note-Pidwirny_2006-8">[7]</a></sup><sup id="cite_ref-CIA_9-0" class="reference"><a href="#cite_note-CIA-9">[8]</a></sup><br>148 940 000 км² суша (29,2&nbsp;%)<sup id="cite_ref-Pidwirny_2006_8-1" class="reference"><a href="#cite_note-Pidwirny_2006-8">[7]</a></sup> <br>361 132 000 км² вода (70,8&nbsp;%)<sup id="cite_ref-Pidwirny_2006_8-2" class="reference"><a href="#cite_note-Pidwirny_2006-8">[7]</a></sup></td>
</tr>
<tr>
<th scope="row" class="plainlist">Объём&nbsp;(<link rel="mw-deduplicated-inline-style" href="mw-data:TemplateStyles:r117753614"><span class="ts-math"><i>V</i></span>)</th>
<td class="plainlist">
1,08321⋅10<sup>12</sup> км³<sup id="cite_ref-earthfact_3-9" class="reference"><a href="#cite_note-earthfact-3">[2]</a></sup></td>
</tr>
<tr>
<th scope="row" class="plainlist">Масса&nbsp;(<link rel="mw-deduplicated-inline-style" href="mw-data:TemplateStyles:r117753614"><span class="ts-math"><i>m</i></span>)</th>
<td class="plainlist">
<span data-wikidata-property-id="P2067" class="no-wikidata">5,9726⋅10<sup>24</sup> кг (3⋅10<sup>-6</sup> M<sub>☉</sub>)<sup id="cite_ref-earthfact_3-10" class="reference"><a href="#cite_note-earthfact-3">[2]</a></sup></span></td>
</tr>
<tr>
<th scope="row" class="plainlist">Средняя <a href="/wiki/%D0%9F%D0%BB%D0%BE%D1%82%D0%BD%D0%BE%D1%81%D1%82%D1%8C" title="Плотность">плотность</a>&nbsp;(<link rel="mw-deduplicated-inline-style" href="mw-data:TemplateStyles:r117753614"><span class="ts-math">ρ</span>)</th>
<td class="plainlist">
5,5153 г/см³<sup id="cite_ref-earthfact_3-11" class="reference"><a href="#cite_note-earthfact-3">[2]</a></sup></td>
</tr>
<tr>
<th scope="row" class="plainlist"><a href="/wiki/%D0%A3%D1%81%D0%BA%D0%BE%D1%80%D0%B5%D0%BD%D0%B8%D0%B5_%D1%81%D0%B2%D0%BE%D0%B1%D0%BE%D0%B4%D0%BD%D0%BE%D0%B3%D0%BE_%D0%BF%D0%B0%D0%B4%D0%B5%D0%BD%D0%B8%D1%8F" title="Ускорение свободного падения">Ускорение свободного падения</a> на экваторе&nbsp;(<link rel="mw-deduplicated-inline-style" href="mw-data:TemplateStyles:r117753614"><span class="ts-math"><i>g</i></span>)</th>
<td class="plainlist">
9,780327 м/с² (0,99732 g)<sup id="cite_ref-earthfact_3-12" class="reference"><a href="#cite_note-earthfact-3">[2]</a></sup></td>
</tr>
<tr>
<th scope="row" class="plainlist"><a href="/wiki/%D0%9F%D0%B5%D1%80%D0%B2%D0%B0%D1%8F_%D0%BA%D0%BE%D1%81%D0%BC%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B0%D1%8F_%D1%81%D0%BA%D0%BE%D1%80%D0%BE%D1%81%D1%82%D1%8C" title="Первая космическая скорость">Первая космическая скорость</a>&nbsp;(<link rel="mw-deduplicated-inline-style" href="mw-data:TemplateStyles:r117753614"><span class="ts-math"><i>v</i></span><sub>1</sub>)</th>
<td class="plainlist">
7,91 км/с<sup id="cite_ref-10" class="reference"><a href="#cite_note-10">[комм. 2]</a></sup></td>
</tr>
<tr>
<th scope="row" class="plainlist"><a href="/wiki/%D0%92%D1%82%D0%BE%D1%80%D0%B0%D1%8F_%D0%BA%D0%BE%D1%81%D0%BC%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B0%D1%8F_%D1%81%D0%BA%D0%BE%D1%80%D0%BE%D1%81%D1%82%D1%8C" title="Вторая космическая скорость">Вторая космическая скорость</a>&nbsp;(<link rel="mw-deduplicated-inline-style" href="mw-data:TemplateStyles:r117753614"><span class="ts-math"><i>v</i></span><sub>2</sub>)</th>
<td class="plainlist">
11,186 км/с<sup id="cite_ref-earthfact_3-13" class="reference"><a href="#cite_note-earthfact-3">[2]</a></sup></td>
</tr>
<tr>
<th scope="row" class="plainlist">Экваториальная скорость вращения</th>
<td class="plainlist">
1674,4 км/ч (465,1 м/с)<sup id="cite_ref-Allen244_11-0" class="reference"><a href="#cite_note-Allen244-11">[9]</a></sup></td>
</tr>
<tr>
<th scope="row" class="plainlist"><a href="/wiki/%D0%9F%D0%B5%D1%80%D0%B8%D0%BE%D0%B4_%D0%B2%D1%80%D0%B0%D1%89%D0%B5%D0%BD%D0%B8%D1%8F" title="Период вращения">Период вращения</a>&nbsp;(<link rel="mw-deduplicated-inline-style" href="mw-data:TemplateStyles:r117753614"><span class="ts-math"><i>T</i></span>)</th>
<td class="plainlist">
0,99726968 суток <br>(23<sup><small>h</small></sup>&nbsp;56<sup><small>m</small></sup>&nbsp;4,100<sup><small>s</small></sup>) — сидерический период вращения<sup id="cite_ref-Allen296_12-0" class="reference"><a href="#cite_note-Allen296-12">[10]</a></sup>,<br>24 часа  — длительность средних <a href="/wiki/%D0%A1%D0%BE%D0%BB%D0%BD%D0%B5%D1%87%D0%BD%D1%8B%D0%B5_%D1%81%D1%83%D1%82%D0%BA%D0%B8" title="Солнечные сутки">солнечных суток</a></td>
</tr>
<tr>
<th scope="row" class="plainlist"><a href="/wiki/%D0%9D%D0%B0%D0%BA%D0%BB%D0%BE%D0%BD_%D0%BE%D1%81%D0%B8_%D0%B2%D1%80%D0%B0%D1%89%D0%B5%D0%BD%D0%B8%D1%8F" title="Наклон оси вращения">Наклон оси</a></th>
<td class="plainlist">
23°26ʹ21ʺ,4119<sup id="cite_ref-IERS_4-1" class="reference"><a href="#cite_note-IERS-4">[3]</a></sup></td>
</tr>
<tr>
<th scope="row" class="plainlist"><a href="/wiki/%D0%90%D0%BB%D1%8C%D0%B1%D0%B5%D0%B4%D0%BE" title="Альбедо">Альбедо</a></th>
<td class="plainlist">
0,306 (Бонд)<sup id="cite_ref-earthfact_3-14" class="reference"><a href="#cite_note-earthfact-3">[2]</a></sup><br>0,434 (геометрическое)<sup id="cite_ref-earthfact_3-15" class="reference"><a href="#cite_note-earthfact-3">[2]</a></sup></td>
</tr>
<tr>
<th colspan="2" scope="colgroup" class="infobox-header" style="">Температура</th>
</tr>
<tr>
<th scope="row" class="plainlist">&nbsp;</th>
<td class="plainlist">
<table><tbody><tr style="font-weight:bold">
<td>мин.</td>
<td>сред.</td>
<td>макс.</td>
</tr></tbody></table></td>
</tr>
<tr>
<th scope="row" class="plainlist"><a href="/wiki/%D0%93%D1%80%D0%B0%D0%B4%D1%83%D1%81_%D0%A6%D0%B5%D0%BB%D1%8C%D1%81%D0%B8%D1%8F" title="Градус Цельсия">Цельсий</a></th>
<td class="plainlist">
<table><tbody><tr>
<td>−89,2&nbsp;°C<sup id="cite_ref-13" class="reference"><a href="#cite_note-13">[11]</a></sup></td>
<td>14&nbsp;°C<sup id="cite_ref-kinver20091210_14-0" class="reference"><a href="#cite_note-kinver20091210-14">[12]</a></sup></td>
<td>56,7&nbsp;°C<sup id="cite_ref-asu_highest_temp_15-0" class="reference"><a href="#cite_note-asu_highest_temp-15">[13]</a></sup><sup id="cite_ref-16" class="reference"><a href="#cite_note-16">[14]</a></sup></td>
</tr></tbody></table></td>
</tr>
<tr>
<th scope="row" class="plainlist"><a href="/wiki/%D0%9A%D0%B5%D0%BB%D1%8C%D0%B2%D0%B8%D0%BD" title="Кельвин">Кельвин</a></th>
<td class="plainlist">
<table><tbody><tr>
<td>184&nbsp;K</td>
<td>287,2&nbsp;К</td>
<td>329,9&nbsp;К</td>
</tr></tbody></table></td>
</tr>
<tr>
<th colspan="2" scope="colgroup" class="infobox-header" style=""><a href="/wiki/%D0%90%D1%82%D0%BC%D0%BE%D1%81%D1%84%D0%B5%D1%80%D0%B0" title="Атмосфера">Атмосфера</a><sup id="cite_ref-earthfact_3-16" class="reference"><a href="#cite_note-earthfact-3">[2]</a></sup></th>
</tr>
<tr>
<td colspan="2" class="plainlist" style="text-align:center;">
<div style="text-align:left"><b>Состав:</b> <div style="margin-left:1em">78,08&nbsp;%&nbsp;— <a href="/wiki/%D0%90%D0%B7%D0%BE%D1%82" title="Азот">азот</a> (N<sub>2</sub>)<br> 20,95&nbsp;%&nbsp;— <a href="/wiki/%D0%9A%D0%B8%D1%81%D0%BB%D0%BE%D1%80%D0%BE%D0%B4" title="Кислород">кислород</a> (O<sub>2</sub>)<br> 0,93&nbsp;%&nbsp;— <a href="/wiki/%D0%90%D1%80%D0%B3%D0%BE%D0%BD" title="Аргон">аргон</a> (Ar)<br> 0,04&nbsp;%&nbsp;— <a href="/wiki/%D0%9E%D0%BA%D1%81%D0%B8%D0%B4_%D1%83%D0%B3%D0%BB%D0%B5%D1%80%D0%BE%D0%B4%D0%B0(IV)" class="mw-redirect" title="Оксид углерода(IV)">углекислый газ</a> (СO<sub>2</sub>)<sup id="cite_ref-esrl_17-0" class="reference"><a href="#cite_note-esrl-17">[15]</a></sup><br>Около 1&nbsp;% <a href="/wiki/%D0%92%D0%BE%D0%B4%D1%8F%D0%BD%D0%BE%D0%B9_%D0%BF%D0%B0%D1%80" title="Водяной пар">водяного пара</a> (в зависимости от климата)</div></div></td>
</tr><tr><td colspan="2" class="infobox-below" style=";"><span data-wikidata-claim-id="q2$92E1BBEA-5747-4AE0-B478-F2EA89E26537" class="wikidata-claim" data-wikidata-property-id="P373"><span class="wikidata-snak wikidata-main-snak"><a href="https://commons.wikimedia.org/wiki/Category:Earth" title="commons:Category:Earth"><img alt="Логотип Викисклада" src="//upload.wikimedia.org/wikipedia/commons/thumb/4/4a/Commons-logo.svg/15px-Commons-logo.svg.png" decoding="async" width="15" height="20" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/4/4a/Commons-logo.svg/23px-Commons-logo.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/4/4a/Commons-logo.svg/30px-Commons-logo.svg.png 2x" data-file-width="1024" data-file-height="1376"></a>&nbsp;<a href="https://commons.wikimedia.org/wiki/Category:Earth" class="extiw" title="commons:Category:Earth">Медиафайлы на Викискладе</a></span></span></td></tr><tr><td colspan="2" class="infobox-below" style=";"><a href="https://www.wikidata.org/wiki/Special:ItemByTitle/ruwiki/%D0%97%D0%B5%D0%BC%D0%BB%D1%8F" title="d:Special:ItemByTitle/ruwiki/Земля"><img alt="Логотип Викиданных" src="//upload.wikimedia.org/wikipedia/commons/thumb/e/e4/Wikidata-logo_S.svg/18px-Wikidata-logo_S.svg.png" decoding="async" width="18" height="10" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/e/e4/Wikidata-logo_S.svg/27px-Wikidata-logo_S.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/e/e4/Wikidata-logo_S.svg/36px-Wikidata-logo_S.svg.png 2x" data-file-width="1050" data-file-height="590"></a> <a href="https://www.wikidata.org/wiki/d:Special:ItemByTitle/ruwiki/%D0%97%D0%B5%D0%BC%D0%BB%D1%8F" class="extiw" title="d:d:Special:ItemByTitle/ruwiki/Земля">Информация в Викиданных</a>&nbsp;<sup><style data-mw-deduplicate="TemplateStyles:r113275842">.mw-parser-output .ts-comment-commentedText{border-bottom:1px dotted;cursor:help}@media(hover:none){.mw-parser-output .ts-comment-commentedText:not(.rt-commentedText){border-bottom:0;cursor:auto}}</style><span class="ts-comment-commentedText" title="Элементы карточки, которых нет в окне редактирования статьи, редактируются в Викиданных">?</span></sup></td></tr>
</tbody></table>
</div>
    <div class="col">
        <div class="alert alert-info">Эта планета, на которой мы живём</div>
    </div>
</body>
</html>
"""
    if planet_name == "Марс":
        return """
        <!doctype html>
        <html>
        <head>
            <meta charset="utf-8">
            <meta name="viewport" content="width=device-width, initial-scale=1">
            <title>Марс</title>
            <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha2/dist/css/bootstrap.min.css" rel="stylesheet"
            integrity="sha384-aFq/bzH65dt+w6FI2ooMVUpc+21e0SRygnTpmBvdBgSdnuTN7QbdgL+OapgHtvPp" crossorigin="anonymous">
            <link rel="stylesheet" type="text/css" href="../static/css/style.css"/>
        </head>
        <body>
            <div class="table">
            <div class="row">
            <div class="col">
            <table class="infobox infobox-0732d68adfb30775" style="width:27em;" data-name="Планета"><tbody><tr><th colspan="2" scope="colgroup" class="infobox-above" style="">Марс <span data-wikidata-property-id="P367" class="no-wikidata"><a href="//commons.wikimedia.org/wiki/File:Mars_symbol_(bold).svg?uselang=ru" class="image"><img alt="Mars symbol (bold).svg" src="//upload.wikimedia.org/wikipedia/commons/thumb/8/8c/Mars_symbol_%28bold%29.svg/20px-Mars_symbol_%28bold%29.svg.png" decoding="async" width="20" height="20" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/8/8c/Mars_symbol_%28bold%29.svg/30px-Mars_symbol_%28bold%29.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/8/8c/Mars_symbol_%28bold%29.svg/40px-Mars_symbol_%28bold%29.svg.png 2x" data-file-width="15" data-file-height="15"></a></span></th></tr><tr><td colspan="2" class="" style="text-align:center;"><a href="/wiki/%D0%9F%D0%BB%D0%B0%D0%BD%D0%B5%D1%82%D0%B0" title="Планета">Планета</a></td></tr><tr><td colspan="2" class="infobox-image" style=""> <span data-wikidata-property-id="P18" class="no-wikidata"><a href="//commons.wikimedia.org/wiki/File:Mars_Valles_Marineris_EDIT.jpg?uselang=ru" class="image" title="Изображение Марса на основе 102&nbsp;снимков, полученных АМС «Викинг-1» 22 февраля 1980 года"><img alt="Изображение Марса на основе 102&nbsp;снимков, полученных АМС «Викинг-1» 22 февраля 1980 года" src="//upload.wikimedia.org/wikipedia/commons/thumb/3/36/Mars_Valles_Marineris_EDIT.jpg/274px-Mars_Valles_Marineris_EDIT.jpg" decoding="async" width="274" height="274" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/3/36/Mars_Valles_Marineris_EDIT.jpg/411px-Mars_Valles_Marineris_EDIT.jpg 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/3/36/Mars_Valles_Marineris_EDIT.jpg/548px-Mars_Valles_Marineris_EDIT.jpg 2x" data-file-width="1716" data-file-height="1716"></a><br><span data-wikidata-qualifier-id="P2096" class="media-caption" style="display:block">Изображение Марса на основе <span class="nowrap">102&nbsp;снимков</span>, полученных <a href="/wiki/%D0%90%D0%B2%D1%82%D0%BE%D0%BC%D0%B0%D1%82%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B0%D1%8F_%D0%BC%D0%B5%D0%B6%D0%BF%D0%BB%D0%B0%D0%BD%D0%B5%D1%82%D0%BD%D0%B0%D1%8F_%D1%81%D1%82%D0%B0%D0%BD%D1%86%D0%B8%D1%8F" title="Автоматическая межпланетная станция">АМС</a> «<a href="/wiki/%D0%92%D0%B8%D0%BA%D0%B8%D0%BD%D0%B3-1" title="Викинг-1">Викинг-1</a>» 22 февраля 1980 года</span></span> </td></tr>
<tr>
<th scope="row" class="plainlist">Другие названия</th>
<td class="plainlist">
Красная планета</td>
</tr>
<tr>
<th colspan="2" scope="colgroup" class="infobox-header" style="">Орбитальные характеристики</th>
</tr>
<tr>
<th scope="row" class="plainlist"><a href="/wiki/%D0%9F%D0%B5%D1%80%D0%B8%D0%B3%D0%B5%D0%BB%D0%B8%D0%B9" title="Перигелий">Перигелий</a></th>
<td class="plainlist">
<span data-wikidata-property-id="P2244" class="no-wikidata">2,06655⋅10<sup>8</sup> км<sup id="cite_ref-factsNasa_1-0" class="reference"><a href="#cite_note-factsNasa-1">[1]</a></sup><sup id="cite_ref-nssdc_2-0" class="reference"><a href="#cite_note-nssdc-2">[2]</a></sup><br>1,381 <a href="/wiki/%D0%90%D1%81%D1%82%D1%80%D0%BE%D0%BD%D0%BE%D0%BC%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B0%D1%8F_%D0%B5%D0%B4%D0%B8%D0%BD%D0%B8%D1%86%D0%B0" title="Астрономическая единица">а.e.</a><sup id="cite_ref-factsNasa_1-1" class="reference"><a href="#cite_note-factsNasa-1">[1]</a></sup></span></td>
</tr>
<tr>
<th scope="row" class="plainlist"><a href="/wiki/%D0%90%D1%84%D0%B5%D0%BB%D0%B8%D0%B9" title="Афелий">Афелий</a></th>
<td class="plainlist">
<span data-wikidata-property-id="P2243" class="no-wikidata">2,49232⋅10<sup>8</sup> км<sup id="cite_ref-factsNasa_1-2" class="reference"><a href="#cite_note-factsNasa-1">[1]</a></sup><sup id="cite_ref-nssdc_2-1" class="reference"><a href="#cite_note-nssdc-2">[2]</a></sup><br>1,666 <a href="/wiki/%D0%90%D1%81%D1%82%D1%80%D0%BE%D0%BD%D0%BE%D0%BC%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B0%D1%8F_%D0%B5%D0%B4%D0%B8%D0%BD%D0%B8%D1%86%D0%B0" title="Астрономическая единица">а.e.</a><sup id="cite_ref-factsNasa_1-3" class="reference"><a href="#cite_note-factsNasa-1">[1]</a></sup></span></td>
</tr>
<tr>
<th scope="row" class="plainlist"><a href="/wiki/%D0%91%D0%BE%D0%BB%D1%8C%D1%88%D0%B0%D1%8F_%D0%BF%D0%BE%D0%BB%D1%83%D0%BE%D1%81%D1%8C" title="Большая полуось">Большая полуось</a>&nbsp;(<style data-mw-deduplicate="TemplateStyles:r117753614">.mw-parser-output .ts-math{white-space:nowrap;font-family:times,serif,palatino linotype,new athena unicode,athena,gentium,code2000;font-size:120%}</style><span class="ts-math"><i>a</i></span>)</th>
<td class="plainlist">
<span data-wikidata-property-id="P2233" class="no-wikidata">2,2794382⋅10<sup>8</sup> км<sup id="cite_ref-factsNasa_1-4" class="reference"><a href="#cite_note-factsNasa-1">[1]</a></sup><sup id="cite_ref-nssdc_2-2" class="reference"><a href="#cite_note-nssdc-2">[2]</a></sup><br>1,523662 <a href="/wiki/%D0%90%D1%81%D1%82%D1%80%D0%BE%D0%BD%D0%BE%D0%BC%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B0%D1%8F_%D0%B5%D0%B4%D0%B8%D0%BD%D0%B8%D1%86%D0%B0" title="Астрономическая единица">а.e.</a><sup id="cite_ref-factsNasa_1-5" class="reference"><a href="#cite_note-factsNasa-1">[1]</a></sup><br>1,524 земной<sup id="cite_ref-factsNasa_1-6" class="reference"><a href="#cite_note-factsNasa-1">[1]</a></sup></span></td>
</tr>
<tr>
<th scope="row" class="plainlist"><a href="/wiki/%D0%AD%D0%BA%D1%81%D1%86%D0%B5%D0%BD%D1%82%D1%80%D0%B8%D1%81%D0%B8%D1%82%D0%B5%D1%82_%D0%BE%D1%80%D0%B1%D0%B8%D1%82%D1%8B" title="Эксцентриситет орбиты">Эксцентриситет орбиты</a>&nbsp;(<link rel="mw-deduplicated-inline-style" href="mw-data:TemplateStyles:r117753614"><span class="ts-math"><i>e</i></span>)</th>
<td class="plainlist">
<span data-wikidata-property-id="P1096" class="no-wikidata">0,0933941<sup id="cite_ref-factsNasa_1-7" class="reference"><a href="#cite_note-factsNasa-1">[1]</a></sup><sup id="cite_ref-nssdc_2-3" class="reference"><a href="#cite_note-nssdc-2">[2]</a></sup></span></td>
</tr>
<tr>
<th scope="row" class="plainlist"><a href="/wiki/%D0%A1%D0%B8%D0%B4%D0%B5%D1%80%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B8%D0%B9_%D0%BF%D0%B5%D1%80%D0%B8%D0%BE%D0%B4" title="Сидерический период">Сидерический период</a> обращения</th>
<td class="plainlist">
<span data-wikidata-property-id="P2146" class="no-wikidata">(продолжительность года)<br>686,98 земных суток<br>1,8808476 земного года<sup id="cite_ref-factsNasa_1-8" class="reference"><a href="#cite_note-factsNasa-1">[1]</a></sup><sup id="cite_ref-nssdc_2-4" class="reference"><a href="#cite_note-nssdc-2">[2]</a></sup></span></td>
</tr>
<tr>
<th scope="row" class="plainlist"><a href="/wiki/%D0%A1%D0%B8%D0%BD%D0%BE%D0%B4%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B8%D0%B9_%D0%BF%D0%B5%D1%80%D0%B8%D0%BE%D0%B4" title="Синодический период">Синодический период</a> обращения</th>
<td class="plainlist">
<span data-wikidata-property-id="P4341" class="no-wikidata">779,94 земных суток<sup id="cite_ref-nssdc_2-5" class="reference"><a href="#cite_note-nssdc-2">[2]</a></sup></span></td>
</tr>
<tr>
<th scope="row" class="plainlist"><a href="/wiki/%D0%9E%D1%80%D0%B1%D0%B8%D1%82%D0%B0%D0%BB%D1%8C%D0%BD%D0%B0%D1%8F_%D1%81%D0%BA%D0%BE%D1%80%D0%BE%D1%81%D1%82%D1%8C" title="Орбитальная скорость">Орбитальная скорость</a>&nbsp;(<link rel="mw-deduplicated-inline-style" href="mw-data:TemplateStyles:r117753614"><span class="ts-math"><i>v</i></span>)</th>
<td class="plainlist">
24,13 км/с (средн.)<sup id="cite_ref-nssdc_2-6" class="reference"><a href="#cite_note-nssdc-2">[2]</a></sup><br>24,077 км/с<sup id="cite_ref-factsNasa_1-9" class="reference"><a href="#cite_note-factsNasa-1">[1]</a></sup></td>
</tr>
<tr>
<th scope="row" class="plainlist"><a href="/wiki/%D0%9A%D0%B5%D0%BF%D0%BB%D0%B5%D1%80%D0%BE%D0%B2%D1%8B_%D1%8D%D0%BB%D0%B5%D0%BC%D0%B5%D0%BD%D1%82%D1%8B_%D0%BE%D1%80%D0%B1%D0%B8%D1%82%D1%8B#Наклонение" title="Кеплеровы элементы орбиты">Наклонение</a>&nbsp;(<link rel="mw-deduplicated-inline-style" href="mw-data:TemplateStyles:r117753614"><span class="ts-math"><i>i</i></span>)</th>
<td class="plainlist">
<div data-wikidata-property-id="P2045" class="no-wikidata">
<p>1,85061° (относительно плоскости эклиптики)<sup id="cite_ref-nssdc_2-7" class="reference"><a href="#cite_note-nssdc-2">[2]</a></sup><br>
</p>
5,65° (относительно солнечного экватора)</div></td>
</tr>
<tr>
<th scope="row" class="plainlist"><a href="/wiki/%D0%94%D0%BE%D0%BB%D0%B3%D0%BE%D1%82%D0%B0_%D0%B2%D0%BE%D1%81%D1%85%D0%BE%D0%B4%D1%8F%D1%89%D0%B5%D0%B3%D0%BE_%D1%83%D0%B7%D0%BB%D0%B0" class="mw-redirect" title="Долгота восходящего узла">Долгота восходящего узла</a>&nbsp;(<link rel="mw-deduplicated-inline-style" href="mw-data:TemplateStyles:r117753614"><span class="ts-math">Ω</span>)</th>
<td class="plainlist">
<span data-wikidata-property-id="P2213" class="no-wikidata">49,57854°</span></td>
</tr>
<tr>
<th scope="row" class="plainlist"><a href="/wiki/%D0%90%D1%80%D0%B3%D1%83%D0%BC%D0%B5%D0%BD%D1%82_%D0%BF%D0%B5%D1%80%D0%B8%D1%86%D0%B5%D0%BD%D1%82%D1%80%D0%B0" class="mw-redirect" title="Аргумент перицентра">Аргумент перицентра</a>&nbsp;(<link rel="mw-deduplicated-inline-style" href="mw-data:TemplateStyles:r117753614"><span class="ts-math">ω</span>)</th>
<td class="plainlist">
<span data-wikidata-property-id="P2248" class="no-wikidata">286,46230°</span></td>
</tr>
<tr>
<th scope="row" class="plainlist">Чей спутник</th>
<td class="plainlist">
<span data-wikidata-property-id="P397" class="no-wikidata"><a href="/wiki/%D0%A1%D0%BE%D0%BB%D0%BD%D1%86%D0%B5" title="Солнце">Солнца</a></span></td>
</tr>
<tr>
<th scope="row" class="plainlist">Спутники</th>
<td class="plainlist">
<span data-wikidata-property-id="P398" class="no-wikidata"><a href="/wiki/%D0%A1%D0%BF%D1%83%D1%82%D0%BD%D0%B8%D0%BA%D0%B8_%D0%9C%D0%B0%D1%80%D1%81%D0%B0" title="Спутники Марса">2</a></span></td>
</tr>
<tr>
<th colspan="2" scope="colgroup" class="infobox-header" style="">Физические характеристики</th>
</tr>
<tr>
<th scope="row" class="plainlist">Полярное сжатие</th>
<td class="plainlist">
<span data-wikidata-property-id="P1102" class="no-wikidata">0,00589 (1,76 земного)</span></td>
</tr>
<tr>
<th scope="row" class="plainlist"><a href="/wiki/%D0%AD%D0%BA%D0%B2%D0%B0%D1%82%D0%BE%D1%80" title="Экватор">Экваториальный</a> радиус</th>
<td class="plainlist">
3396,2 ± 0,1 км<sup id="cite_ref-sei07_3-0" class="reference"><a href="#cite_note-sei07-3">[3]</a></sup><sup id="cite_ref-bfe_4-0" class="reference"><a href="#cite_note-bfe-4">[4]</a></sup><br>0,532 земного</td>
</tr>
<tr>
<th scope="row" class="plainlist"><a href="/wiki/%D0%93%D0%B5%D0%BE%D0%B3%D1%80%D0%B0%D1%84%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B8%D0%B9_%D0%BF%D0%BE%D0%BB%D1%8E%D1%81" title="Географический полюс">Полярный</a> радиус</th>
<td class="plainlist">
3376,2 ± 0,1 км<sup id="cite_ref-sei07_3-1" class="reference"><a href="#cite_note-sei07-3">[3]</a></sup><sup id="cite_ref-bfe_4-1" class="reference"><a href="#cite_note-bfe-4">[4]</a></sup><br>0,531 земного</td>
</tr>
<tr>
<th scope="row" class="plainlist">Средний радиус</th>
<td class="plainlist">
3389,5 ± 0,2 км<sup id="cite_ref-factsNasa_1-10" class="reference"><a href="#cite_note-factsNasa-1">[1]</a></sup><sup id="cite_ref-nssdc_2-8" class="reference"><a href="#cite_note-nssdc-2">[2]</a></sup><sup id="cite_ref-sei07_3-2" class="reference"><a href="#cite_note-sei07-3">[3]</a></sup><br>0,532 земного</td>
</tr>
<tr>
<th scope="row" class="plainlist">Площадь поверхности&nbsp;(<link rel="mw-deduplicated-inline-style" href="mw-data:TemplateStyles:r117753614"><span class="ts-math"><i>S</i></span>)</th>
<td class="plainlist">
1,4437⋅10<sup>8</sup> км²<sup id="cite_ref-factsNasa_1-11" class="reference"><a href="#cite_note-factsNasa-1">[1]</a></sup><br>0,283 земной</td>
</tr>
<tr>
<th scope="row" class="plainlist">Объём&nbsp;(<link rel="mw-deduplicated-inline-style" href="mw-data:TemplateStyles:r117753614"><span class="ts-math"><i>V</i></span>)</th>
<td class="plainlist">
1,6318⋅10<sup>11</sup> км³<sup id="cite_ref-factsNasa_1-12" class="reference"><a href="#cite_note-factsNasa-1">[1]</a></sup><sup id="cite_ref-nssdc_2-9" class="reference"><a href="#cite_note-nssdc-2">[2]</a></sup><br>0,151 земного</td>
</tr>
<tr>
<th scope="row" class="plainlist">Масса&nbsp;(<link rel="mw-deduplicated-inline-style" href="mw-data:TemplateStyles:r117753614"><span class="ts-math"><i>m</i></span>)</th>
<td class="plainlist">
<span data-wikidata-property-id="P2067" class="no-wikidata">6,4171⋅10<sup>23</sup> кг<sup id="cite_ref-kon11_5-0" class="reference"><a href="#cite_note-kon11-5">[5]</a></sup><br>0,107 земной</span></td>
</tr>
<tr>
<th scope="row" class="plainlist">Средняя <a href="/wiki/%D0%9F%D0%BB%D0%BE%D1%82%D0%BD%D0%BE%D1%81%D1%82%D1%8C" title="Плотность">плотность</a>&nbsp;(<link rel="mw-deduplicated-inline-style" href="mw-data:TemplateStyles:r117753614"><span class="ts-math">ρ</span>)</th>
<td class="plainlist">
3,933 г/см³<sup id="cite_ref-factsNasa_1-13" class="reference"><a href="#cite_note-factsNasa-1">[1]</a></sup><sup id="cite_ref-nssdc_2-10" class="reference"><a href="#cite_note-nssdc-2">[2]</a></sup><br>0,714 земной</td>
</tr>
<tr>
<th scope="row" class="plainlist"><a href="/wiki/%D0%A3%D1%81%D0%BA%D0%BE%D1%80%D0%B5%D0%BD%D0%B8%D0%B5_%D1%81%D0%B2%D0%BE%D0%B1%D0%BE%D0%B4%D0%BD%D0%BE%D0%B3%D0%BE_%D0%BF%D0%B0%D0%B4%D0%B5%D0%BD%D0%B8%D1%8F" title="Ускорение свободного падения">Ускорение свободного падения</a> на экваторе&nbsp;(<link rel="mw-deduplicated-inline-style" href="mw-data:TemplateStyles:r117753614"><span class="ts-math"><i>g</i></span>)</th>
<td class="plainlist">
3,711 м/с²<br>0,378 <link rel="mw-deduplicated-inline-style" href="mw-data:TemplateStyles:r117753614"><span class="ts-math"><i>g</i></span><sup id="cite_ref-factsNasa_1-14" class="reference"><a href="#cite_note-factsNasa-1">[1]</a></sup></td>
</tr>
<tr>
<th scope="row" class="plainlist"><a href="/wiki/%D0%9F%D0%B5%D1%80%D0%B2%D0%B0%D1%8F_%D0%BA%D0%BE%D1%81%D0%BC%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B0%D1%8F_%D1%81%D0%BA%D0%BE%D1%80%D0%BE%D1%81%D1%82%D1%8C" title="Первая космическая скорость">Первая космическая скорость</a>&nbsp;(<link rel="mw-deduplicated-inline-style" href="mw-data:TemplateStyles:r117753614"><span class="ts-math"><i>v</i></span><sub>1</sub>)</th>
<td class="plainlist">
3,55 км/с<br>0,45 земной</td>
</tr>
<tr>
<th scope="row" class="plainlist"><a href="/wiki/%D0%92%D1%82%D0%BE%D1%80%D0%B0%D1%8F_%D0%BA%D0%BE%D1%81%D0%BC%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B0%D1%8F_%D1%81%D0%BA%D0%BE%D1%80%D0%BE%D1%81%D1%82%D1%8C" title="Вторая космическая скорость">Вторая космическая скорость</a>&nbsp;(<link rel="mw-deduplicated-inline-style" href="mw-data:TemplateStyles:r117753614"><span class="ts-math"><i>v</i></span><sub>2</sub>)</th>
<td class="plainlist">
5,03 км/с<br>0,45 земной<sup id="cite_ref-factsNasa_1-15" class="reference"><a href="#cite_note-factsNasa-1">[1]</a></sup><sup id="cite_ref-nssdc_2-11" class="reference"><a href="#cite_note-nssdc-2">[2]</a></sup></td>
</tr>
<tr>
<th scope="row" class="plainlist">Экваториальная скорость вращения</th>
<td class="plainlist">
868,22 км/ч</td>
</tr>
<tr>
<th scope="row" class="plainlist"><a href="/wiki/%D0%9F%D0%B5%D1%80%D0%B8%D0%BE%D0%B4_%D0%B2%D1%80%D0%B0%D1%89%D0%B5%D0%BD%D0%B8%D1%8F" title="Период вращения">Период вращения</a>&nbsp;(<link rel="mw-deduplicated-inline-style" href="mw-data:TemplateStyles:r117753614"><span class="ts-math"><i>T</i></span>)</th>
<td class="plainlist">
24 часа 37 минут 22,663 секунды<sup id="cite_ref-factsNasa_1-16" class="reference"><a href="#cite_note-factsNasa-1">[1]</a></sup> (<span class="nowrap">24,6229 ч</span>)&nbsp;— сидерический период вращения,<br>24 часа 39 минут 35,244 секунды (<span class="nowrap">24,6597 ч</span>)&nbsp;— длительность средних солнечных суток<sup id="cite_ref-Allison_6-0" class="reference"><a href="#cite_note-Allison-6">[6]</a></sup>.</td>
</tr>
<tr>
<th scope="row" class="plainlist"><a href="/wiki/%D0%9D%D0%B0%D0%BA%D0%BB%D0%BE%D0%BD_%D0%BE%D1%81%D0%B8_%D0%B2%D1%80%D0%B0%D1%89%D0%B5%D0%BD%D0%B8%D1%8F" title="Наклон оси вращения">Наклон оси</a></th>
<td class="plainlist">
25,1919°<sup id="cite_ref-Allison_6-1" class="reference"><a href="#cite_note-Allison-6">[6]</a></sup></td>
</tr>
<tr>
<th scope="row" class="plainlist"><a href="/wiki/%D0%9F%D1%80%D1%8F%D0%BC%D0%BE%D0%B5_%D0%B2%D0%BE%D1%81%D1%85%D0%BE%D0%B6%D0%B4%D0%B5%D0%BD%D0%B8%D0%B5" title="Прямое восхождение">Прямое восхождение</a> северного полюса&nbsp;(<link rel="mw-deduplicated-inline-style" href="mw-data:TemplateStyles:r117753614"><span class="ts-math">α</span>)</th>
<td class="plainlist">
317,681°<sup id="cite_ref-nssdc_2-12" class="reference"><a href="#cite_note-nssdc-2">[2]</a></sup></td>
</tr>
<tr>
<th scope="row" class="plainlist"><a href="/wiki/%D0%A1%D0%BA%D0%BB%D0%BE%D0%BD%D0%B5%D0%BD%D0%B8%D0%B5_(%D0%B0%D1%81%D1%82%D1%80%D0%BE%D0%BD%D0%BE%D0%BC%D0%B8%D1%8F)" title="Склонение (астрономия)">Склонение</a> северного полюса&nbsp;(<link rel="mw-deduplicated-inline-style" href="mw-data:TemplateStyles:r117753614"><span class="ts-math">δ</span>)</th>
<td class="plainlist">
52,887°<sup id="cite_ref-nssdc_2-13" class="reference"><a href="#cite_note-nssdc-2">[2]</a></sup></td>
</tr>
<tr>
<th scope="row" class="plainlist"><a href="/wiki/%D0%90%D0%BB%D1%8C%D0%B1%D0%B5%D0%B4%D0%BE" title="Альбедо">Альбедо</a></th>
<td class="plainlist">
0,250 (<a href="/wiki/%D0%90%D0%BB%D1%8C%D0%B1%D0%B5%D0%B4%D0%BE_%D0%91%D0%BE%D0%BD%D0%B4%D0%B0" class="mw-redirect" title="Альбедо Бонда">Бонд</a>)<sup id="cite_ref-nssdc_2-14" class="reference"><a href="#cite_note-nssdc-2">[2]</a></sup><br>0,150 (<a href="/wiki/%D0%93%D0%B5%D0%BE%D0%BC%D0%B5%D1%82%D1%80%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%BE%D0%B5_%D0%B0%D0%BB%D1%8C%D0%B1%D0%B5%D0%B4%D0%BE" class="mw-redirect" title="Геометрическое альбедо">геом. альбедо</a>)<br>0,170<sup id="cite_ref-nssdc_2-15" class="reference"><a href="#cite_note-nssdc-2">[2]</a></sup></td>
</tr>
<tr>
<th scope="row" class="plainlist"><a href="/wiki/%D0%92%D0%B8%D0%B4%D0%B8%D0%BC%D0%B0%D1%8F_%D0%B7%D0%B2%D1%91%D0%B7%D0%B4%D0%BD%D0%B0%D1%8F_%D0%B2%D0%B5%D0%BB%D0%B8%D1%87%D0%B8%D0%BD%D0%B0" title="Видимая звёздная величина">Видимая звёздная величина</a></th>
<td class="plainlist">
<span data-wikidata-claim-id="Q111$A314E67F-62A1-43CE-B7AE-8DC67B547D76" class="wikidata-claim" data-wikidata-property-id="P1215"><span class="wikidata-snak wikidata-main-snak">−2,94</span></span></td>
</tr>
<tr>
<th colspan="2" scope="colgroup" class="infobox-header" style="">Температура</th>
</tr>
<tr>
<th scope="row" class="plainlist">На поверхности</th>
<td class="plainlist">
от −153&nbsp;°C до +35&nbsp;°C<sup id="cite_ref-7" class="reference"><a href="#cite_note-7">[7]</a></sup></td>
</tr>
<tr>
<th scope="row" class="plainlist">&nbsp;</th>
<td class="plainlist">
<table><tbody><tr style="font-weight:bold">
<td>мин.</td>
<td>сред.</td>
<td>макс.</td>
</tr></tbody></table></td>
</tr>
<tr>
<th scope="row" class="plainlist">по всей планете</th>
<td class="plainlist">
<table><tbody><tr>
<td>186 <a href="/wiki/%D0%9A%D0%B5%D0%BB%D1%8C%D0%B2%D0%B8%D0%BD" title="Кельвин">К</a>;<br>−87&nbsp;°C<sup id="cite_ref-factsNasa_1-17" class="reference"><a href="#cite_note-factsNasa-1">[1]</a></sup></td>
<td>210 K<br>(−63&nbsp;°C)<sup id="cite_ref-nssdc_2-16" class="reference"><a href="#cite_note-nssdc-2">[2]</a></sup></td>
<td>268 К;<br>−5&nbsp;°C<sup id="cite_ref-factsNasa_1-18" class="reference"><a href="#cite_note-factsNasa-1">[1]</a></sup></td>
</tr></tbody></table></td>
</tr>
<tr>
<th colspan="2" scope="colgroup" class="infobox-header" style=""><a href="/wiki/%D0%90%D1%82%D0%BC%D0%BE%D1%81%D1%84%D0%B5%D1%80%D0%B0" title="Атмосфера">Атмосфера</a><sup id="cite_ref-nssdc_2-17" class="reference"><a href="#cite_note-nssdc-2">[2]</a></sup></th>
</tr>
<tr>
<th scope="row" class="plainlist"><a href="/wiki/%D0%90%D1%82%D0%BC%D0%BE%D1%81%D1%84%D0%B5%D1%80%D0%BD%D0%BE%D0%B5_%D0%B4%D0%B0%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5" title="Атмосферное давление">Атмосферное давление</a></th>
<td class="plainlist">
0,4—0,87 к<a href="/wiki/%D0%9F%D0%B0%D1%81%D0%BA%D0%B0%D0%BB%D1%8C_(%D0%B5%D0%B4%D0%B8%D0%BD%D0%B8%D1%86%D0%B0_%D0%B8%D0%B7%D0%BC%D0%B5%D1%80%D0%B5%D0%BD%D0%B8%D1%8F)" title="Паскаль (единица измерения)">Па</a><br>(4⋅10<sup>−3</sup>—8,7⋅10<sup>−3</sup> <a href="/wiki/%D0%90%D1%82%D0%BC%D0%BE%D1%81%D1%84%D0%B5%D1%80%D0%B0_(%D0%B5%D0%B4%D0%B8%D0%BD%D0%B8%D1%86%D0%B0_%D0%B8%D0%B7%D0%BC%D0%B5%D1%80%D0%B5%D0%BD%D0%B8%D1%8F)" title="Атмосфера (единица измерения)">атм</a>)</td>
</tr>
<tr>
<td colspan="2" class="plainlist" style="text-align:center;">
<div style="text-align:left"><b>Состав:</b> <div style="margin-left:1em">95,32&nbsp;% <a href="/wiki/%D0%A3%D0%B3%D0%BB%D0%B5%D0%BA%D0%B8%D1%81%D0%BB%D1%8B%D0%B9_%D0%B3%D0%B0%D0%B7" class="mw-redirect" title="Углекислый газ">углекислый газ</a><br>
<p>2,7&nbsp;% <a href="/wiki/%D0%90%D0%B7%D0%BE%D1%82" title="Азот">азот</a><br>
1,6&nbsp;% <a href="/wiki/%D0%90%D1%80%D0%B3%D0%BE%D0%BD" title="Аргон">аргон</a><br>
0,145&nbsp;% <a href="/wiki/%D0%9A%D0%B8%D1%81%D0%BB%D0%BE%D1%80%D0%BE%D0%B4" title="Кислород">кислород</a><br>
0,08&nbsp;% <a href="/wiki/%D0%A3%D0%B3%D0%B0%D1%80%D0%BD%D1%8B%D0%B9_%D0%B3%D0%B0%D0%B7" class="mw-redirect" title="Угарный газ">угарный газ</a><br>
0,021&nbsp;% <a href="/wiki/%D0%92%D0%BE%D0%B4%D0%B0" title="Вода">водяной</a> пар<br>
0,01&nbsp;% <a href="/wiki/%D0%9E%D0%BA%D1%81%D0%B8%D0%B4_%D0%B0%D0%B7%D0%BE%D1%82%D0%B0(II)" title="Оксид азота(II)">окись азота</a><br>
</p>
0,00025&nbsp;% <a href="/wiki/%D0%9D%D0%B5%D0%BE%D0%BD" title="Неон">неон</a><br></div></div></td>
</tr><tr><td colspan="2" class="infobox-below" style=";"><span data-wikidata-claim-id="q111$414A3A47-C0B9-4561-92EA-57DBC44CA8D7" class="wikidata-claim" data-wikidata-property-id="P373"><span class="wikidata-snak wikidata-main-snak"><a href="https://commons.wikimedia.org/wiki/Category:Mars_(planet)" title="commons:Category:Mars (planet)"><img alt="Логотип Викисклада" src="//upload.wikimedia.org/wikipedia/commons/thumb/4/4a/Commons-logo.svg/15px-Commons-logo.svg.png" decoding="async" width="15" height="20" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/4/4a/Commons-logo.svg/23px-Commons-logo.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/4/4a/Commons-logo.svg/30px-Commons-logo.svg.png 2x" data-file-width="1024" data-file-height="1376"></a>&nbsp;<a href="https://commons.wikimedia.org/wiki/Category:Mars_(planet)" class="extiw" title="commons:Category:Mars (planet)">Медиафайлы на Викискладе</a></span></span></td></tr><tr><td colspan="2" class="infobox-below" style=";"><a href="https://www.wikidata.org/wiki/Special:ItemByTitle/ruwiki/%D0%9C%D0%B0%D1%80%D1%81" title="d:Special:ItemByTitle/ruwiki/Марс"><img alt="Логотип Викиданных" src="//upload.wikimedia.org/wikipedia/commons/thumb/e/e4/Wikidata-logo_S.svg/18px-Wikidata-logo_S.svg.png" decoding="async" width="18" height="10" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/e/e4/Wikidata-logo_S.svg/27px-Wikidata-logo_S.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/e/e4/Wikidata-logo_S.svg/36px-Wikidata-logo_S.svg.png 2x" data-file-width="1050" data-file-height="590"></a> <a href="https://www.wikidata.org/wiki/d:Special:ItemByTitle/ruwiki/%D0%9C%D0%B0%D1%80%D1%81" class="extiw" title="d:d:Special:ItemByTitle/ruwiki/Марс">Информация в Викиданных</a>&nbsp;<sup><style data-mw-deduplicate="TemplateStyles:r113275842">.mw-parser-output .ts-comment-commentedText{border-bottom:1px dotted;cursor:help}@media(hover:none){.mw-parser-output .ts-comment-commentedText:not(.rt-commentedText){border-bottom:0;cursor:auto}}</style><span class="ts-comment-commentedText" title="Элементы карточки, которых нет в окне редактирования статьи, редактируются в Викиданных">?</span></sup></td></tr>
</tbody></table>
        </div>
            <div class="col">
                <h2>Плюсы</h2>
                <div class="alert alert-success">Близко</div>
                <div class="alert alert-success">Самая схожая с Землей средняя температура по сравнению с остальными планетами</div>
                <h2>Минусы</h2>
                <div class="alert alert-danger">Низкое содержание воды и кислорода</div>
                <br><br>
                <div class="alert alert-info">Эта планета - лучший вариант для колонизации</div>
            </div>
        </body>
        </html>
        """
    if planet_name == "Юпитер":
        return """
        <!doctype html>
        <html>
        <head>
            <meta charset="utf-8">
            <meta name="viewport" content="width=device-width, initial-scale=1">
            <title>Юпитер</title>
            <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha2/dist/css/bootstrap.min.css" rel="stylesheet"
            integrity="sha384-aFq/bzH65dt+w6FI2ooMVUpc+21e0SRygnTpmBvdBgSdnuTN7QbdgL+OapgHtvPp" crossorigin="anonymous">
            <link rel="stylesheet" type="text/css" href="../static/css/style.css"/>
        </head>
        <body>
            <div class="table">
            <div class="row">
            <div class="col">
            <table class="infobox infobox-4cc3f8b605b53b7e" style="width:27em;" data-name="Планета"><tbody><tr><th colspan="2" scope="colgroup" class="infobox-above" style="">Юпитер <span data-wikidata-property-id="P367" class="no-wikidata"><a href="//commons.wikimedia.org/wiki/File:Jupiter_symbol_(bold).svg?uselang=ru" class="image"><img alt="Jupiter symbol (bold).svg" src="//upload.wikimedia.org/wikipedia/commons/thumb/7/78/Jupiter_symbol_%28bold%29.svg/20px-Jupiter_symbol_%28bold%29.svg.png" decoding="async" width="20" height="20" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/7/78/Jupiter_symbol_%28bold%29.svg/30px-Jupiter_symbol_%28bold%29.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/7/78/Jupiter_symbol_%28bold%29.svg/40px-Jupiter_symbol_%28bold%29.svg.png 2x" data-file-width="15" data-file-height="15"></a></span></th></tr><tr><td colspan="2" class="" style="text-align:center;"><a href="/wiki/%D0%9F%D0%BB%D0%B0%D0%BD%D0%B5%D1%82%D0%B0" title="Планета">Планета</a></td></tr><tr><td colspan="2" class="infobox-image" style=""> <span data-wikidata-property-id="P18" class="no-wikidata"><a href="//commons.wikimedia.org/wiki/File:Jupiter,_image_taken_by_NASA%27s_Hubble_Space_Telescope,_June_2019_-_Edited.jpg?uselang=ru" class="image" title="Фотография Юпитера, сделанная 27 июня 2019 года с телескопа «Хаббл»"><img alt="Фотография Юпитера, сделанная 27 июня 2019 года с телескопа «Хаббл»" src="//upload.wikimedia.org/wikipedia/commons/thumb/5/50/Jupiter%2C_image_taken_by_NASA%27s_Hubble_Space_Telescope%2C_June_2019_-_Edited.jpg/300px-Jupiter%2C_image_taken_by_NASA%27s_Hubble_Space_Telescope%2C_June_2019_-_Edited.jpg" decoding="async" width="300" height="288" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/5/50/Jupiter%2C_image_taken_by_NASA%27s_Hubble_Space_Telescope%2C_June_2019_-_Edited.jpg/450px-Jupiter%2C_image_taken_by_NASA%27s_Hubble_Space_Telescope%2C_June_2019_-_Edited.jpg 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/5/50/Jupiter%2C_image_taken_by_NASA%27s_Hubble_Space_Telescope%2C_June_2019_-_Edited.jpg/600px-Jupiter%2C_image_taken_by_NASA%27s_Hubble_Space_Telescope%2C_June_2019_-_Edited.jpg 2x" data-file-width="1525" data-file-height="1462"></a><br><span data-wikidata-qualifier-id="P2096" class="media-caption" style="display:block">Фотография Юпитера, сделанная 27 июня 2019 года с телескопа «<a href="/wiki/%D0%A5%D0%B0%D0%B1%D0%B1%D0%BB_(%D1%82%D0%B5%D0%BB%D0%B5%D1%81%D0%BA%D0%BE%D0%BF)" title="Хаббл (телескоп)">Хаббл</a>»</span></span> </td></tr>
<tr>
<th colspan="2" scope="colgroup" class="infobox-header" style="">Орбитальные характеристики</th>
</tr>
<tr>
<th scope="row" class="plainlist"><a href="/wiki/%D0%9F%D0%B5%D1%80%D0%B8%D0%B3%D0%B5%D0%BB%D0%B8%D0%B9" title="Перигелий">Перигелий</a></th>
<td class="plainlist">
<span data-wikidata-property-id="P2244" class="no-wikidata">7,405736⋅10<sup>8</sup> км<br>(4,950429 а.е.)<sup id="cite_ref-jupiter-info_1-0" class="reference"><a href="#cite_note-jupiter-info-1">[1]</a></sup></span></td>
</tr>
<tr>
<th scope="row" class="plainlist"><a href="/wiki/%D0%90%D1%84%D0%B5%D0%BB%D0%B8%D0%B9" title="Афелий">Афелий</a></th>
<td class="plainlist">
<span data-wikidata-property-id="P2243" class="no-wikidata">8,165208⋅10<sup>8</sup> км<br>(5,458104 а.е.)<sup id="cite_ref-jupiter-info_1-1" class="reference"><a href="#cite_note-jupiter-info-1">[1]</a></sup></span></td>
</tr>
<tr>
<th scope="row" class="plainlist"><a href="/wiki/%D0%91%D0%BE%D0%BB%D1%8C%D1%88%D0%B0%D1%8F_%D0%BF%D0%BE%D0%BB%D1%83%D0%BE%D1%81%D1%8C" title="Большая полуось">Большая полуось</a>&nbsp;(<style data-mw-deduplicate="TemplateStyles:r117753614">.mw-parser-output .ts-math{white-space:nowrap;font-family:times,serif,palatino linotype,new athena unicode,athena,gentium,code2000;font-size:120%}</style><span class="ts-math"><i>a</i></span>)</th>
<td class="plainlist">
<span data-wikidata-property-id="P2233" class="no-wikidata">7,785472⋅10<sup>8</sup> км<br>(5,204267 а.е.)<sup id="cite_ref-nasa-jupiter_2-0" class="reference"><a href="#cite_note-nasa-jupiter-2">[2]</a></sup></span></td>
</tr>
<tr>
<th scope="row" class="plainlist"><a href="/wiki/%D0%AD%D0%BA%D1%81%D1%86%D0%B5%D0%BD%D1%82%D1%80%D0%B8%D1%81%D0%B8%D1%82%D0%B5%D1%82_%D0%BE%D1%80%D0%B1%D0%B8%D1%82%D1%8B" title="Эксцентриситет орбиты">Эксцентриситет орбиты</a>&nbsp;(<link rel="mw-deduplicated-inline-style" href="mw-data:TemplateStyles:r117753614"><span class="ts-math"><i>e</i></span>)</th>
<td class="plainlist">
<span data-wikidata-property-id="P1096" class="no-wikidata">0,048775<sup id="cite_ref-jupiter-info_1-2" class="reference"><a href="#cite_note-jupiter-info-1">[1]</a></sup></span></td>
</tr>
<tr>
<th scope="row" class="plainlist"><a href="/wiki/%D0%A1%D0%B8%D0%B4%D0%B5%D1%80%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B8%D0%B9_%D0%BF%D0%B5%D1%80%D0%B8%D0%BE%D0%B4" title="Сидерический период">Сидерический период</a> обращения</th>
<td class="plainlist">
<span data-wikidata-property-id="P2146" class="no-wikidata">4332,589 дня (11,8618 года)<sup id="cite_ref-jupiter-info_1-3" class="reference"><a href="#cite_note-jupiter-info-1">[1]</a></sup></span></td>
</tr>
<tr>
<th scope="row" class="plainlist"><a href="/wiki/%D0%A1%D0%B8%D0%BD%D0%BE%D0%B4%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B8%D0%B9_%D0%BF%D0%B5%D1%80%D0%B8%D0%BE%D0%B4" title="Синодический период">Синодический период</a> обращения</th>
<td class="plainlist">
<span data-wikidata-property-id="P4341" class="no-wikidata">398,88 дня<sup id="cite_ref-jupiter-info_1-4" class="reference"><a href="#cite_note-jupiter-info-1">[1]</a></sup></span></td>
</tr>
<tr>
<th scope="row" class="plainlist"><a href="/wiki/%D0%9E%D1%80%D0%B1%D0%B8%D1%82%D0%B0%D0%BB%D1%8C%D0%BD%D0%B0%D1%8F_%D1%81%D0%BA%D0%BE%D1%80%D0%BE%D1%81%D1%82%D1%8C" title="Орбитальная скорость">Орбитальная скорость</a>&nbsp;(<link rel="mw-deduplicated-inline-style" href="mw-data:TemplateStyles:r117753614"><span class="ts-math"><i>v</i></span>)</th>
<td class="plainlist">
13,07 км/с (средн.)<sup id="cite_ref-jupiter-info_1-5" class="reference"><a href="#cite_note-jupiter-info-1">[1]</a></sup></td>
</tr>
<tr>
<th scope="row" class="plainlist"><a href="/wiki/%D0%9A%D0%B5%D0%BF%D0%BB%D0%B5%D1%80%D0%BE%D0%B2%D1%8B_%D1%8D%D0%BB%D0%B5%D0%BC%D0%B5%D0%BD%D1%82%D1%8B_%D0%BE%D1%80%D0%B1%D0%B8%D1%82%D1%8B#Наклонение" title="Кеплеровы элементы орбиты">Наклонение</a>&nbsp;(<link rel="mw-deduplicated-inline-style" href="mw-data:TemplateStyles:r117753614"><span class="ts-math"><i>i</i></span>)</th>
<td class="plainlist">
<span data-wikidata-property-id="P2045" class="no-wikidata">1,304° (относительно эклиптики)<br>6,09° (относительно солнечного экватора)</span></td>
</tr>
<tr>
<th scope="row" class="plainlist"><a href="/wiki/%D0%94%D0%BE%D0%BB%D0%B3%D0%BE%D1%82%D0%B0_%D0%B2%D0%BE%D1%81%D1%85%D0%BE%D0%B4%D1%8F%D1%89%D0%B5%D0%B3%D0%BE_%D1%83%D0%B7%D0%BB%D0%B0" class="mw-redirect" title="Долгота восходящего узла">Долгота восходящего узла</a>&nbsp;(<link rel="mw-deduplicated-inline-style" href="mw-data:TemplateStyles:r117753614"><span class="ts-math">Ω</span>)</th>
<td class="plainlist">
<span data-wikidata-property-id="P2213" class="no-wikidata">100,55615°<sup id="cite_ref-jupiter-info_1-6" class="reference"><a href="#cite_note-jupiter-info-1">[1]</a></sup></span></td>
</tr>
<tr>
<th scope="row" class="plainlist"><a href="/wiki/%D0%90%D1%80%D0%B3%D1%83%D0%BC%D0%B5%D0%BD%D1%82_%D0%BF%D0%B5%D1%80%D0%B8%D1%86%D0%B5%D0%BD%D1%82%D1%80%D0%B0" class="mw-redirect" title="Аргумент перицентра">Аргумент перицентра</a>&nbsp;(<link rel="mw-deduplicated-inline-style" href="mw-data:TemplateStyles:r117753614"><span class="ts-math">ω</span>)</th>
<td class="plainlist">
<span data-wikidata-property-id="P2248" class="no-wikidata">275,066°</span></td>
</tr>
<tr>
<th scope="row" class="plainlist">Чей спутник</th>
<td class="plainlist">
<span data-wikidata-claim-id="q319$764C2E46-EA8F-4AA3-A7B3-AF3629FE8AE3" class="wikidata-claim" data-wikidata-property-id="P397"><span class="wikidata-snak wikidata-main-snak"><a href="/wiki/%D0%A1%D0%BE%D0%BB%D0%BD%D1%86%D0%B5" title="Солнце">Солнце</a></span></span></td>
</tr>
<tr>
<th scope="row" class="plainlist">Спутники</th>
<td class="plainlist">
<span data-wikidata-property-id="P398" class="no-wikidata"><a href="/wiki/%D0%A1%D0%BF%D1%83%D1%82%D0%BD%D0%B8%D0%BA%D0%B8_%D0%AE%D0%BF%D0%B8%D1%82%D0%B5%D1%80%D0%B0" title="Спутники Юпитера">92</a><sup id="cite_ref-автоссылка1_3-0" class="reference"><a href="#cite_note-автоссылка1-3">[3]</a></sup><sup id="cite_ref-автоссылка2_4-0" class="reference"><a href="#cite_note-автоссылка2-4">[4]</a></sup><sup id="cite_ref-автоссылка3_5-0" class="reference"><a href="#cite_note-автоссылка3-5">[5]</a></sup><sup id="cite_ref-автоссылка4_6-0" class="reference"><a href="#cite_note-автоссылка4-6">[6]</a></sup></span></td>
</tr>
<tr>
<th colspan="2" scope="colgroup" class="infobox-header" style="">Физические характеристики</th>
</tr>
<tr>
<th scope="row" class="plainlist">Полярное сжатие</th>
<td class="plainlist">
<span data-wikidata-property-id="P1102" class="no-wikidata">0,06487<sup id="cite_ref-jupiter-info_1-7" class="reference"><a href="#cite_note-jupiter-info-1">[1]</a></sup></span></td>
</tr>
<tr>
<th scope="row" class="plainlist"><a href="/wiki/%D0%AD%D0%BA%D0%B2%D0%B0%D1%82%D0%BE%D1%80" title="Экватор">Экваториальный</a> радиус</th>
<td class="plainlist">
71&nbsp;492 ± 4 км<sup id="cite_ref-jupiter-info_1-8" class="reference"><a href="#cite_note-jupiter-info-1">[1]</a></sup></td>
</tr>
<tr>
<th scope="row" class="plainlist"><a href="/wiki/%D0%93%D0%B5%D0%BE%D0%B3%D1%80%D0%B0%D1%84%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B8%D0%B9_%D0%BF%D0%BE%D0%BB%D1%8E%D1%81" title="Географический полюс">Полярный</a> радиус</th>
<td class="plainlist">
66&nbsp;854 ± 10 км<sup id="cite_ref-jupiter-info_1-9" class="reference"><a href="#cite_note-jupiter-info-1">[1]</a></sup></td>
</tr>
<tr>
<th scope="row" class="plainlist">Средний радиус</th>
<td class="plainlist">
69&nbsp;911 ± 6 км<sup id="cite_ref-Seidelmann_Archinal_A'hearn_et_al._2007_7-0" class="reference"><a href="#cite_note-Seidelmann_Archinal_A'hearn_et_al._2007-7">[7]</a></sup></td>
</tr>
<tr>
<th scope="row" class="plainlist">Площадь поверхности&nbsp;(<link rel="mw-deduplicated-inline-style" href="mw-data:TemplateStyles:r117753614"><span class="ts-math"><i>S</i></span>)</th>
<td class="plainlist">
6,21796⋅10<sup>10</sup> км²<br>121,9&nbsp;земных</td>
</tr>
<tr>
<th scope="row" class="plainlist">Объём&nbsp;(<link rel="mw-deduplicated-inline-style" href="mw-data:TemplateStyles:r117753614"><span class="ts-math"><i>V</i></span>)</th>
<td class="plainlist">
1,43128⋅10<sup>15</sup> км³<br>1321,3&nbsp;земных</td>
</tr>
<tr>
<th scope="row" class="plainlist">Масса&nbsp;(<link rel="mw-deduplicated-inline-style" href="mw-data:TemplateStyles:r117753614"><span class="ts-math"><i>m</i></span>)</th>
<td class="plainlist">
<span data-wikidata-property-id="P2067" class="no-wikidata">1,8986⋅10<sup>27</sup> кг<br>317,8&nbsp;земных</span></td>
</tr>
<tr>
<th scope="row" class="plainlist">Средняя <a href="/wiki/%D0%9F%D0%BB%D0%BE%D1%82%D0%BD%D0%BE%D1%81%D1%82%D1%8C" title="Плотность">плотность</a>&nbsp;(<link rel="mw-deduplicated-inline-style" href="mw-data:TemplateStyles:r117753614"><span class="ts-math">ρ</span>)</th>
<td class="plainlist">
1326 кг/м³<sup id="cite_ref-jupiter-info_1-10" class="reference"><a href="#cite_note-jupiter-info-1">[1]</a></sup></td>
</tr>
<tr>
<th scope="row" class="plainlist"><a href="/wiki/%D0%A3%D1%81%D0%BA%D0%BE%D1%80%D0%B5%D0%BD%D0%B8%D0%B5_%D1%81%D0%B2%D0%BE%D0%B1%D0%BE%D0%B4%D0%BD%D0%BE%D0%B3%D0%BE_%D0%BF%D0%B0%D0%B4%D0%B5%D0%BD%D0%B8%D1%8F" title="Ускорение свободного падения">Ускорение свободного падения</a> на экваторе&nbsp;(<link rel="mw-deduplicated-inline-style" href="mw-data:TemplateStyles:r117753614"><span class="ts-math"><i>g</i></span>)</th>
<td class="plainlist">
24,79 м/с² (2,535 g)</td>
</tr>
<tr>
<th scope="row" class="plainlist"><a href="/wiki/%D0%9F%D0%B5%D1%80%D0%B2%D0%B0%D1%8F_%D0%BA%D0%BE%D1%81%D0%BC%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B0%D1%8F_%D1%81%D0%BA%D0%BE%D1%80%D0%BE%D1%81%D1%82%D1%8C" title="Первая космическая скорость">Первая космическая скорость</a>&nbsp;(<link rel="mw-deduplicated-inline-style" href="mw-data:TemplateStyles:r117753614"><span class="ts-math"><i>v</i></span><sub>1</sub>)</th>
<td class="plainlist">
42,58 км/с</td>
</tr>
<tr>
<th scope="row" class="plainlist"><a href="/wiki/%D0%92%D1%82%D0%BE%D1%80%D0%B0%D1%8F_%D0%BA%D0%BE%D1%81%D0%BC%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B0%D1%8F_%D1%81%D0%BA%D0%BE%D1%80%D0%BE%D1%81%D1%82%D1%8C" title="Вторая космическая скорость">Вторая космическая скорость</a>&nbsp;(<link rel="mw-deduplicated-inline-style" href="mw-data:TemplateStyles:r117753614"><span class="ts-math"><i>v</i></span><sub>2</sub>)</th>
<td class="plainlist">
59,5 км/с<sup id="cite_ref-jupiter-info_1-11" class="reference"><a href="#cite_note-jupiter-info-1">[1]</a></sup></td>
</tr>
<tr>
<th scope="row" class="plainlist">Экваториальная скорость вращения</th>
<td class="plainlist">
12,6 км/с или 45&nbsp;300 км/ч</td>
</tr>
<tr>
<th scope="row" class="plainlist"><a href="/wiki/%D0%9F%D0%B5%D1%80%D0%B8%D0%BE%D0%B4_%D0%B2%D1%80%D0%B0%D1%89%D0%B5%D0%BD%D0%B8%D1%8F" title="Период вращения">Период вращения</a>&nbsp;(<link rel="mw-deduplicated-inline-style" href="mw-data:TemplateStyles:r117753614"><span class="ts-math"><i>T</i></span>)</th>
<td class="plainlist">
9,925 часа<sup id="cite_ref-jupiter-info_1-12" class="reference"><a href="#cite_note-jupiter-info-1">[1]</a></sup></td>
</tr>
<tr>
<th scope="row" class="plainlist"><a href="/wiki/%D0%9D%D0%B0%D0%BA%D0%BB%D0%BE%D0%BD_%D0%BE%D1%81%D0%B8_%D0%B2%D1%80%D0%B0%D1%89%D0%B5%D0%BD%D0%B8%D1%8F" title="Наклон оси вращения">Наклон оси</a></th>
<td class="plainlist">
3,13°</td>
</tr>
<tr>
<th scope="row" class="plainlist"><a href="/wiki/%D0%9F%D1%80%D1%8F%D0%BC%D0%BE%D0%B5_%D0%B2%D0%BE%D1%81%D1%85%D0%BE%D0%B6%D0%B4%D0%B5%D0%BD%D0%B8%D0%B5" title="Прямое восхождение">Прямое восхождение</a> северного полюса&nbsp;(<link rel="mw-deduplicated-inline-style" href="mw-data:TemplateStyles:r117753614"><span class="ts-math">α</span>)</th>
<td class="plainlist">
17 ч 52 мин 14 с<br>268,057°</td>
</tr>
<tr>
<th scope="row" class="plainlist"><a href="/wiki/%D0%A1%D0%BA%D0%BB%D0%BE%D0%BD%D0%B5%D0%BD%D0%B8%D0%B5_(%D0%B0%D1%81%D1%82%D1%80%D0%BE%D0%BD%D0%BE%D0%BC%D0%B8%D1%8F)" title="Склонение (астрономия)">Склонение</a> северного полюса&nbsp;(<link rel="mw-deduplicated-inline-style" href="mw-data:TemplateStyles:r117753614"><span class="ts-math">δ</span>)</th>
<td class="plainlist">
64,496°</td>
</tr>
<tr>
<th scope="row" class="plainlist"><a href="/wiki/%D0%90%D0%BB%D1%8C%D0%B1%D0%B5%D0%B4%D0%BE" title="Альбедо">Альбедо</a></th>
<td class="plainlist">
0,343 (<a href="/wiki/%D0%90%D0%BB%D1%8C%D0%B1%D0%B5%D0%B4%D0%BE_%D0%91%D0%BE%D0%BD%D0%B4%D0%B0" class="mw-redirect" title="Альбедо Бонда">Бонд</a>)<sup id="cite_ref-jupiter-info_1-13" class="reference"><a href="#cite_note-jupiter-info-1">[1]</a></sup><br>0,52 (<a href="/wiki/%D0%93%D0%B5%D0%BE%D0%BC%D0%B5%D1%82%D1%80%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%BE%D0%B5_%D0%B0%D0%BB%D1%8C%D0%B1%D0%B5%D0%B4%D0%BE" class="mw-redirect" title="Геометрическое альбедо">геом. альбедо</a>)<sup id="cite_ref-jupiter-info_1-14" class="reference"><a href="#cite_note-jupiter-info-1">[1]</a></sup></td>
</tr>
<tr>
<th scope="row" class="plainlist"><a href="/wiki/%D0%92%D0%B8%D0%B4%D0%B8%D0%BC%D0%B0%D1%8F_%D0%B7%D0%B2%D1%91%D0%B7%D0%B4%D0%BD%D0%B0%D1%8F_%D0%B2%D0%B5%D0%BB%D0%B8%D1%87%D0%B8%D0%BD%D0%B0" title="Видимая звёздная величина">Видимая звёздная величина</a></th>
<td class="plainlist">
<span data-wikidata-property-id="P1215" class="no-wikidata">от −1,61 до −2,94</span></td>
</tr>
<tr>
<th scope="row" class="plainlist"><a href="/wiki/%D0%90%D0%B1%D1%81%D0%BE%D0%BB%D1%8E%D1%82%D0%BD%D0%B0%D1%8F_%D0%B7%D0%B2%D1%91%D0%B7%D0%B4%D0%BD%D0%B0%D1%8F_%D0%B2%D0%B5%D0%BB%D0%B8%D1%87%D0%B8%D0%BD%D0%B0" title="Абсолютная звёздная величина">Абсолютная звёздная величина</a></th>
<td class="plainlist">
<span data-wikidata-property-id="P1457" class="no-wikidata">−9,4</span></td>
</tr>
<tr>
<th scope="row" class="plainlist"><a href="/wiki/%D0%A3%D0%B3%D0%BB%D0%BE%D0%B2%D0%BE%D0%B9_%D0%B4%D0%B8%D0%B0%D0%BC%D0%B5%D1%82%D1%80" class="mw-redirect" title="Угловой диаметр">Угловой диаметр</a></th>
<td class="plainlist">
29,8″—50,1″</td>
</tr>
<tr>
<th colspan="2" scope="colgroup" class="infobox-header" style=""><a href="/wiki/%D0%90%D1%82%D0%BC%D0%BE%D1%81%D1%84%D0%B5%D1%80%D0%B0" title="Атмосфера">Атмосфера</a></th>
</tr>
<tr>
<th scope="row" class="plainlist"><a href="/wiki/%D0%90%D1%82%D0%BC%D0%BE%D1%81%D1%84%D0%B5%D1%80%D0%BD%D0%BE%D0%B5_%D0%B4%D0%B0%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5" title="Атмосферное давление">Атмосферное давление</a></th>
<td class="plainlist">
20—220 <a href="/wiki/%D0%9F%D0%B0%D1%81%D0%BA%D0%B0%D0%BB%D1%8C_(%D0%B5%D0%B4%D0%B8%D0%BD%D0%B8%D1%86%D0%B0_%D0%B8%D0%B7%D0%BC%D0%B5%D1%80%D0%B5%D0%BD%D0%B8%D1%8F)" title="Паскаль (единица измерения)">кПа</a><sup id="cite_ref-8" class="reference"><a href="#cite_note-8">[8]</a></sup></td>
</tr>
<tr>
<th scope="row" class="plainlist"><a href="/wiki/%D0%A8%D0%BA%D0%B0%D0%BB%D0%B0_%D0%B2%D1%8B%D1%81%D0%BE%D1%82%D1%8B" class="mw-redirect" title="Шкала высоты">Шкала высоты</a></th>
<td class="plainlist">
27 км</td>
</tr>
<tr>
<td colspan="2" class="plainlist" style="text-align:center;">
<div style="text-align:left"><b>Состав:</b> <div style="margin-left:1em"><table class="transparent">
<tbody><tr><td>
89,8±2,0&nbsp;%</td><td><a href="/wiki/%D0%92%D0%BE%D0%B4%D0%BE%D1%80%D0%BE%D0%B4" title="Водород">Водород</a> (H<sub>2</sub>)
</td></tr><tr><td>
10,2±2,0&nbsp;%</td><td><a href="/wiki/%D0%93%D0%B5%D0%BB%D0%B8%D0%B9" title="Гелий">Гелий</a> (He)
</td></tr><tr><td>
~0,3&nbsp;%</td><td><a href="/wiki/%D0%9C%D0%B5%D1%82%D0%B0%D0%BD" title="Метан">Метан</a> (CH<sub>4</sub>)
</td></tr><tr><td>
~0,026&nbsp;%</td><td><a href="/wiki/%D0%90%D0%BC%D0%BC%D0%BE%D0%BD%D0%B8%D0%B9" title="Аммоний">Аммоний</a> (NH<sub>4</sub><sup>+</sup>)
</td></tr><tr><td>
~0,003&nbsp;%</td><td><a href="/wiki/%D0%94%D0%B5%D0%B9%D1%82%D0%B5%D1%80%D0%B8%D0%B4_%D0%B2%D0%BE%D0%B4%D0%BE%D1%80%D0%BE%D0%B4%D0%B0" title="Дейтерид водорода">Дейтерид водорода</a> (HD)
</td></tr><tr><td>
0,0006&nbsp;%</td><td><a href="/wiki/%D0%AD%D1%82%D0%B0%D0%BD" title="Этан">Этан</a> (CH<sub>3</sub>−CH<sub>3</sub>)
</td></tr><tr><td>
0,0004&nbsp;%</td><td><a href="/wiki/%D0%92%D0%BE%D0%B4%D0%B0" title="Вода">Вода</a> (H<sub>2</sub>O)
</td></tr><tr><td>
<b>Льды</b>:</td><td>
</td></tr><tr><td>
</td><td><a href="/wiki/%D0%90%D0%BC%D0%BC%D0%BE%D0%BD%D0%B8%D0%B9" title="Аммоний">Аммоний</a>
</td></tr><tr><td>
</td><td><a href="/wiki/%D0%92%D0%BE%D0%B4%D0%B0" title="Вода">Вода</a>
</td></tr><tr><td>
</td><td><a href="/wiki/%D0%93%D0%B8%D0%B4%D1%80%D0%BE%D1%81%D1%83%D0%BB%D1%8C%D1%84%D0%B8%D0%B4_%D0%B0%D0%BC%D0%BC%D0%BE%D0%BD%D0%B8%D1%8F" title="Гидросульфид аммония">Гидросульфид аммония</a> (NH<sub>4</sub>SH)
</td></tr></tbody></table></div></div></td>
</tr><tr><td colspan="2" class="infobox-below" style=";"><span data-wikidata-claim-id="q319$0FE31656-AEA5-4D36-942D-61006B5DE2A8" class="wikidata-claim" data-wikidata-property-id="P373"><span class="wikidata-snak wikidata-main-snak"><a href="https://commons.wikimedia.org/wiki/Category:Jupiter_(planet)" title="commons:Category:Jupiter (planet)"><img alt="Логотип Викисклада" src="//upload.wikimedia.org/wikipedia/commons/thumb/4/4a/Commons-logo.svg/15px-Commons-logo.svg.png" decoding="async" width="15" height="20" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/4/4a/Commons-logo.svg/23px-Commons-logo.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/4/4a/Commons-logo.svg/30px-Commons-logo.svg.png 2x" data-file-width="1024" data-file-height="1376"></a>&nbsp;<a href="https://commons.wikimedia.org/wiki/Category:Jupiter_(planet)" class="extiw" title="commons:Category:Jupiter (planet)">Медиафайлы на Викискладе</a></span></span></td></tr><tr><td colspan="2" class="infobox-below" style=";"><a href="https://www.wikidata.org/wiki/Special:ItemByTitle/ruwiki/%D0%AE%D0%BF%D0%B8%D1%82%D0%B5%D1%80" title="d:Special:ItemByTitle/ruwiki/Юпитер"><img alt="Логотип Викиданных" src="//upload.wikimedia.org/wikipedia/commons/thumb/e/e4/Wikidata-logo_S.svg/18px-Wikidata-logo_S.svg.png" decoding="async" width="18" height="10" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/e/e4/Wikidata-logo_S.svg/27px-Wikidata-logo_S.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/e/e4/Wikidata-logo_S.svg/36px-Wikidata-logo_S.svg.png 2x" data-file-width="1050" data-file-height="590"></a> <a href="https://www.wikidata.org/wiki/d:Special:ItemByTitle/ruwiki/%D0%AE%D0%BF%D0%B8%D1%82%D0%B5%D1%80" class="extiw" title="d:d:Special:ItemByTitle/ruwiki/Юпитер">Информация в Викиданных</a>&nbsp;<sup><style data-mw-deduplicate="TemplateStyles:r113275842">.mw-parser-output .ts-comment-commentedText{border-bottom:1px dotted;cursor:help}@media(hover:none){.mw-parser-output .ts-comment-commentedText:not(.rt-commentedText){border-bottom:0;cursor:auto}}</style><span class="ts-comment-commentedText" title="Элементы карточки, которых нет в окне редактирования статьи, редактируются в Викиданных">?</span></sup></td></tr>
</tbody></table>
        </div>
            <div class="col">
                <h2>Минусы</h2>
                <div class="alert alert-danger">На поверхности планеты один газ</div>
                <br><br>
                <div class="alert alert-info">Колонизация невозможна</div>
            </div>
        </body>
        </html>
        """
    if planet_name == "Сатурн":
        return """
        <!doctype html>
        <html>
        <head>
            <meta charset="utf-8">
            <meta name="viewport" content="width=device-width, initial-scale=1">
            <title>Сатурн</title>
            <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha2/dist/css/bootstrap.min.css" rel="stylesheet"
            integrity="sha384-aFq/bzH65dt+w6FI2ooMVUpc+21e0SRygnTpmBvdBgSdnuTN7QbdgL+OapgHtvPp" crossorigin="anonymous">
            <link rel="stylesheet" type="text/css" href="../static/css/style.css"/>
        </head>
        <body>
            <div class="table">
            <div class="row">
            <div class="col">
            <table class="infobox infobox-56165a6c4b2a4982" style="width:27em;" data-name="Планета"><tbody><tr><th colspan="2" scope="colgroup" class="infobox-above" style="">Сатурн <span data-wikidata-property-id="P367" class="no-wikidata"><a href="//commons.wikimedia.org/wiki/File:Saturn_symbol_(bold).svg?uselang=ru" class="image"><img alt="Saturn symbol (bold).svg" src="//upload.wikimedia.org/wikipedia/commons/thumb/1/1f/Saturn_symbol_%28bold%29.svg/20px-Saturn_symbol_%28bold%29.svg.png" decoding="async" width="20" height="20" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/1/1f/Saturn_symbol_%28bold%29.svg/30px-Saturn_symbol_%28bold%29.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/1/1f/Saturn_symbol_%28bold%29.svg/40px-Saturn_symbol_%28bold%29.svg.png 2x" data-file-width="15" data-file-height="15"></a></span></th></tr><tr><td colspan="2" class="" style="text-align:center;"><a href="/wiki/%D0%9F%D0%BB%D0%B0%D0%BD%D0%B5%D1%82%D0%B0" title="Планета">Планета</a></td></tr><tr><td colspan="2" class="infobox-image" style=""> <span data-wikidata-property-id="P18" class="no-wikidata"><a href="//commons.wikimedia.org/wiki/File:Saturn_-_April_25_2016_(37612580000).png?uselang=ru" class="image" title="Изображение Сатурна на основе снимков КА «Кассини», сделанных 25 апреля 2016 года."><img alt="Изображение Сатурна на основе снимков КА «Кассини», сделанных 25 апреля 2016 года." src="//upload.wikimedia.org/wikipedia/commons/thumb/c/c1/Saturn_-_April_25_2016_%2837612580000%29.png/300px-Saturn_-_April_25_2016_%2837612580000%29.png" decoding="async" width="300" height="164" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/c/c1/Saturn_-_April_25_2016_%2837612580000%29.png/450px-Saturn_-_April_25_2016_%2837612580000%29.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/c/c1/Saturn_-_April_25_2016_%2837612580000%29.png/600px-Saturn_-_April_25_2016_%2837612580000%29.png 2x" data-file-width="1647" data-file-height="899"></a><br><span data-wikidata-qualifier-id="P2096" class="media-caption" style="display:block">Изображение Сатурна на основе снимков <a href="/wiki/%D0%9A%D0%B0%D1%81%D1%81%D0%B8%D0%BD%D0%B8_(%D0%BA%D0%BE%D1%81%D0%BC%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B8%D0%B9_%D0%B0%D0%BF%D0%BF%D0%B0%D1%80%D0%B0%D1%82)" title="Кассини (космический аппарат)">КА «Кассини»</a>, сделанных 25 апреля 2016 года.</span></span> </td></tr>
<tr>
<th colspan="2" scope="colgroup" class="infobox-header" style="">Орбитальные характеристики</th>
</tr>
<tr>
<th scope="row" class="plainlist"><a href="/wiki/%D0%9F%D0%B5%D1%80%D0%B8%D0%B3%D0%B5%D0%BB%D0%B8%D0%B9" title="Перигелий">Перигелий</a></th>
<td class="plainlist">
<span data-wikidata-property-id="P2244" class="no-wikidata">1&nbsp;353&nbsp;572&nbsp;956&nbsp;км<br>9,048&nbsp;а.&nbsp;е.</span></td>
</tr>
<tr>
<th scope="row" class="plainlist"><a href="/wiki/%D0%90%D1%84%D0%B5%D0%BB%D0%B8%D0%B9" title="Афелий">Афелий</a></th>
<td class="plainlist">
<span data-wikidata-property-id="P2243" class="no-wikidata">1&nbsp;513&nbsp;325&nbsp;783&nbsp;км<br>10,116&nbsp;<a href="/wiki/%D0%90%D1%81%D1%82%D1%80%D0%BE%D0%BD%D0%BE%D0%BC%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B0%D1%8F_%D0%B5%D0%B4%D0%B8%D0%BD%D0%B8%D1%86%D0%B0" title="Астрономическая единица">а.&nbsp;е.</a></span></td>
</tr>
<tr>
<th scope="row" class="plainlist"><a href="/wiki/%D0%91%D0%BE%D0%BB%D1%8C%D1%88%D0%B0%D1%8F_%D0%BF%D0%BE%D0%BB%D1%83%D0%BE%D1%81%D1%8C" title="Большая полуось">Большая полуось</a>&nbsp;(<style data-mw-deduplicate="TemplateStyles:r117753614">.mw-parser-output .ts-math{white-space:nowrap;font-family:times,serif,palatino linotype,new athena unicode,athena,gentium,code2000;font-size:120%}</style><span class="ts-math"><i>a</i></span>)</th>
<td class="plainlist">
<span data-wikidata-claim-id="Q193$6254e3ab-4166-c06f-2a71-35f5b33791b6" class="wikidata-claim" data-wikidata-property-id="P2233"><span class="wikidata-snak wikidata-main-snak">1&nbsp;429&nbsp;394&nbsp;069&nbsp;± 0&nbsp;км</span><sup id="cite_ref-_d57da5e24284929e_11-0" class="reference"><a href="#cite_note-_d57da5e24284929e-11">[11]</a></sup></span> и <span data-wikidata-claim-id="Q193$c6fafc12-410d-4e02-1f74-eb2ee04ca3a8" class="wikidata-claim" data-wikidata-property-id="P2233"><span class="wikidata-snak wikidata-main-snak">1&nbsp;426&nbsp;666&nbsp;414&nbsp;179,9&nbsp;м</span><sup id="cite_ref-_170395512d6649af_12-0" class="reference"><a href="#cite_note-_170395512d6649af-12">[12]</a></sup></span></td>
</tr>
<tr>
<th scope="row" class="plainlist"><a href="/wiki/%D0%AD%D0%BA%D1%81%D1%86%D0%B5%D0%BD%D1%82%D1%80%D0%B8%D1%81%D0%B8%D1%82%D0%B5%D1%82_%D0%BE%D1%80%D0%B1%D0%B8%D1%82%D1%8B" title="Эксцентриситет орбиты">Эксцентриситет орбиты</a>&nbsp;(<link rel="mw-deduplicated-inline-style" href="mw-data:TemplateStyles:r117753614"><span class="ts-math"><i>e</i></span>)</th>
<td class="plainlist">
<span data-wikidata-property-id="P1096" class="no-wikidata">0,055723219</span></td>
</tr>
<tr>
<th scope="row" class="plainlist"><a href="/wiki/%D0%A1%D0%B8%D0%B4%D0%B5%D1%80%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B8%D0%B9_%D0%BF%D0%B5%D1%80%D0%B8%D0%BE%D0%B4" title="Сидерический период">Сидерический период</a> обращения</th>
<td class="plainlist">
<span data-wikidata-property-id="P2146" class="no-wikidata">10 759,22&nbsp;суток (29,46&nbsp;года)<sup id="cite_ref-1" class="reference"><a href="#cite_note-1">[1]</a></sup></span></td>
</tr>
<tr>
<th scope="row" class="plainlist"><a href="/wiki/%D0%A1%D0%B8%D0%BD%D0%BE%D0%B4%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B8%D0%B9_%D0%BF%D0%B5%D1%80%D0%B8%D0%BE%D0%B4" title="Синодический период">Синодический период</a> обращения</th>
<td class="plainlist">
<span data-wikidata-property-id="P4341" class="no-wikidata">378,09 суток</span></td>
</tr>
<tr>
<th scope="row" class="plainlist"><a href="/wiki/%D0%9E%D1%80%D0%B1%D0%B8%D1%82%D0%B0%D0%BB%D1%8C%D0%BD%D0%B0%D1%8F_%D1%81%D0%BA%D0%BE%D1%80%D0%BE%D1%81%D1%82%D1%8C" title="Орбитальная скорость">Орбитальная скорость</a>&nbsp;(<link rel="mw-deduplicated-inline-style" href="mw-data:TemplateStyles:r117753614"><span class="ts-math"><i>v</i></span>)</th>
<td class="plainlist">
9,69&nbsp;км/с</td>
</tr>
<tr>
<th scope="row" class="plainlist"><a href="/wiki/%D0%9A%D0%B5%D0%BF%D0%BB%D0%B5%D1%80%D0%BE%D0%B2%D1%8B_%D1%8D%D0%BB%D0%B5%D0%BC%D0%B5%D0%BD%D1%82%D1%8B_%D0%BE%D1%80%D0%B1%D0%B8%D1%82%D1%8B#Наклонение" title="Кеплеровы элементы орбиты">Наклонение</a>&nbsp;(<link rel="mw-deduplicated-inline-style" href="mw-data:TemplateStyles:r117753614"><span class="ts-math"><i>i</i></span>)</th>
<td class="plainlist">
<span data-wikidata-property-id="P2045" class="no-wikidata">2,485240°<br>5,51° (относительно солнечного экватора)</span></td>
</tr>
<tr>
<th scope="row" class="plainlist"><a href="/wiki/%D0%94%D0%BE%D0%BB%D0%B3%D0%BE%D1%82%D0%B0_%D0%B2%D0%BE%D1%81%D1%85%D0%BE%D0%B4%D1%8F%D1%89%D0%B5%D0%B3%D0%BE_%D1%83%D0%B7%D0%BB%D0%B0" class="mw-redirect" title="Долгота восходящего узла">Долгота восходящего узла</a>&nbsp;(<link rel="mw-deduplicated-inline-style" href="mw-data:TemplateStyles:r117753614"><span class="ts-math">Ω</span>)</th>
<td class="plainlist">
<span data-wikidata-property-id="P2213" class="no-wikidata">113,642&nbsp;811°</span></td>
</tr>
<tr>
<th scope="row" class="plainlist"><a href="/wiki/%D0%90%D1%80%D0%B3%D1%83%D0%BC%D0%B5%D0%BD%D1%82_%D0%BF%D0%B5%D1%80%D0%B8%D1%86%D0%B5%D0%BD%D1%82%D1%80%D0%B0" class="mw-redirect" title="Аргумент перицентра">Аргумент перицентра</a>&nbsp;(<link rel="mw-deduplicated-inline-style" href="mw-data:TemplateStyles:r117753614"><span class="ts-math">ω</span>)</th>
<td class="plainlist">
<span data-wikidata-property-id="P2248" class="no-wikidata">336,013&nbsp;862°</span></td>
</tr>
<tr>
<th scope="row" class="plainlist">Чей спутник</th>
<td class="plainlist">
<span data-wikidata-claim-id="q193$65629D2B-44CD-45D9-AE81-9D70759E1B7D" class="wikidata-claim" data-wikidata-property-id="P397"><span class="wikidata-snak wikidata-main-snak"><a href="/wiki/%D0%A1%D0%BE%D0%BB%D0%BD%D1%86%D0%B5" title="Солнце">Солнце</a></span></span></td>
</tr>
<tr>
<th scope="row" class="plainlist">Спутники</th>
<td class="plainlist">
<span data-wikidata-property-id="P398" class="no-wikidata"><a href="/wiki/%D0%A1%D0%BF%D1%83%D1%82%D0%BD%D0%B8%D0%BA%D0%B8_%D0%A1%D0%B0%D1%82%D1%83%D1%80%D0%BD%D0%B0" title="Спутники Сатурна">83</a><sup id="cite_ref-Moons_2-0" class="reference"><a href="#cite_note-Moons-2">[2]</a></sup></span></td>
</tr>
<tr>
<th colspan="2" scope="colgroup" class="infobox-header" style="">Физические характеристики</th>
</tr>
<tr>
<th scope="row" class="plainlist">Полярное сжатие</th>
<td class="plainlist">
<span data-wikidata-property-id="P1102" class="no-wikidata">0,09796 ± 0,00018</span></td>
</tr>
<tr>
<th scope="row" class="plainlist"><a href="/wiki/%D0%AD%D0%BA%D0%B2%D0%B0%D1%82%D0%BE%D1%80" title="Экватор">Экваториальный</a> радиус</th>
<td class="plainlist">
60&nbsp;268 ± 4&nbsp;км<sup id="cite_ref-horizons_3-0" class="reference"><a href="#cite_note-horizons-3">[3]</a></sup></td>
</tr>
<tr>
<th scope="row" class="plainlist"><a href="/wiki/%D0%93%D0%B5%D0%BE%D0%B3%D1%80%D0%B0%D1%84%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B8%D0%B9_%D0%BF%D0%BE%D0%BB%D1%8E%D1%81" title="Географический полюс">Полярный</a> радиус</th>
<td class="plainlist">
54&nbsp;364 ± 10&nbsp;км<sup id="cite_ref-horizons_3-1" class="reference"><a href="#cite_note-horizons-3">[3]</a></sup></td>
</tr>
<tr>
<th scope="row" class="plainlist">Средний радиус</th>
<td class="plainlist">
58&nbsp;232 ± 6&nbsp;км<sup id="cite_ref-4" class="reference"><a href="#cite_note-4">[4]</a></sup></td>
</tr>
<tr>
<th scope="row" class="plainlist">Площадь поверхности&nbsp;(<link rel="mw-deduplicated-inline-style" href="mw-data:TemplateStyles:r117753614"><span class="ts-math"><i>S</i></span>)</th>
<td class="plainlist">
4,272⋅10<sup>10</sup> км²<sup id="cite_ref-nasafact_5-0" class="reference"><a href="#cite_note-nasafact-5">[5]</a></sup></td>
</tr>
<tr>
<th scope="row" class="plainlist">Объём&nbsp;(<link rel="mw-deduplicated-inline-style" href="mw-data:TemplateStyles:r117753614"><span class="ts-math"><i>V</i></span>)</th>
<td class="plainlist">
8,2713⋅10<sup>14</sup> км³<sup id="cite_ref-fact_6-0" class="reference"><a href="#cite_note-fact-6">[6]</a></sup></td>
</tr>
<tr>
<th scope="row" class="plainlist">Масса&nbsp;(<link rel="mw-deduplicated-inline-style" href="mw-data:TemplateStyles:r117753614"><span class="ts-math"><i>m</i></span>)</th>
<td class="plainlist">
<span data-wikidata-property-id="P2067" class="no-wikidata">5,6846⋅10<sup>26</sup> кг<sup id="cite_ref-fact_6-1" class="reference"><a href="#cite_note-fact-6">[6]</a></sup>  <br>95,2&nbsp;земных</span></td>
</tr>
<tr>
<th scope="row" class="plainlist">Средняя <a href="/wiki/%D0%9F%D0%BB%D0%BE%D1%82%D0%BD%D0%BE%D1%81%D1%82%D1%8C" title="Плотность">плотность</a>&nbsp;(<link rel="mw-deduplicated-inline-style" href="mw-data:TemplateStyles:r117753614"><span class="ts-math">ρ</span>)</th>
<td class="plainlist">
0,687 г/см³<sup id="cite_ref-horizons_3-2" class="reference"><a href="#cite_note-horizons-3">[3]</a></sup><sup id="cite_ref-fact_6-2" class="reference"><a href="#cite_note-fact-6">[6]</a></sup></td>
</tr>
<tr>
<th scope="row" class="plainlist"><a href="/wiki/%D0%A3%D1%81%D0%BA%D0%BE%D1%80%D0%B5%D0%BD%D0%B8%D0%B5_%D1%81%D0%B2%D0%BE%D0%B1%D0%BE%D0%B4%D0%BD%D0%BE%D0%B3%D0%BE_%D0%BF%D0%B0%D0%B4%D0%B5%D0%BD%D0%B8%D1%8F" title="Ускорение свободного падения">Ускорение свободного падения</a> на экваторе&nbsp;(<link rel="mw-deduplicated-inline-style" href="mw-data:TemplateStyles:r117753614"><span class="ts-math"><i>g</i></span>)</th>
<td class="plainlist">
10,44 м/с²<sup id="cite_ref-fact_6-3" class="reference"><a href="#cite_note-fact-6">[6]</a></sup></td>
</tr>
<tr>
<th scope="row" class="plainlist"><a href="/wiki/%D0%9F%D0%B5%D1%80%D0%B2%D0%B0%D1%8F_%D0%BA%D0%BE%D1%81%D0%BC%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B0%D1%8F_%D1%81%D0%BA%D0%BE%D1%80%D0%BE%D1%81%D1%82%D1%8C" title="Первая космическая скорость">Первая космическая скорость</a>&nbsp;(<link rel="mw-deduplicated-inline-style" href="mw-data:TemplateStyles:r117753614"><span class="ts-math"><i>v</i></span><sub>1</sub>)</th>
<td class="plainlist">
25,535 км/с<sup id="cite_ref-7" class="reference"><a href="#cite_note-7">[7]</a></sup></td>
</tr>
<tr>
<th scope="row" class="plainlist"><a href="/wiki/%D0%92%D1%82%D0%BE%D1%80%D0%B0%D1%8F_%D0%BA%D0%BE%D1%81%D0%BC%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B0%D1%8F_%D1%81%D0%BA%D0%BE%D1%80%D0%BE%D1%81%D1%82%D1%8C" title="Вторая космическая скорость">Вторая космическая скорость</a>&nbsp;(<link rel="mw-deduplicated-inline-style" href="mw-data:TemplateStyles:r117753614"><span class="ts-math"><i>v</i></span><sub>2</sub>)</th>
<td class="plainlist">
35,5&nbsp;км/с<sup id="cite_ref-fact_6-4" class="reference"><a href="#cite_note-fact-6">[6]</a></sup></td>
</tr>
<tr>
<th scope="row" class="plainlist">Экваториальная скорость вращения</th>
<td class="plainlist">
9,87&nbsp;км/c</td>
</tr>
<tr>
<th scope="row" class="plainlist"><a href="/wiki/%D0%9F%D0%B5%D1%80%D0%B8%D0%BE%D0%B4_%D0%B2%D1%80%D0%B0%D1%89%D0%B5%D0%BD%D0%B8%D1%8F" title="Период вращения">Период вращения</a>&nbsp;(<link rel="mw-deduplicated-inline-style" href="mw-data:TemplateStyles:r117753614"><span class="ts-math"><i>T</i></span>)</th>
<td class="plainlist">
10 ч 32 мин 45 с ± 46 с<sup id="cite_ref-nature2015_8-0" class="reference"><a href="#cite_note-nature2015-8">[8]</a></sup><sup id="cite_ref-Лента.ру_9-0" class="reference"><a href="#cite_note-Лента.ру-9">[9]</a></sup></td>
</tr>
<tr>
<th scope="row" class="plainlist"><a href="/wiki/%D0%9D%D0%B0%D0%BA%D0%BB%D0%BE%D0%BD_%D0%BE%D1%81%D0%B8_%D0%B2%D1%80%D0%B0%D1%89%D0%B5%D0%BD%D0%B8%D1%8F" title="Наклон оси вращения">Наклон оси</a></th>
<td class="plainlist">
26,73°<sup id="cite_ref-fact_6-5" class="reference"><a href="#cite_note-fact-6">[6]</a></sup></td>
</tr>
<tr>
<th scope="row" class="plainlist"><a href="/wiki/%D0%A1%D0%BA%D0%BB%D0%BE%D0%BD%D0%B5%D0%BD%D0%B8%D0%B5_(%D0%B0%D1%81%D1%82%D1%80%D0%BE%D0%BD%D0%BE%D0%BC%D0%B8%D1%8F)" title="Склонение (астрономия)">Склонение</a> северного полюса&nbsp;(<link rel="mw-deduplicated-inline-style" href="mw-data:TemplateStyles:r117753614"><span class="ts-math">δ</span>)</th>
<td class="plainlist">
83,537°</td>
</tr>
<tr>
<th scope="row" class="plainlist"><a href="/wiki/%D0%90%D0%BB%D1%8C%D0%B1%D0%B5%D0%B4%D0%BE" title="Альбедо">Альбедо</a></th>
<td class="plainlist">
0,342 (<a href="/wiki/%D0%90%D0%BB%D1%8C%D0%B1%D0%B5%D0%B4%D0%BE_%D0%91%D0%BE%D0%BD%D0%B4%D0%B0" class="mw-redirect" title="Альбедо Бонда">альбедо Бонда</a>)<br>0,47 (<a href="/wiki/%D0%93%D0%B5%D0%BE%D0%BC%D0%B5%D1%82%D1%80%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%BE%D0%B5_%D0%B0%D0%BB%D1%8C%D0%B1%D0%B5%D0%B4%D0%BE" class="mw-redirect" title="Геометрическое альбедо">геом. альбедо</a>)<sup id="cite_ref-fact_6-6" class="reference"><a href="#cite_note-fact-6">[6]</a></sup></td>
</tr>
<tr>
<th scope="row" class="plainlist"><a href="/wiki/%D0%92%D0%B8%D0%B4%D0%B8%D0%BC%D0%B0%D1%8F_%D0%B7%D0%B2%D1%91%D0%B7%D0%B4%D0%BD%D0%B0%D1%8F_%D0%B2%D0%B5%D0%BB%D0%B8%D1%87%D0%B8%D0%BD%D0%B0" title="Видимая звёздная величина">Видимая звёздная величина</a></th>
<td class="plainlist">
<span data-wikidata-property-id="P1215" class="no-wikidata">от +1,47 до −0,24<sup id="cite_ref-magnitude_10-0" class="reference"><a href="#cite_note-magnitude-10">[10]</a></sup></span></td>
</tr>
<tr>
<th scope="row" class="plainlist"><a href="/wiki/%D0%90%D0%B1%D1%81%D0%BE%D0%BB%D1%8E%D1%82%D0%BD%D0%B0%D1%8F_%D0%B7%D0%B2%D1%91%D0%B7%D0%B4%D0%BD%D0%B0%D1%8F_%D0%B2%D0%B5%D0%BB%D0%B8%D1%87%D0%B8%D0%BD%D0%B0" title="Абсолютная звёздная величина">Абсолютная звёздная величина</a></th>
<td class="plainlist">
<span data-wikidata-property-id="P1457" class="no-wikidata">-8,9 m</span></td>
</tr>
<tr>
<th scope="row" class="plainlist"><a href="/wiki/%D0%A3%D0%B3%D0%BB%D0%BE%D0%B2%D0%BE%D0%B9_%D0%B4%D0%B8%D0%B0%D0%BC%D0%B5%D1%82%D1%80" class="mw-redirect" title="Угловой диаметр">Угловой диаметр</a></th>
<td class="plainlist">
14,5"—20,1"</td>
</tr>
<tr>
<th colspan="2" scope="colgroup" class="infobox-header" style="">Температура</th>
</tr>
<tr>
<th scope="row" class="plainlist">&nbsp;</th>
<td class="plainlist">
<table><tbody><tr style="font-weight:bold">
<td>мин.</td>
<td>сред.</td>
<td>макс.</td>
</tr></tbody></table></td>
</tr>
<tr>
<th scope="row" class="plainlist">уровень 1 бара</th>
<td class="plainlist">
<table><tbody><tr>
<td></td>
<td>134&nbsp;K</td>
<td></td>
</tr></tbody></table></td>
</tr>
<tr>
<th scope="row" class="plainlist">0,1 бара</th>
<td class="plainlist">
<table><tbody><tr>
<td></td>
<td>84&nbsp;K</td>
<td></td>
</tr></tbody></table></td>
</tr>
<tr>
<th colspan="2" scope="colgroup" class="infobox-header" style=""><a href="/wiki/%D0%90%D1%82%D0%BC%D0%BE%D1%81%D1%84%D0%B5%D1%80%D0%B0" title="Атмосфера">Атмосфера</a></th>
</tr>
<tr>
<td colspan="2" class="plainlist" style="text-align:center;">
<div style="text-align:left"><b>Состав:</b> <div style="margin-left:1em"><table>
<tbody><tr><td>
~96&nbsp;%</td><td><a href="/wiki/%D0%92%D0%BE%D0%B4%D0%BE%D1%80%D0%BE%D0%B4" title="Водород">Водород</a> (H<sub>2</sub>)
</td></tr><tr><td>
~3&nbsp;%</td><td><a href="/wiki/%D0%93%D0%B5%D0%BB%D0%B8%D0%B9" title="Гелий">Гелий</a>
</td></tr><tr><td>
~0,4&nbsp;%</td><td><a href="/wiki/%D0%9C%D0%B5%D1%82%D0%B0%D0%BD" title="Метан">Метан</a>
</td></tr><tr><td>
~0,01&nbsp;%</td><td><a href="/wiki/%D0%90%D0%BC%D0%BC%D0%B8%D0%B0%D0%BA" title="Аммиак">Аммиак</a>
</td></tr><tr><td>
~0,01&nbsp;%</td><td><a href="/wiki/%D0%94%D0%B5%D0%B9%D1%82%D0%B5%D1%80%D0%B8%D0%B4_%D0%B2%D0%BE%D0%B4%D0%BE%D1%80%D0%BE%D0%B4%D0%B0" title="Дейтерид водорода">Дейтерид водорода</a> (HD)
</td></tr><tr><td>
~0,0007&nbsp;%</td><td><a href="/wiki/%D0%AD%D1%82%D0%B0%D0%BD" title="Этан">Этан</a>
</td></tr><tr><td>
<b>Льды</b>:</td><td>
</td></tr><tr><td>
</td><td>Аммиачные
</td></tr><tr><td>
</td><td>Водяные
</td></tr><tr><td>
</td><td>Гидросульфид аммония (NH<sub>4</sub>SH)
</td></tr></tbody></table></div></div></td>
</tr><tr><td colspan="2" class="infobox-below" style=";"><span data-wikidata-claim-id="q193$221DDF16-6333-4CF6-AF95-41E61A8DE4F5" class="wikidata-claim" data-wikidata-property-id="P373"><span class="wikidata-snak wikidata-main-snak"><a href="https://commons.wikimedia.org/wiki/Category:Saturn_(planet)" title="commons:Category:Saturn (planet)"><img alt="Логотип Викисклада" src="//upload.wikimedia.org/wikipedia/commons/thumb/4/4a/Commons-logo.svg/15px-Commons-logo.svg.png" decoding="async" width="15" height="20" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/4/4a/Commons-logo.svg/23px-Commons-logo.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/4/4a/Commons-logo.svg/30px-Commons-logo.svg.png 2x" data-file-width="1024" data-file-height="1376"></a>&nbsp;<a href="https://commons.wikimedia.org/wiki/Category:Saturn_(planet)" class="extiw" title="commons:Category:Saturn (planet)">Медиафайлы на Викискладе</a></span></span></td></tr><tr><td colspan="2" class="infobox-below" style=";"><a href="https://www.wikidata.org/wiki/Special:ItemByTitle/ruwiki/%D0%A1%D0%B0%D1%82%D1%83%D1%80%D0%BD" title="d:Special:ItemByTitle/ruwiki/Сатурн"><img alt="Логотип Викиданных" src="//upload.wikimedia.org/wikipedia/commons/thumb/e/e4/Wikidata-logo_S.svg/18px-Wikidata-logo_S.svg.png" decoding="async" width="18" height="10" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/e/e4/Wikidata-logo_S.svg/27px-Wikidata-logo_S.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/e/e4/Wikidata-logo_S.svg/36px-Wikidata-logo_S.svg.png 2x" data-file-width="1050" data-file-height="590"></a> <a href="https://www.wikidata.org/wiki/d:Special:ItemByTitle/ruwiki/%D0%A1%D0%B0%D1%82%D1%83%D1%80%D0%BD" class="extiw" title="d:d:Special:ItemByTitle/ruwiki/Сатурн">Информация в Викиданных</a>&nbsp;<sup><style data-mw-deduplicate="TemplateStyles:r113275842">.mw-parser-output .ts-comment-commentedText{border-bottom:1px dotted;cursor:help}@media(hover:none){.mw-parser-output .ts-comment-commentedText:not(.rt-commentedText){border-bottom:0;cursor:auto}}</style><span class="ts-comment-commentedText" title="Элементы карточки, которых нет в окне редактирования статьи, редактируются в Викиданных">?</span></sup></td></tr>
</tbody></table>
        </div>
            <div class="col">
                <h2>Минусы</h2>
                <div class="alert alert-danger">На поверхности планеты один газ</div>
                <br><br>
                <div class="alert alert-info">Колонизация невозможна</div>
            </div>
        </body>
        </html>
        """
    if planet_name == "Уран":
        return """
        <!doctype html>
        <html>
        <head>
            <meta charset="utf-8">
            <meta name="viewport" content="width=device-width, initial-scale=1">
            <title>Уран</title>
            <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha2/dist/css/bootstrap.min.css" rel="stylesheet"
            integrity="sha384-aFq/bzH65dt+w6FI2ooMVUpc+21e0SRygnTpmBvdBgSdnuTN7QbdgL+OapgHtvPp" crossorigin="anonymous">
            <link rel="stylesheet" type="text/css" href="../static/css/style.css"/>
        </head>
        <body>
            <div class="table">
            <div class="row">
            <div class="col">
            <table class="infobox infobox-3198f401f00aeaec" style="width:27em;" data-name="Планета"><tbody><tr><th colspan="2" scope="colgroup" class="infobox-above" style="">Уран <span data-wikidata-property-id="P367" class="no-wikidata"><a href="//commons.wikimedia.org/wiki/File:Uranus_symbol_(bold).svg?uselang=ru" class="image"><img alt="Uranus symbol (bold).svg" src="//upload.wikimedia.org/wikipedia/commons/thumb/8/8a/Uranus_symbol_%28bold%29.svg/20px-Uranus_symbol_%28bold%29.svg.png" decoding="async" width="20" height="20" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/8/8a/Uranus_symbol_%28bold%29.svg/30px-Uranus_symbol_%28bold%29.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/8/8a/Uranus_symbol_%28bold%29.svg/40px-Uranus_symbol_%28bold%29.svg.png 2x" data-file-width="15" data-file-height="15"></a></span></th></tr><tr><td colspan="2" class="" style="text-align:center;"><a href="/wiki/%D0%9F%D0%BB%D0%B0%D0%BD%D0%B5%D1%82%D0%B0" title="Планета">Планета</a></td></tr><tr><td colspan="2" class="infobox-image" style=""> <span data-wikidata-property-id="P18" class="no-wikidata"><a href="//commons.wikimedia.org/wiki/File:Uranus_as_seen_by_NASA%27s_Voyager_2_(remastered)_-_JPEG_converted.jpg?uselang=ru" class="image" title="Снимок «Вояджера-2» в натуральных цветах (1986)"><img alt="Снимок «Вояджера-2» в натуральных цветах (1986)" src="//upload.wikimedia.org/wikipedia/commons/thumb/c/c9/Uranus_as_seen_by_NASA%27s_Voyager_2_%28remastered%29_-_JPEG_converted.jpg/274px-Uranus_as_seen_by_NASA%27s_Voyager_2_%28remastered%29_-_JPEG_converted.jpg" decoding="async" width="274" height="274" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/c/c9/Uranus_as_seen_by_NASA%27s_Voyager_2_%28remastered%29_-_JPEG_converted.jpg/411px-Uranus_as_seen_by_NASA%27s_Voyager_2_%28remastered%29_-_JPEG_converted.jpg 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/c/c9/Uranus_as_seen_by_NASA%27s_Voyager_2_%28remastered%29_-_JPEG_converted.jpg/548px-Uranus_as_seen_by_NASA%27s_Voyager_2_%28remastered%29_-_JPEG_converted.jpg 2x" data-file-width="1720" data-file-height="1720"></a><br><span data-wikidata-qualifier-id="P2096" class="media-caption" style="display:block">Снимок «<a href="/wiki/%D0%92%D0%BE%D1%8F%D0%B4%D0%B6%D0%B5%D1%80-2" title="Вояджер-2">Вояджера-2</a>» в натуральных цветах (1986)</span></span> </td></tr>
<tr>
<th colspan="2" scope="colgroup" class="infobox-header" style="">Открытие</th>
</tr>
<tr>
<th scope="row" class="plainlist">Первооткрыватель</th>
<td class="plainlist">
<span data-wikidata-property-id="P61" class="no-wikidata"><a href="/wiki/%D0%93%D0%B5%D1%80%D1%88%D0%B5%D0%BB%D1%8C,_%D0%A3%D0%B8%D0%BB%D1%8C%D1%8F%D0%BC" title="Гершель, Уильям">Уильям Гершель</a></span></td>
</tr>
<tr>
<th scope="row" class="plainlist">Место открытия</th>
<td class="plainlist">
<a href="/wiki/%D0%91%D0%B0%D1%82_(%D0%90%D0%BD%D0%B3%D0%BB%D0%B8%D1%8F)" title="Бат (Англия)">Бат</a>, <a href="/wiki/%D0%92%D0%B5%D0%BB%D0%B8%D0%BA%D0%BE%D0%B1%D1%80%D0%B8%D1%82%D0%B0%D0%BD%D0%B8%D1%8F" title="Великобритания">Великобритания</a></td>
</tr>
<tr>
<th scope="row" class="plainlist">Дата открытия</th>
<td class="plainlist">
<span data-wikidata-property-id="P575" class="no-wikidata"><a href="/wiki/13_%D0%BC%D0%B0%D1%80%D1%82%D0%B0" title="13 марта">13 марта</a> <a href="/wiki/1781" class="mw-redirect" title="1781">1781</a></span></td>
</tr>
<tr>
<th scope="row" class="plainlist"><a href="/wiki/%D0%9C%D0%B5%D1%82%D0%BE%D0%B4%D1%8B_%D0%BF%D0%BE%D0%B8%D1%81%D0%BA%D0%B0_%D1%8D%D0%BA%D0%B7%D0%BE%D0%BF%D0%BB%D0%B0%D0%BD%D0%B5%D1%82" class="mw-redirect" title="Методы поиска экзопланет">Способ обнаружения</a></th>
<td class="plainlist">
прямое наблюдение</td>
</tr>
<tr>
<th colspan="2" scope="colgroup" class="infobox-header" style="">Орбитальные характеристики</th>
</tr>
<tr>
<td colspan="2" class="plainlist" style="text-align:center;">
<a href="/wiki/%D0%AD%D0%BF%D0%BE%D1%85%D0%B0_(%D0%B0%D1%81%D1%82%D1%80%D0%BE%D0%BD%D0%BE%D0%BC%D0%B8%D1%8F)" title="Эпоха (астрономия)">Эпоха</a>: <a href="/wiki/J2000" class="mw-redirect" title="J2000">J2000</a></td>
</tr>
<tr>
<th scope="row" class="plainlist"><a href="/wiki/%D0%9F%D0%B5%D1%80%D0%B8%D0%B3%D0%B5%D0%BB%D0%B8%D0%B9" title="Перигелий">Перигелий</a></th>
<td class="plainlist">
<span data-wikidata-property-id="P2244" class="no-wikidata">2 748 938 461&nbsp;<a href="/wiki/%D0%9A%D0%B8%D0%BB%D0%BE%D0%BC%D0%B5%D1%82%D1%80" title="Километр">км</a><br>18,375&nbsp;518&nbsp;63 <a href="/wiki/%D0%90%D1%81%D1%82%D1%80%D0%BE%D0%BD%D0%BE%D0%BC%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B0%D1%8F_%D0%B5%D0%B4%D0%B8%D0%BD%D0%B8%D1%86%D0%B0" title="Астрономическая единица">а.е.</a></span></td>
</tr>
<tr>
<th scope="row" class="plainlist"><a href="/wiki/%D0%90%D1%84%D0%B5%D0%BB%D0%B8%D0%B9" title="Афелий">Афелий</a></th>
<td class="plainlist">
<span data-wikidata-property-id="P2243" class="no-wikidata">3 004 419 704&nbsp;<a href="/wiki/%D0%9A%D0%B8%D0%BB%D0%BE%D0%BC%D0%B5%D1%82%D1%80" title="Километр">км</a><br>20,083&nbsp;305&nbsp;26&nbsp;<a href="/wiki/%D0%90%D1%81%D1%82%D1%80%D0%BE%D0%BD%D0%BE%D0%BC%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B0%D1%8F_%D0%B5%D0%B4%D0%B8%D0%BD%D0%B8%D1%86%D0%B0" title="Астрономическая единица">а.е.</a></span></td>
</tr>
<tr>
<th scope="row" class="plainlist"><a href="/wiki/%D0%91%D0%BE%D0%BB%D1%8C%D1%88%D0%B0%D1%8F_%D0%BF%D0%BE%D0%BB%D1%83%D0%BE%D1%81%D1%8C" title="Большая полуось">Большая полуось</a>&nbsp;(<style data-mw-deduplicate="TemplateStyles:r117753614">.mw-parser-output .ts-math{white-space:nowrap;font-family:times,serif,palatino linotype,new athena unicode,athena,gentium,code2000;font-size:120%}</style><span class="ts-math"><i>a</i></span>)</th>
<td class="plainlist">
<span data-wikidata-property-id="P2233" class="no-wikidata">2 876 679 082&nbsp;<a href="/wiki/%D0%9A%D0%B8%D0%BB%D0%BE%D0%BC%D0%B5%D1%82%D1%80" title="Километр">км</a><br>19,229&nbsp;411&nbsp;95 <a href="/wiki/%D0%90%D1%81%D1%82%D1%80%D0%BE%D0%BD%D0%BE%D0%BC%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B0%D1%8F_%D0%B5%D0%B4%D0%B8%D0%BD%D0%B8%D1%86%D0%B0" title="Астрономическая единица">а.е.</a></span></td>
</tr>
<tr>
<th scope="row" class="plainlist"><a href="/wiki/%D0%AD%D0%BA%D1%81%D1%86%D0%B5%D0%BD%D1%82%D1%80%D0%B8%D1%81%D0%B8%D1%82%D0%B5%D1%82_%D0%BE%D1%80%D0%B1%D0%B8%D1%82%D1%8B" title="Эксцентриситет орбиты">Эксцентриситет орбиты</a>&nbsp;(<link rel="mw-deduplicated-inline-style" href="mw-data:TemplateStyles:r117753614"><span class="ts-math"><i>e</i></span>)</th>
<td class="plainlist">
<span data-wikidata-property-id="P1096" class="no-wikidata">0,044&nbsp;405&nbsp;586</span></td>
</tr>
<tr>
<th scope="row" class="plainlist"><a href="/wiki/%D0%A1%D0%B8%D0%B4%D0%B5%D1%80%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B8%D0%B9_%D0%BF%D0%B5%D1%80%D0%B8%D0%BE%D0%B4" title="Сидерический период">Сидерический период</a> обращения</th>
<td class="plainlist">
<span data-wikidata-property-id="P2146" class="no-wikidata">30 685,4 земных суток или<br>84,01&nbsp;года<sup id="cite_ref-planet_years_1-0" class="reference"><a href="#cite_note-planet_years-1">[1]</a></sup></span></td>
</tr>
<tr>
<th scope="row" class="plainlist"><a href="/wiki/%D0%A1%D0%B8%D0%BD%D0%BE%D0%B4%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B8%D0%B9_%D0%BF%D0%B5%D1%80%D0%B8%D0%BE%D0%B4" title="Синодический период">Синодический период</a> обращения</th>
<td class="plainlist">
<span data-wikidata-property-id="P4341" class="no-wikidata">369,66&nbsp;дней<sup id="cite_ref-fact_2-0" class="reference"><a href="#cite_note-fact-2">[2]</a></sup></span></td>
</tr>
<tr>
<th scope="row" class="plainlist"><a href="/wiki/%D0%9E%D1%80%D0%B1%D0%B8%D1%82%D0%B0%D0%BB%D1%8C%D0%BD%D0%B0%D1%8F_%D1%81%D0%BA%D0%BE%D1%80%D0%BE%D1%81%D1%82%D1%8C" title="Орбитальная скорость">Орбитальная скорость</a>&nbsp;(<link rel="mw-deduplicated-inline-style" href="mw-data:TemplateStyles:r117753614"><span class="ts-math"><i>v</i></span>)</th>
<td class="plainlist">
6,81&nbsp;км/с<sup id="cite_ref-fact_2-1" class="reference"><a href="#cite_note-fact-2">[2]</a></sup></td>
</tr>
<tr>
<th scope="row" class="plainlist"><a href="/wiki/%D0%A1%D1%80%D0%B5%D0%B4%D0%BD%D1%8F%D1%8F_%D0%B0%D0%BD%D0%BE%D0%BC%D0%B0%D0%BB%D0%B8%D1%8F" class="mw-redirect" title="Средняя аномалия">Средняя аномалия</a>&nbsp;(<link rel="mw-deduplicated-inline-style" href="mw-data:TemplateStyles:r117753614"><span class="ts-math"><i>M<sub>o</sub></i></span>)</th>
<td class="plainlist">
142,955717°</td>
</tr>
<tr>
<th scope="row" class="plainlist"><a href="/wiki/%D0%9A%D0%B5%D0%BF%D0%BB%D0%B5%D1%80%D0%BE%D0%B2%D1%8B_%D1%8D%D0%BB%D0%B5%D0%BC%D0%B5%D0%BD%D1%82%D1%8B_%D0%BE%D1%80%D0%B1%D0%B8%D1%82%D1%8B#Наклонение" title="Кеплеровы элементы орбиты">Наклонение</a>&nbsp;(<link rel="mw-deduplicated-inline-style" href="mw-data:TemplateStyles:r117753614"><span class="ts-math"><i>i</i></span>)</th>
<td class="plainlist">
<span data-wikidata-property-id="P2045" class="no-wikidata">0,772556°<br>6,48°<br> относительно <a href="/wiki/%D0%A1%D0%BE%D0%BB%D0%BD%D1%86%D0%B5" title="Солнце">солнечного</a> экватора</span></td>
</tr>
<tr>
<th scope="row" class="plainlist"><a href="/wiki/%D0%94%D0%BE%D0%BB%D0%B3%D0%BE%D1%82%D0%B0_%D0%B2%D0%BE%D1%81%D1%85%D0%BE%D0%B4%D1%8F%D1%89%D0%B5%D0%B3%D0%BE_%D1%83%D0%B7%D0%BB%D0%B0" class="mw-redirect" title="Долгота восходящего узла">Долгота восходящего узла</a>&nbsp;(<link rel="mw-deduplicated-inline-style" href="mw-data:TemplateStyles:r117753614"><span class="ts-math">Ω</span>)</th>
<td class="plainlist">
<span data-wikidata-property-id="P2213" class="no-wikidata">73,989821°</span></td>
</tr>
<tr>
<th scope="row" class="plainlist"><a href="/wiki/%D0%90%D1%80%D0%B3%D1%83%D0%BC%D0%B5%D0%BD%D1%82_%D0%BF%D0%B5%D1%80%D0%B8%D1%86%D0%B5%D0%BD%D1%82%D1%80%D0%B0" class="mw-redirect" title="Аргумент перицентра">Аргумент перицентра</a>&nbsp;(<link rel="mw-deduplicated-inline-style" href="mw-data:TemplateStyles:r117753614"><span class="ts-math">ω</span>)</th>
<td class="plainlist">
<span data-wikidata-property-id="P2248" class="no-wikidata">96,541318°</span></td>
</tr>
<tr>
<th scope="row" class="plainlist">Чей спутник</th>
<td class="plainlist">
<span data-wikidata-claim-id="q324$ED331E29-69A1-4431-A28F-CD9032B30EBB" class="wikidata-claim" data-wikidata-property-id="P397"><span class="wikidata-snak wikidata-main-snak"><a href="/wiki/%D0%A1%D0%BE%D0%BB%D0%BD%D1%86%D0%B5" title="Солнце">Солнце</a></span></span></td>
</tr>
<tr>
<th scope="row" class="plainlist">Спутники</th>
<td class="plainlist">
<span data-wikidata-property-id="P398" class="no-wikidata"><a href="/wiki/%D0%A1%D0%BF%D1%83%D1%82%D0%BD%D0%B8%D0%BA%D0%B8_%D0%A3%D1%80%D0%B0%D0%BD%D0%B0" title="Спутники Урана">27</a></span></td>
</tr>
<tr>
<th colspan="2" scope="colgroup" class="infobox-header" style="">Физические характеристики</th>
</tr>
<tr>
<th scope="row" class="plainlist">Полярное сжатие</th>
<td class="plainlist">
<span data-wikidata-property-id="P1102" class="no-wikidata">0,02293</span></td>
</tr>
<tr>
<th scope="row" class="plainlist"><a href="/wiki/%D0%AD%D0%BA%D0%B2%D0%B0%D1%82%D0%BE%D1%80" title="Экватор">Экваториальный</a> радиус</th>
<td class="plainlist">
25&nbsp;559&nbsp;км<sup id="cite_ref-Seidelmann2007_3-0" class="reference"><a href="#cite_note-Seidelmann2007-3">[3]</a></sup><sup id="cite_ref-1bar_4-0" class="reference"><a href="#cite_note-1bar-4">[4]</a></sup></td>
</tr>
<tr>
<th scope="row" class="plainlist"><a href="/wiki/%D0%93%D0%B5%D0%BE%D0%B3%D1%80%D0%B0%D1%84%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B8%D0%B9_%D0%BF%D0%BE%D0%BB%D1%8E%D1%81" title="Географический полюс">Полярный</a> радиус</th>
<td class="plainlist">
24&nbsp;973&nbsp;км<sup id="cite_ref-Seidelmann2007_3-1" class="reference"><a href="#cite_note-Seidelmann2007-3">[3]</a></sup><sup id="cite_ref-1bar_4-1" class="reference"><a href="#cite_note-1bar-4">[4]</a></sup></td>
</tr>
<tr>
<th scope="row" class="plainlist">Средний радиус</th>
<td class="plainlist">
25&nbsp;362 ± 7&nbsp;км<sup id="cite_ref-5" class="reference"><a href="#cite_note-5">[5]</a></sup></td>
</tr>
<tr>
<th scope="row" class="plainlist">Площадь поверхности&nbsp;(<link rel="mw-deduplicated-inline-style" href="mw-data:TemplateStyles:r117753614"><span class="ts-math"><i>S</i></span>)</th>
<td class="plainlist">
8,1156⋅10<sup>9</sup>&nbsp;км²<sup id="cite_ref-1bar_4-2" class="reference"><a href="#cite_note-1bar-4">[4]</a></sup><sup id="cite_ref-nasafact_6-0" class="reference"><a href="#cite_note-nasafact-6">[6]</a></sup></td>
</tr>
<tr>
<th scope="row" class="plainlist">Объём&nbsp;(<link rel="mw-deduplicated-inline-style" href="mw-data:TemplateStyles:r117753614"><span class="ts-math"><i>V</i></span>)</th>
<td class="plainlist">
6,833⋅10<sup>13</sup>&nbsp;км³<sup id="cite_ref-1bar_4-3" class="reference"><a href="#cite_note-1bar-4">[4]</a></sup><sup id="cite_ref-nasauranusfact_7-0" class="reference"><a href="#cite_note-nasauranusfact-7">[7]</a></sup></td>
</tr>
<tr>
<th scope="row" class="plainlist">Масса&nbsp;(<link rel="mw-deduplicated-inline-style" href="mw-data:TemplateStyles:r117753614"><span class="ts-math"><i>m</i></span>)</th>
<td class="plainlist">
<span data-wikidata-property-id="P2067" class="no-wikidata">8,6813⋅10<sup>25</sup>&nbsp;<a href="/wiki/%D0%9A%D0%B8%D0%BB%D0%BE%D0%B3%D1%80%D0%B0%D0%BC%D0%BC" title="Килограмм">кг</a><sup id="cite_ref-nasauranusfact_7-1" class="reference"><a href="#cite_note-nasauranusfact-7">[7]</a></sup> <br>14,54&nbsp;земных</span></td>
</tr>
<tr>
<th scope="row" class="plainlist">Средняя <a href="/wiki/%D0%9F%D0%BB%D0%BE%D1%82%D0%BD%D0%BE%D1%81%D1%82%D1%8C" title="Плотность">плотность</a>&nbsp;(<link rel="mw-deduplicated-inline-style" href="mw-data:TemplateStyles:r117753614"><span class="ts-math">ρ</span>)</th>
<td class="plainlist">
1,27&nbsp;г/см³<sup id="cite_ref-fact_2-2" class="reference"><a href="#cite_note-fact-2">[2]</a></sup><sup id="cite_ref-1bar_4-4" class="reference"><a href="#cite_note-1bar-4">[4]</a></sup></td>
</tr>
<tr>
<th scope="row" class="plainlist"><a href="/wiki/%D0%A3%D1%81%D0%BA%D0%BE%D1%80%D0%B5%D0%BD%D0%B8%D0%B5_%D1%81%D0%B2%D0%BE%D0%B1%D0%BE%D0%B4%D0%BD%D0%BE%D0%B3%D0%BE_%D0%BF%D0%B0%D0%B4%D0%B5%D0%BD%D0%B8%D1%8F" title="Ускорение свободного падения">Ускорение свободного падения</a> на экваторе&nbsp;(<link rel="mw-deduplicated-inline-style" href="mw-data:TemplateStyles:r117753614"><span class="ts-math"><i>g</i></span>)</th>
<td class="plainlist">
8,87&nbsp;м/с² (0,886&nbsp;<i>g</i>)</td>
</tr>
<tr>
<th scope="row" class="plainlist"><a href="/wiki/%D0%92%D1%82%D0%BE%D1%80%D0%B0%D1%8F_%D0%BA%D0%BE%D1%81%D0%BC%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B0%D1%8F_%D1%81%D0%BA%D0%BE%D1%80%D0%BE%D1%81%D1%82%D1%8C" title="Вторая космическая скорость">Вторая космическая скорость</a>&nbsp;(<link rel="mw-deduplicated-inline-style" href="mw-data:TemplateStyles:r117753614"><span class="ts-math"><i>v</i></span><sub>2</sub>)</th>
<td class="plainlist">
21,3&nbsp;км/c<sup id="cite_ref-fact_2-3" class="reference"><a href="#cite_note-fact-2">[2]</a></sup><sup id="cite_ref-1bar_4-5" class="reference"><a href="#cite_note-1bar-4">[4]</a></sup></td>
</tr>
<tr>
<th scope="row" class="plainlist">Экваториальная скорость вращения</th>
<td class="plainlist">
2,59&nbsp;км/с<br>9&nbsp;324&nbsp;км/ч</td>
</tr>
<tr>
<th scope="row" class="plainlist"><a href="/wiki/%D0%9F%D0%B5%D1%80%D0%B8%D0%BE%D0%B4_%D0%B2%D1%80%D0%B0%D1%89%D0%B5%D0%BD%D0%B8%D1%8F" title="Период вращения">Период вращения</a>&nbsp;(<link rel="mw-deduplicated-inline-style" href="mw-data:TemplateStyles:r117753614"><span class="ts-math"><i>T</i></span>)</th>
<td class="plainlist">
0,71833&nbsp;дней<br>17&nbsp;<a href="/wiki/%D0%A7%D0%B0%D1%81" title="Час">ч</a> 14&nbsp;<a href="/wiki/%D0%9C%D0%B8%D0%BD%D1%83%D1%82%D0%B0" title="Минута">мин</a> 24&nbsp;<a href="/wiki/%D0%A1%D0%B5%D0%BA%D1%83%D0%BD%D0%B4%D0%B0" title="Секунда">с</a></td>
</tr>
<tr>
<th scope="row" class="plainlist"><a href="/wiki/%D0%9D%D0%B0%D0%BA%D0%BB%D0%BE%D0%BD_%D0%BE%D1%81%D0%B8_%D0%B2%D1%80%D0%B0%D1%89%D0%B5%D0%BD%D0%B8%D1%8F" title="Наклон оси вращения">Наклон оси</a></th>
<td class="plainlist">
97,77°<sup id="cite_ref-Seidelmann2007_3-2" class="reference"><a href="#cite_note-Seidelmann2007-3">[3]</a></sup></td>
</tr>
<tr>
<th scope="row" class="plainlist"><a href="/wiki/%D0%9F%D1%80%D1%8F%D0%BC%D0%BE%D0%B5_%D0%B2%D0%BE%D1%81%D1%85%D0%BE%D0%B6%D0%B4%D0%B5%D0%BD%D0%B8%D0%B5" title="Прямое восхождение">Прямое восхождение</a> северного полюса&nbsp;(<link rel="mw-deduplicated-inline-style" href="mw-data:TemplateStyles:r117753614"><span class="ts-math">α</span>)</th>
<td class="plainlist">
17&nbsp;ч 9&nbsp;мин 15&nbsp;с<br>257,311°<sup id="cite_ref-Seidelmann2007_3-3" class="reference"><a href="#cite_note-Seidelmann2007-3">[3]</a></sup></td>
</tr>
<tr>
<th scope="row" class="plainlist"><a href="/wiki/%D0%A1%D0%BA%D0%BB%D0%BE%D0%BD%D0%B5%D0%BD%D0%B8%D0%B5_(%D0%B0%D1%81%D1%82%D1%80%D0%BE%D0%BD%D0%BE%D0%BC%D0%B8%D1%8F)" title="Склонение (астрономия)">Склонение</a> северного полюса&nbsp;(<link rel="mw-deduplicated-inline-style" href="mw-data:TemplateStyles:r117753614"><span class="ts-math">δ</span>)</th>
<td class="plainlist">
−15,175°<sup id="cite_ref-Seidelmann2007_3-4" class="reference"><a href="#cite_note-Seidelmann2007-3">[3]</a></sup></td>
</tr>
<tr>
<th scope="row" class="plainlist"><a href="/wiki/%D0%90%D0%BB%D1%8C%D0%B1%D0%B5%D0%B4%D0%BE" title="Альбедо">Альбедо</a></th>
<td class="plainlist">
0,300 (<a href="/wiki/%D0%90%D0%BB%D1%8C%D0%B1%D0%B5%D0%B4%D0%BE_%D0%91%D0%BE%D0%BD%D0%B4%D0%B0" class="mw-redirect" title="Альбедо Бонда">Бонд</a>)<br>0,51 (<a href="/wiki/%D0%93%D0%B5%D0%BE%D0%BC%D0%B5%D1%82%D1%80%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%BE%D0%B5_%D0%B0%D0%BB%D1%8C%D0%B1%D0%B5%D0%B4%D0%BE" class="mw-redirect" title="Геометрическое альбедо">геом.</a>)<sup id="cite_ref-fact_2-4" class="reference"><a href="#cite_note-fact-2">[2]</a></sup></td>
</tr>
<tr>
<th scope="row" class="plainlist"><a href="/wiki/%D0%92%D0%B8%D0%B4%D0%B8%D0%BC%D0%B0%D1%8F_%D0%B7%D0%B2%D1%91%D0%B7%D0%B4%D0%BD%D0%B0%D1%8F_%D0%B2%D0%B5%D0%BB%D0%B8%D1%87%D0%B8%D0%BD%D0%B0" title="Видимая звёздная величина">Видимая звёздная величина</a></th>
<td class="plainlist">
<span data-wikidata-property-id="P1215" class="no-wikidata">5,9<sup id="cite_ref-ephemeris_8-0" class="reference"><a href="#cite_note-ephemeris-8">[8]</a></sup>&nbsp;— 5,32<sup id="cite_ref-fact_2-5" class="reference"><a href="#cite_note-fact-2">[2]</a></sup></span></td>
</tr>
<tr>
<th scope="row" class="plainlist"><a href="/wiki/%D0%90%D0%B1%D1%81%D0%BE%D0%BB%D1%8E%D1%82%D0%BD%D0%B0%D1%8F_%D0%B7%D0%B2%D1%91%D0%B7%D0%B4%D0%BD%D0%B0%D1%8F_%D0%B2%D0%B5%D0%BB%D0%B8%D1%87%D0%B8%D0%BD%D0%B0" title="Абсолютная звёздная величина">Абсолютная звёздная величина</a></th>
<td class="plainlist">
<span data-wikidata-property-id="P1457" class="no-wikidata">-6,64</span></td>
</tr>
<tr>
<th scope="row" class="plainlist"><a href="/wiki/%D0%A3%D0%B3%D0%BB%D0%BE%D0%B2%D0%BE%D0%B9_%D0%B4%D0%B8%D0%B0%D0%BC%D0%B5%D1%82%D1%80" class="mw-redirect" title="Угловой диаметр">Угловой диаметр</a></th>
<td class="plainlist">
3,3"—4,1"<sup id="cite_ref-fact_2-6" class="reference"><a href="#cite_note-fact-2">[2]</a></sup></td>
</tr>
<tr>
<th colspan="2" scope="colgroup" class="infobox-header" style="">Температура</th>
</tr>
<tr>
<th scope="row" class="plainlist">&nbsp;</th>
<td class="plainlist">
<table><tbody><tr style="font-weight:bold">
<td>мин.</td>
<td>сред.</td>
<td>макс.</td>
</tr></tbody></table></td>
</tr>
<tr>
<th scope="row" class="plainlist">уровень 1 бара</th>
<td class="plainlist">
<table><tbody><tr>
<td></td>
<td>76&nbsp;<a href="/wiki/%D0%9A%D0%B5%D0%BB%D1%8C%D0%B2%D0%B8%D0%BD" title="Кельвин">K</a><sup id="cite_ref-Podolak1995_9-0" class="reference"><a href="#cite_note-Podolak1995-9">[9]</a></sup></td>
<td></td>
</tr></tbody></table></td>
</tr>
<tr>
<th scope="row" class="plainlist">0,1 бара (тропопауза)</th>
<td class="plainlist">
<table><tbody><tr>
<td>49 <a href="/wiki/%D0%9A%D0%B5%D0%BB%D1%8C%D0%B2%D0%B8%D0%BD" title="Кельвин">К</a><sup id="cite_ref-Lunine1993_10-0" class="reference"><a href="#cite_note-Lunine1993-10">[10]</a></sup> (−224 °C)</td>
<td>53 <a href="/wiki/%D0%9A%D0%B5%D0%BB%D1%8C%D0%B2%D0%B8%D0%BD" title="Кельвин">К</a><sup id="cite_ref-Lunine1993_10-1" class="reference"><a href="#cite_note-Lunine1993-10">[10]</a></sup> (−220 °C)</td>
<td>57 <a href="/wiki/%D0%9A%D0%B5%D0%BB%D1%8C%D0%B2%D0%B8%D0%BD" title="Кельвин">К</a><sup id="cite_ref-Lunine1993_10-2" class="reference"><a href="#cite_note-Lunine1993-10">[10]</a></sup> (−216 °C)</td>
</tr></tbody></table></td>
</tr>
<tr>
<th colspan="2" scope="colgroup" class="infobox-header" style=""><a href="/wiki/%D0%90%D1%82%D0%BC%D0%BE%D1%81%D1%84%D0%B5%D1%80%D0%B0" title="Атмосфера">Атмосфера</a></th>
</tr>
<tr>
<td colspan="2" class="plainlist" style="text-align:center;">
<div style="text-align:left"><b>Состав:</b> <div style="margin-left:1em"><table>
<tbody><tr><td>
83±3&nbsp;%</td><td><a href="/wiki/%D0%92%D0%BE%D0%B4%D0%BE%D1%80%D0%BE%D0%B4" title="Водород">Водород</a> (H<sub>2</sub>)
</td></tr><tr><td>
15±3&nbsp;%</td><td><a href="/wiki/%D0%93%D0%B5%D0%BB%D0%B8%D0%B9" title="Гелий">Гелий</a>
</td></tr><tr><td>
2,3&nbsp;%</td><td><a href="/wiki/%D0%9C%D0%B5%D1%82%D0%B0%D0%BD" title="Метан">Метан</a></td></tr><tr><td> Лёд:</td><td> <a href="/wiki/%D0%90%D0%BC%D0%BC%D0%B8%D0%B0%D0%BA" title="Аммиак">аммиачный</a><br><a href="/wiki/%D0%92%D0%BE%D0%B4%D0%B0" title="Вода">водяной</a><br><a href="/wiki/%D0%93%D0%B8%D0%B4%D1%80%D0%BE%D1%81%D1%83%D0%BB%D1%8C%D1%84%D0%B8%D0%B4_%D0%B0%D0%BC%D0%BC%D0%BE%D0%BD%D0%B8%D1%8F" title="Гидросульфид аммония">гидросульфидно-аммиачный</a><br><a href="/wiki/%D0%9C%D0%B5%D1%82%D0%B0%D0%BD" title="Метан">метановый</a>
</td></tr></tbody></table></div></div></td>
</tr><tr><td colspan="2" class="infobox-below" style=";"><span data-wikidata-claim-id="q324$C3593AC7-420F-4D73-80EE-F53F37F8CF68" class="wikidata-claim" data-wikidata-property-id="P373"><span class="wikidata-snak wikidata-main-snak"><a href="https://commons.wikimedia.org/wiki/Category:Uranus_(planet)" title="commons:Category:Uranus (planet)"><img alt="Логотип Викисклада" src="//upload.wikimedia.org/wikipedia/commons/thumb/4/4a/Commons-logo.svg/15px-Commons-logo.svg.png" decoding="async" width="15" height="20" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/4/4a/Commons-logo.svg/23px-Commons-logo.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/4/4a/Commons-logo.svg/30px-Commons-logo.svg.png 2x" data-file-width="1024" data-file-height="1376"></a>&nbsp;<a href="https://commons.wikimedia.org/wiki/Category:Uranus_(planet)" class="extiw" title="commons:Category:Uranus (planet)">Медиафайлы на Викискладе</a></span></span></td></tr><tr><td colspan="2" class="infobox-below" style=";"><a href="https://www.wikidata.org/wiki/Special:ItemByTitle/ruwiki/%D0%A3%D1%80%D0%B0%D0%BD_(%D0%BF%D0%BB%D0%B0%D0%BD%D0%B5%D1%82%D0%B0)" title="d:Special:ItemByTitle/ruwiki/Уран (планета)"><img alt="Логотип Викиданных" src="//upload.wikimedia.org/wikipedia/commons/thumb/e/e4/Wikidata-logo_S.svg/18px-Wikidata-logo_S.svg.png" decoding="async" width="18" height="10" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/e/e4/Wikidata-logo_S.svg/27px-Wikidata-logo_S.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/e/e4/Wikidata-logo_S.svg/36px-Wikidata-logo_S.svg.png 2x" data-file-width="1050" data-file-height="590"></a> <a href="https://www.wikidata.org/wiki/d:Special:ItemByTitle/ruwiki/%D0%A3%D1%80%D0%B0%D0%BD_(%D0%BF%D0%BB%D0%B0%D0%BD%D0%B5%D1%82%D0%B0)" class="extiw" title="d:d:Special:ItemByTitle/ruwiki/Уран (планета)">Информация в Викиданных</a>&nbsp;<sup><style data-mw-deduplicate="TemplateStyles:r113275842">.mw-parser-output .ts-comment-commentedText{border-bottom:1px dotted;cursor:help}@media(hover:none){.mw-parser-output .ts-comment-commentedText:not(.rt-commentedText){border-bottom:0;cursor:auto}}</style><span class="ts-comment-commentedText" title="Элементы карточки, которых нет в окне редактирования статьи, редактируются в Викиданных">?</span></sup></td></tr>
</tbody></table>
        </div>
            <div class="col">
                <h2>Минусы</h2>
                <div class="alert alert-danger">Экстремально низкая температура</div>
                <br><br>
                <div class="alert alert-info">Колонизация невозможна</div>
            </div>
        </body>
        </html>
        """
    if planet_name == "Нептун":
        return """
        <!doctype html>
        <html>
        <head>
            <meta charset="utf-8">
            <meta name="viewport" content="width=device-width, initial-scale=1">
            <title>Нептун</title>
            <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha2/dist/css/bootstrap.min.css" rel="stylesheet"
            integrity="sha384-aFq/bzH65dt+w6FI2ooMVUpc+21e0SRygnTpmBvdBgSdnuTN7QbdgL+OapgHtvPp" crossorigin="anonymous">
            <link rel="stylesheet" type="text/css" href="../static/css/style.css"/>
        </head>
        <body>
            <div class="table">
            <div class="row">
            <div class="col">
            <table class="infobox infobox-1ed5f18c87b133f7" style="width:27em;" data-name="Планета"><tbody><tr><th colspan="2" scope="colgroup" class="infobox-above" style="">Нептун <span data-wikidata-property-id="P367" class="no-wikidata"><a href="//commons.wikimedia.org/wiki/File:Neptune_symbol_(bold).svg?uselang=ru" class="image"><img alt="Neptune symbol (bold).svg" src="//upload.wikimedia.org/wikipedia/commons/thumb/d/d7/Neptune_symbol_%28bold%29.svg/20px-Neptune_symbol_%28bold%29.svg.png" decoding="async" width="20" height="20" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/d/d7/Neptune_symbol_%28bold%29.svg/30px-Neptune_symbol_%28bold%29.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/d/d7/Neptune_symbol_%28bold%29.svg/40px-Neptune_symbol_%28bold%29.svg.png 2x" data-file-width="15" data-file-height="15"></a></span></th></tr><tr><td colspan="2" class="" style="text-align:center;"><a href="/wiki/%D0%9F%D0%BB%D0%B0%D0%BD%D0%B5%D1%82%D0%B0" title="Планета">Планета</a></td></tr><tr><td colspan="2" class="infobox-image" style=""> <span data-wikidata-property-id="P18" class="no-wikidata"><a href="//commons.wikimedia.org/wiki/File:Neptune_-_Voyager_2_(29347980845)_flatten_crop.jpg?uselang=ru" class="image" title="Нептун с «Вояджера-2» (1989)"><img alt="Нептун с «Вояджера-2» (1989)" src="//upload.wikimedia.org/wikipedia/commons/thumb/6/63/Neptune_-_Voyager_2_%2829347980845%29_flatten_crop.jpg/240px-Neptune_-_Voyager_2_%2829347980845%29_flatten_crop.jpg" decoding="async" width="240" height="240" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/6/63/Neptune_-_Voyager_2_%2829347980845%29_flatten_crop.jpg/360px-Neptune_-_Voyager_2_%2829347980845%29_flatten_crop.jpg 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/6/63/Neptune_-_Voyager_2_%2829347980845%29_flatten_crop.jpg/480px-Neptune_-_Voyager_2_%2829347980845%29_flatten_crop.jpg 2x" data-file-width="1000" data-file-height="1000"></a><br><span data-wikidata-qualifier-id="P2096" class="media-caption" style="display:block">Нептун с «<a href="/wiki/%D0%92%D0%BE%D1%8F%D0%B4%D0%B6%D0%B5%D1%80-2" title="Вояджер-2">Вояджера-2</a>» (1989)</span></span> </td></tr>
<tr>
<th colspan="2" scope="colgroup" class="infobox-header" style="">Открытие</th>
</tr>
<tr>
<th scope="row" class="plainlist">Первооткрыватель</th>
<td class="plainlist">
<span data-wikidata-claim-id="q332$4B44A2BB-9EC6-440B-A519-132A0AA1804E" class="wikidata-claim" data-wikidata-property-id="P61"><span class="wikidata-snak wikidata-main-snak"><a href="/wiki/%D0%9B%D0%B5%D0%B2%D0%B5%D1%80%D1%8C%D0%B5,_%D0%A3%D1%80%D0%B1%D0%B5%D0%BD" title="Леверье, Урбен">Урбен Жан Жозеф Леверье</a></span><sup id="cite_ref-_067baf791065ba7c_1-0" class="reference"><a href="#cite_note-_067baf791065ba7c-1">[1]</a></sup></span>, <span data-wikidata-claim-id="q332$35E9E181-535B-4EC8-AA9E-163796090D8D" class="wikidata-claim" data-wikidata-property-id="P61"><span class="wikidata-snak wikidata-main-snak"><a href="/wiki/%D0%90%D0%B4%D0%B0%D0%BC%D1%81,_%D0%94%D0%B6%D0%BE%D0%BD_%D0%9A%D1%83%D1%87" title="Адамс, Джон Куч">Джон Куч Адамс</a></span><sup id="cite_ref-_067baf791065ba7c_1-1" class="reference"><a href="#cite_note-_067baf791065ba7c-1">[1]</a></sup></span>, <span data-wikidata-claim-id="q332$78315836-8EAD-4F5E-AC63-7DB34990E852" class="wikidata-claim" data-wikidata-property-id="P61"><span class="wikidata-snak wikidata-main-snak"><a href="/wiki/%D0%93%D0%B0%D0%BB%D0%BB%D0%B5,_%D0%98%D0%BE%D0%B3%D0%B0%D0%BD%D0%BD_%D0%93%D0%BE%D1%82%D1%82%D1%84%D1%80%D0%B8%D0%B4" title="Галле, Иоганн Готтфрид">Иоганн Готтфрид Галле</a></span><sup id="cite_ref-_067baf791065ba7c_1-2" class="reference"><a href="#cite_note-_067baf791065ba7c-1">[1]</a></sup></span> и <span data-wikidata-claim-id="Q332$50B01B3B-E5F1-4810-95E1-2A26F177F819" class="wikidata-claim" data-wikidata-property-id="P61"><span class="wikidata-snak wikidata-main-snak"><a href="/wiki/%D0%94%E2%80%99%D0%90%D1%80%D1%80%D0%B5,_%D0%93%D0%B5%D0%BD%D1%80%D0%B8%D1%85_%D0%9B%D1%83%D0%B8" title="Д’Арре, Генрих Луи">Генрих Луи д’Арре</a></span></span></td>
</tr>
<tr>
<th scope="row" class="plainlist">Место открытия</th>
<td class="plainlist">
<a href="/wiki/%D0%91%D0%B5%D1%80%D0%BB%D0%B8%D0%BD" title="Берлин">Берлин</a>, <a href="/wiki/%D0%93%D0%B5%D1%80%D0%BC%D0%B0%D0%BD%D0%B8%D1%8F" title="Германия">Германия</a></td>
</tr>
<tr>
<th scope="row" class="plainlist">Дата открытия</th>
<td class="plainlist">
<span data-wikidata-property-id="P575" class="no-wikidata"><a href="/wiki/23_%D1%81%D0%B5%D0%BD%D1%82%D1%8F%D0%B1%D1%80%D1%8F" title="23 сентября">23 сентября</a> <a href="/wiki/1846" class="mw-redirect" title="1846">1846</a><sup id="cite_ref-Hamilton_2-0" class="reference"><a href="#cite_note-Hamilton-2">[2]</a></sup></span></td>
</tr>
<tr>
<th scope="row" class="plainlist"><a href="/wiki/%D0%9C%D0%B5%D1%82%D0%BE%D0%B4%D1%8B_%D0%BF%D0%BE%D0%B8%D1%81%D0%BA%D0%B0_%D1%8D%D0%BA%D0%B7%D0%BE%D0%BF%D0%BB%D0%B0%D0%BD%D0%B5%D1%82" class="mw-redirect" title="Методы поиска экзопланет">Способ обнаружения</a></th>
<td class="plainlist">
расчёт</td>
</tr>
<tr>
<th colspan="2" scope="colgroup" class="infobox-header" style="">Орбитальные характеристики<sup id="cite_ref-horizons_3-0" class="reference"><a href="#cite_note-horizons-3">[3]</a></sup><sup id="cite_ref-4" class="reference"><a href="#cite_note-4">[a]</a></sup></th>
</tr>
<tr>
<th scope="row" class="plainlist"><a href="/wiki/%D0%9F%D0%B5%D1%80%D0%B8%D0%B3%D0%B5%D0%BB%D0%B8%D0%B9" title="Перигелий">Перигелий</a></th>
<td class="plainlist">
<span data-wikidata-property-id="P2244" class="no-wikidata">4&nbsp;452&nbsp;940&nbsp;833 км<br>29,76607095 а. е.</span></td>
</tr>
<tr>
<th scope="row" class="plainlist"><a href="/wiki/%D0%90%D1%84%D0%B5%D0%BB%D0%B8%D0%B9" title="Афелий">Афелий</a></th>
<td class="plainlist">
<span data-wikidata-property-id="P2243" class="no-wikidata">4&nbsp;553&nbsp;946&nbsp;490 км<br>30,44125206 <a href="/wiki/%D0%90%D1%81%D1%82%D1%80%D0%BE%D0%BD%D0%BE%D0%BC%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B0%D1%8F_%D0%B5%D0%B4%D0%B8%D0%BD%D0%B8%D1%86%D0%B0" title="Астрономическая единица">а. е.</a></span></td>
</tr>
<tr>
<th scope="row" class="plainlist"><a href="/wiki/%D0%91%D0%BE%D0%BB%D1%8C%D1%88%D0%B0%D1%8F_%D0%BF%D0%BE%D0%BB%D1%83%D0%BE%D1%81%D1%8C" title="Большая полуось">Большая полуось</a>&nbsp;(<style data-mw-deduplicate="TemplateStyles:r117753614">.mw-parser-output .ts-math{white-space:nowrap;font-family:times,serif,palatino linotype,new athena unicode,athena,gentium,code2000;font-size:120%}</style><span class="ts-math"><i>a</i></span>)</th>
<td class="plainlist">
<span data-wikidata-property-id="P2233" class="no-wikidata">4&nbsp;503&nbsp;443&nbsp;661 км<br>30,10366151 а. е.</span></td>
</tr>
<tr>
<th scope="row" class="plainlist"><a href="/wiki/%D0%AD%D0%BA%D1%81%D1%86%D0%B5%D0%BD%D1%82%D1%80%D0%B8%D1%81%D0%B8%D1%82%D0%B5%D1%82_%D0%BE%D1%80%D0%B1%D0%B8%D1%82%D1%8B" title="Эксцентриситет орбиты">Эксцентриситет орбиты</a>&nbsp;(<link rel="mw-deduplicated-inline-style" href="mw-data:TemplateStyles:r117753614"><span class="ts-math"><i>e</i></span>)</th>
<td class="plainlist">
<span data-wikidata-property-id="P1096" class="no-wikidata">0,011214269</span></td>
</tr>
<tr>
<th scope="row" class="plainlist"><a href="/wiki/%D0%A1%D0%B8%D0%B4%D0%B5%D1%80%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B8%D0%B9_%D0%BF%D0%B5%D1%80%D0%B8%D0%BE%D0%B4" title="Сидерический период">Сидерический период</a> обращения</th>
<td class="plainlist">
<span data-wikidata-property-id="P2146" class="no-wikidata">60&nbsp;190,03<sup id="cite_ref-fact2_5-0" class="reference"><a href="#cite_note-fact2-5">[4]</a></sup> <a href="/wiki/%D0%94%D0%B5%D0%BD%D1%8C" title="День">дня</a><br>164,79 года</span></td>
</tr>
<tr>
<th scope="row" class="plainlist"><a href="/wiki/%D0%A1%D0%B8%D0%BD%D0%BE%D0%B4%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B8%D0%B9_%D0%BF%D0%B5%D1%80%D0%B8%D0%BE%D0%B4" title="Синодический период">Синодический период</a> обращения</th>
<td class="plainlist">
<span data-wikidata-property-id="P4341" class="no-wikidata">367,49 дня<sup id="cite_ref-fact_6-0" class="reference"><a href="#cite_note-fact-6">[5]</a></sup></span></td>
</tr>
<tr>
<th scope="row" class="plainlist"><a href="/wiki/%D0%9E%D1%80%D0%B1%D0%B8%D1%82%D0%B0%D0%BB%D1%8C%D0%BD%D0%B0%D1%8F_%D1%81%D0%BA%D0%BE%D1%80%D0%BE%D1%81%D1%82%D1%8C" title="Орбитальная скорость">Орбитальная скорость</a>&nbsp;(<link rel="mw-deduplicated-inline-style" href="mw-data:TemplateStyles:r117753614"><span class="ts-math"><i>v</i></span>)</th>
<td class="plainlist">
<p>5,4349 км/с<sup id="cite_ref-fact_6-1" class="reference"><a href="#cite_note-fact-6">[5]</a></sup>
</p>
19 566 км/ч</td>
</tr>
<tr>
<th scope="row" class="plainlist"><a href="/wiki/%D0%A1%D1%80%D0%B5%D0%B4%D0%BD%D1%8F%D1%8F_%D0%B0%D0%BD%D0%BE%D0%BC%D0%B0%D0%BB%D0%B8%D1%8F" class="mw-redirect" title="Средняя аномалия">Средняя аномалия</a>&nbsp;(<link rel="mw-deduplicated-inline-style" href="mw-data:TemplateStyles:r117753614"><span class="ts-math"><i>M<sub>o</sub></i></span>)</th>
<td class="plainlist">
267,767281°</td>
</tr>
<tr>
<th scope="row" class="plainlist"><a href="/wiki/%D0%9A%D0%B5%D0%BF%D0%BB%D0%B5%D1%80%D0%BE%D0%B2%D1%8B_%D1%8D%D0%BB%D0%B5%D0%BC%D0%B5%D0%BD%D1%82%D1%8B_%D0%BE%D1%80%D0%B1%D0%B8%D1%82%D1%8B#Наклонение" title="Кеплеровы элементы орбиты">Наклонение</a>&nbsp;(<link rel="mw-deduplicated-inline-style" href="mw-data:TemplateStyles:r117753614"><span class="ts-math"><i>i</i></span>)</th>
<td class="plainlist">
<span data-wikidata-property-id="P2045" class="no-wikidata">1,767975°<br>6,43° относительно <a href="/wiki/%D0%A1%D0%BE%D0%BB%D0%BD%D1%86%D0%B5" title="Солнце">солнечного</a> экватора</span></td>
</tr>
<tr>
<th scope="row" class="plainlist"><a href="/wiki/%D0%94%D0%BE%D0%BB%D0%B3%D0%BE%D1%82%D0%B0_%D0%B2%D0%BE%D1%81%D1%85%D0%BE%D0%B4%D1%8F%D1%89%D0%B5%D0%B3%D0%BE_%D1%83%D0%B7%D0%BB%D0%B0" class="mw-redirect" title="Долгота восходящего узла">Долгота восходящего узла</a>&nbsp;(<link rel="mw-deduplicated-inline-style" href="mw-data:TemplateStyles:r117753614"><span class="ts-math">Ω</span>)</th>
<td class="plainlist">
<span data-wikidata-property-id="P2213" class="no-wikidata">131,794310°</span></td>
</tr>
<tr>
<th scope="row" class="plainlist"><a href="/wiki/%D0%90%D1%80%D0%B3%D1%83%D0%BC%D0%B5%D0%BD%D1%82_%D0%BF%D0%B5%D1%80%D0%B8%D1%86%D0%B5%D0%BD%D1%82%D1%80%D0%B0" class="mw-redirect" title="Аргумент перицентра">Аргумент перицентра</a>&nbsp;(<link rel="mw-deduplicated-inline-style" href="mw-data:TemplateStyles:r117753614"><span class="ts-math">ω</span>)</th>
<td class="plainlist">
<span data-wikidata-property-id="P2248" class="no-wikidata">265,646853°</span></td>
</tr>
<tr>
<th scope="row" class="plainlist">Чей спутник</th>
<td class="plainlist">
<span data-wikidata-property-id="P397" class="no-wikidata">Солнца</span></td>
</tr>
<tr>
<th scope="row" class="plainlist">Спутники</th>
<td class="plainlist">
<span data-wikidata-property-id="P398" class="no-wikidata"><a href="/wiki/%D0%A1%D0%BF%D1%83%D1%82%D0%BD%D0%B8%D0%BA%D0%B8_%D0%9D%D0%B5%D0%BF%D1%82%D1%83%D0%BD%D0%B0" title="Спутники Нептуна">14</a></span></td>
</tr>
<tr>
<th colspan="2" scope="colgroup" class="infobox-header" style="">Физические характеристики</th>
</tr>
<tr>
<th scope="row" class="plainlist">Полярное сжатие</th>
<td class="plainlist">
<span data-wikidata-property-id="P1102" class="no-wikidata">0,0171 ± 0,0013</span></td>
</tr>
<tr>
<th scope="row" class="plainlist"><a href="/wiki/%D0%AD%D0%BA%D0%B2%D0%B0%D1%82%D0%BE%D1%80" title="Экватор">Экваториальный</a> радиус</th>
<td class="plainlist">
24 764 ± 15 км<sup id="cite_ref-Seidelmann2007_7-0" class="reference"><a href="#cite_note-Seidelmann2007-7">[6]</a></sup><sup id="cite_ref-1bar_8-0" class="reference"><a href="#cite_note-1bar-8">[b]</a></sup></td>
</tr>
<tr>
<th scope="row" class="plainlist"><a href="/wiki/%D0%93%D0%B5%D0%BE%D0%B3%D1%80%D0%B0%D1%84%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B8%D0%B9_%D0%BF%D0%BE%D0%BB%D1%8E%D1%81" title="Географический полюс">Полярный</a> радиус</th>
<td class="plainlist">
<span class="nowrap">24&nbsp;341 ± 30 км</span><sup id="cite_ref-Seidelmann2007_7-1" class="reference"><a href="#cite_note-Seidelmann2007-7">[6]</a></sup><sup id="cite_ref-1bar_8-1" class="reference"><a href="#cite_note-1bar-8">[b]</a></sup></td>
</tr>
<tr>
<th scope="row" class="plainlist">Средний радиус</th>
<td class="plainlist">
24&nbsp;622 ± 19&nbsp;км<sup id="cite_ref-9" class="reference"><a href="#cite_note-9">[7]</a></sup></td>
</tr>
<tr>
<th scope="row" class="plainlist">Площадь поверхности&nbsp;(<link rel="mw-deduplicated-inline-style" href="mw-data:TemplateStyles:r117753614"><span class="ts-math"><i>S</i></span>)</th>
<td class="plainlist">
7,6408⋅10<sup>9</sup> км²<sup id="cite_ref-fact2_5-1" class="reference"><a href="#cite_note-fact2-5">[4]</a></sup><sup id="cite_ref-1bar_8-2" class="reference"><a href="#cite_note-1bar-8">[b]</a></sup></td>
</tr>
<tr>
<th scope="row" class="plainlist">Объём&nbsp;(<link rel="mw-deduplicated-inline-style" href="mw-data:TemplateStyles:r117753614"><span class="ts-math"><i>V</i></span>)</th>
<td class="plainlist">
6,254⋅10<sup>13</sup> км³<sup id="cite_ref-fact_6-2" class="reference"><a href="#cite_note-fact-6">[5]</a></sup><sup id="cite_ref-1bar_8-3" class="reference"><a href="#cite_note-1bar-8">[b]</a></sup></td>
</tr>
<tr>
<th scope="row" class="plainlist">Масса&nbsp;(<link rel="mw-deduplicated-inline-style" href="mw-data:TemplateStyles:r117753614"><span class="ts-math"><i>m</i></span>)</th>
<td class="plainlist">
<span data-wikidata-property-id="P2067" class="no-wikidata">1,0243⋅10<sup>26</sup>&nbsp;<a href="/wiki/%D0%9A%D0%B8%D0%BB%D0%BE%D0%B3%D1%80%D0%B0%D0%BC%D0%BC" title="Килограмм">кг</a><sup id="cite_ref-fact_6-3" class="reference"><a href="#cite_note-fact-6">[5]</a></sup><br>17,147 земных</span></td>
</tr>
<tr>
<th scope="row" class="plainlist">Средняя <a href="/wiki/%D0%9F%D0%BB%D0%BE%D1%82%D0%BD%D0%BE%D1%81%D1%82%D1%8C" title="Плотность">плотность</a>&nbsp;(<link rel="mw-deduplicated-inline-style" href="mw-data:TemplateStyles:r117753614"><span class="ts-math">ρ</span>)</th>
<td class="plainlist">
1,638 г/см³<sup id="cite_ref-fact_6-4" class="reference"><a href="#cite_note-fact-6">[5]</a></sup><sup id="cite_ref-1bar_8-4" class="reference"><a href="#cite_note-1bar-8">[b]</a></sup></td>
</tr>
<tr>
<th scope="row" class="plainlist"><a href="/wiki/%D0%A3%D1%81%D0%BA%D0%BE%D1%80%D0%B5%D0%BD%D0%B8%D0%B5_%D1%81%D0%B2%D0%BE%D0%B1%D0%BE%D0%B4%D0%BD%D0%BE%D0%B3%D0%BE_%D0%BF%D0%B0%D0%B4%D0%B5%D0%BD%D0%B8%D1%8F" title="Ускорение свободного падения">Ускорение свободного падения</a> на экваторе&nbsp;(<link rel="mw-deduplicated-inline-style" href="mw-data:TemplateStyles:r117753614"><span class="ts-math"><i>g</i></span>)</th>
<td class="plainlist">
11,15 м/с²<sup id="cite_ref-fact_6-5" class="reference"><a href="#cite_note-fact-6">[5]</a></sup><sup id="cite_ref-1bar_8-5" class="reference"><a href="#cite_note-1bar-8">[b]</a></sup> (1,14&nbsp;<i>g</i>)</td>
</tr>
<tr>
<th scope="row" class="plainlist"><a href="/wiki/%D0%92%D1%82%D0%BE%D1%80%D0%B0%D1%8F_%D0%BA%D0%BE%D1%81%D0%BC%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B0%D1%8F_%D1%81%D0%BA%D0%BE%D1%80%D0%BE%D1%81%D1%82%D1%8C" title="Вторая космическая скорость">Вторая космическая скорость</a>&nbsp;(<link rel="mw-deduplicated-inline-style" href="mw-data:TemplateStyles:r117753614"><span class="ts-math"><i>v</i></span><sub>2</sub>)</th>
<td class="plainlist">
23,5 км/c<sup id="cite_ref-fact_6-6" class="reference"><a href="#cite_note-fact-6">[5]</a></sup><sup id="cite_ref-1bar_8-6" class="reference"><a href="#cite_note-1bar-8">[b]</a></sup></td>
</tr>
<tr>
<th scope="row" class="plainlist">Экваториальная скорость вращения</th>
<td class="plainlist">
2,68 км/с<br>9648 км/ч</td>
</tr>
<tr>
<th scope="row" class="plainlist"><a href="/wiki/%D0%9F%D0%B5%D1%80%D0%B8%D0%BE%D0%B4_%D0%B2%D1%80%D0%B0%D1%89%D0%B5%D0%BD%D0%B8%D1%8F" title="Период вращения">Период вращения</a>&nbsp;(<link rel="mw-deduplicated-inline-style" href="mw-data:TemplateStyles:r117753614"><span class="ts-math"><i>T</i></span>)</th>
<td class="plainlist">
0,6653 дня<sup id="cite_ref-10" class="reference"><a href="#cite_note-10">[8]</a></sup><br>15 ч 57 мин 59 с</td>
</tr>
<tr>
<th scope="row" class="plainlist"><a href="/wiki/%D0%9D%D0%B0%D0%BA%D0%BB%D0%BE%D0%BD_%D0%BE%D1%81%D0%B8_%D0%B2%D1%80%D0%B0%D1%89%D0%B5%D0%BD%D0%B8%D1%8F" title="Наклон оси вращения">Наклон оси</a></th>
<td class="plainlist">
28,32°<sup id="cite_ref-fact_6-7" class="reference"><a href="#cite_note-fact-6">[5]</a></sup></td>
</tr>
<tr>
<th scope="row" class="plainlist"><a href="/wiki/%D0%9F%D1%80%D1%8F%D0%BC%D0%BE%D0%B5_%D0%B2%D0%BE%D1%81%D1%85%D0%BE%D0%B6%D0%B4%D0%B5%D0%BD%D0%B8%D0%B5" title="Прямое восхождение">Прямое восхождение</a> северного полюса&nbsp;(<link rel="mw-deduplicated-inline-style" href="mw-data:TemplateStyles:r117753614"><span class="ts-math">α</span>)</th>
<td class="plainlist">
19<sup>ч</sup>&nbsp;57<sup>м</sup>&nbsp;20<sup>с</sup><sup id="cite_ref-Seidelmann2007_7-2" class="reference"><a href="#cite_note-Seidelmann2007-7">[6]</a></sup></td>
</tr>
<tr>
<th scope="row" class="plainlist"><a href="/wiki/%D0%A1%D0%BA%D0%BB%D0%BE%D0%BD%D0%B5%D0%BD%D0%B8%D0%B5_(%D0%B0%D1%81%D1%82%D1%80%D0%BE%D0%BD%D0%BE%D0%BC%D0%B8%D1%8F)" title="Склонение (астрономия)">Склонение</a> северного полюса&nbsp;(<link rel="mw-deduplicated-inline-style" href="mw-data:TemplateStyles:r117753614"><span class="ts-math">δ</span>)</th>
<td class="plainlist">
42,950°<sup id="cite_ref-Seidelmann2007_7-3" class="reference"><a href="#cite_note-Seidelmann2007-7">[6]</a></sup></td>
</tr>
<tr>
<th scope="row" class="plainlist"><a href="/wiki/%D0%90%D0%BB%D1%8C%D0%B1%D0%B5%D0%B4%D0%BE" title="Альбедо">Альбедо</a></th>
<td class="plainlist">
0,29 (<a href="/wiki/%D0%90%D0%BB%D1%8C%D0%B1%D0%B5%D0%B4%D0%BE_%D0%91%D0%BE%D0%BD%D0%B4%D0%B0" class="mw-redirect" title="Альбедо Бонда">Бонд</a>)<br>0,41 (<a href="/wiki/%D0%93%D0%B5%D0%BE%D0%BC%D0%B5%D1%82%D1%80%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%BE%D0%B5_%D0%B0%D0%BB%D1%8C%D0%B1%D0%B5%D0%B4%D0%BE" class="mw-redirect" title="Геометрическое альбедо">геом.</a>)<sup id="cite_ref-fact_6-8" class="reference"><a href="#cite_note-fact-6">[5]</a></sup></td>
</tr>
<tr>
<th scope="row" class="plainlist"><a href="/wiki/%D0%92%D0%B8%D0%B4%D0%B8%D0%BC%D0%B0%D1%8F_%D0%B7%D0%B2%D1%91%D0%B7%D0%B4%D0%BD%D0%B0%D1%8F_%D0%B2%D0%B5%D0%BB%D0%B8%D1%87%D0%B8%D0%BD%D0%B0" title="Видимая звёздная величина">Видимая звёздная величина</a></th>
<td class="plainlist">
<span data-wikidata-property-id="P1215" class="no-wikidata">8,0—7,78<sup id="cite_ref-fact_6-9" class="reference"><a href="#cite_note-fact-6">[5]</a></sup></span></td>
</tr>
<tr>
<th scope="row" class="plainlist"><a href="/wiki/%D0%A3%D0%B3%D0%BB%D0%BE%D0%B2%D0%BE%D0%B9_%D0%B4%D0%B8%D0%B0%D0%BC%D0%B5%D1%82%D1%80" class="mw-redirect" title="Угловой диаметр">Угловой диаметр</a></th>
<td class="plainlist">
2,2"—2,4"<sup id="cite_ref-fact_6-10" class="reference"><a href="#cite_note-fact-6">[5]</a></sup></td>
</tr>
<tr>
<th colspan="2" scope="colgroup" class="infobox-header" style="">Температура</th>
</tr>
<tr>
<th scope="row" class="plainlist">&nbsp;</th>
<td class="plainlist">
<table><tbody><tr style="font-weight:bold">
<td>мин.</td>
<td>сред.</td>
<td>макс.</td>
</tr></tbody></table></td>
</tr>
<tr>
<th scope="row" class="plainlist">уровень 1 бара</th>
<td class="plainlist">
<table><tbody><tr>
<td></td>
<td>72 <a href="/wiki/%D0%9A%D0%B5%D0%BB%D1%8C%D0%B2%D0%B8%D0%BD" title="Кельвин">К</a><sup id="cite_ref-fact_6-11" class="reference"><a href="#cite_note-fact-6">[5]</a></sup> (около −200 °С)</td>
<td></td>
</tr></tbody></table></td>
</tr>
<tr>
<th scope="row" class="plainlist">0,1 бара (тропопауза)</th>
<td class="plainlist">
<table><tbody><tr>
<td></td>
<td>55 К<sup id="cite_ref-fact_6-12" class="reference"><a href="#cite_note-fact-6">[5]</a></sup></td>
<td></td>
</tr></tbody></table></td>
</tr>
<tr>
<th colspan="2" scope="colgroup" class="infobox-header" style=""><a href="/wiki/%D0%90%D1%82%D0%BC%D0%BE%D1%81%D1%84%D0%B5%D1%80%D0%B0" title="Атмосфера">Атмосфера</a><sup id="cite_ref-fact_6-13" class="reference"><a href="#cite_note-fact-6">[5]</a></sup></th>
</tr>
<tr>
<td colspan="2" class="plainlist" style="text-align:center;">
<div style="text-align:left"><b>Состав:</b> <div style="margin-left:1em"><table>
<tbody><tr>
<td>80±3,2&nbsp;%</td><td><a href="/wiki/%D0%92%D0%BE%D0%B4%D0%BE%D1%80%D0%BE%D0%B4" title="Водород">водород</a> (H<sub>2</sub>)</td>
</tr><tr>
<td>19±3,2&nbsp;%</td><td><a href="/wiki/%D0%93%D0%B5%D0%BB%D0%B8%D0%B9" title="Гелий">гелий</a></td>
</tr><tr>
<td>1,5±0,5&nbsp;%</td><td><a href="/wiki/%D0%9C%D0%B5%D1%82%D0%B0%D0%BD" title="Метан">метан</a></td>
</tr><tr>
<td>~0,019&nbsp;%</td><td><a href="/wiki/%D0%94%D0%B5%D0%B9%D1%82%D0%B5%D1%80%D0%B8%D0%B4_%D0%B2%D0%BE%D0%B4%D0%BE%D1%80%D0%BE%D0%B4%D0%B0" title="Дейтерид водорода">дейтерид водорода</a> (HD)</td>
</tr><tr>
<td>~0,00015&nbsp;%</td><td><a href="/wiki/%D0%AD%D1%82%D0%B0%D0%BD" title="Этан">этан</a></td>
</tr><tr>
<td><b>Льды:</b></td><td></td>
</tr><tr>
<td></td><td><a href="/wiki/%D0%90%D0%BC%D0%BC%D0%B8%D0%B0%D0%BA" title="Аммиак">аммиачные</a></td>
</tr><tr>
<td></td><td><a href="/wiki/%D0%92%D0%BE%D0%B4%D0%B0" title="Вода">водные</a></td>
</tr><tr>
<td></td><td><a href="/wiki/%D0%93%D0%B8%D0%B4%D1%80%D0%BE%D1%81%D1%83%D0%BB%D1%8C%D1%84%D0%B8%D0%B4_%D0%B0%D0%BC%D0%BC%D0%BE%D0%BD%D0%B8%D1%8F" title="Гидросульфид аммония">гидросульфидно-аммониевые</a> (NH<sub>4</sub>SH)</td>
</tr><tr>
<td></td><td>метановые (?)</td>
</tr></tbody></table></div></div></td>
</tr><tr><td colspan="2" class="infobox-below" style=";"><span data-wikidata-claim-id="q332$94C664D9-CF24-4CB2-8092-577D9664FFBE" class="wikidata-claim" data-wikidata-property-id="P373"><span class="wikidata-snak wikidata-main-snak"><a href="https://commons.wikimedia.org/wiki/Category:Neptune_(planet)" title="commons:Category:Neptune (planet)"><img alt="Логотип Викисклада" src="//upload.wikimedia.org/wikipedia/commons/thumb/4/4a/Commons-logo.svg/15px-Commons-logo.svg.png" decoding="async" width="15" height="20" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/4/4a/Commons-logo.svg/23px-Commons-logo.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/4/4a/Commons-logo.svg/30px-Commons-logo.svg.png 2x" data-file-width="1024" data-file-height="1376"></a>&nbsp;<a href="https://commons.wikimedia.org/wiki/Category:Neptune_(planet)" class="extiw" title="commons:Category:Neptune (planet)">Медиафайлы на Викискладе</a></span></span></td></tr><tr><td colspan="2" class="infobox-below" style=";"><a href="https://www.wikidata.org/wiki/Special:ItemByTitle/ruwiki/%D0%9D%D0%B5%D0%BF%D1%82%D1%83%D0%BD" title="d:Special:ItemByTitle/ruwiki/Нептун"><img alt="Логотип Викиданных" src="//upload.wikimedia.org/wikipedia/commons/thumb/e/e4/Wikidata-logo_S.svg/18px-Wikidata-logo_S.svg.png" decoding="async" width="18" height="10" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/e/e4/Wikidata-logo_S.svg/27px-Wikidata-logo_S.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/e/e4/Wikidata-logo_S.svg/36px-Wikidata-logo_S.svg.png 2x" data-file-width="1050" data-file-height="590"></a> <a href="https://www.wikidata.org/wiki/d:Special:ItemByTitle/ruwiki/%D0%9D%D0%B5%D0%BF%D1%82%D1%83%D0%BD" class="extiw" title="d:d:Special:ItemByTitle/ruwiki/Нептун">Информация в Викиданных</a>&nbsp;<sup><style data-mw-deduplicate="TemplateStyles:r113275842">.mw-parser-output .ts-comment-commentedText{border-bottom:1px dotted;cursor:help}@media(hover:none){.mw-parser-output .ts-comment-commentedText:not(.rt-commentedText){border-bottom:0;cursor:auto}}</style><span class="ts-comment-commentedText" title="Элементы карточки, которых нет в окне редактирования статьи, редактируются в Викиданных">?</span></sup></td></tr>
</tbody></table>
        </div>
            <div class="col">
                <h2>Минусы</h2>
                <div class="alert alert-danger">Экстремально низкая температура</div>
                <br><br>
                <div class="alert alert-info">Колонизация невозможна</div>
            </div>
        </body>
        </html>
        """


@app.route("/results/<nickname>/<int:level>/<float:rating>")
def results(nickname, level, rating):
    return f"""
<!doctype html>
<html>
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Bootstrap demo</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha2/dist/css/bootstrap.min.css" rel="stylesheet"
    integrity="sha384-aFq/bzH65dt+w6FI2ooMVUpc+21e0SRygnTpmBvdBgSdnuTN7QbdgL+OapgHtvPp" crossorigin="anonymous">
</head>
<body>
    <h1>Результаты отбора</h1>
    <h2>Претендента на участие в мисии {nickname}</h2>
    <div class="alert alert-success">Поздравляем! Ваш рейтинг после {level} этапа отбора составляет {rating}.</div>
    <div class="alert alert-warning">Желаем удачи!</div>
</body>
</html>
    """


if __name__ == "__main__":
    app.run(port=8080, host="127.0.0.1")
