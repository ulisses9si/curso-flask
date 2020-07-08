from flask import render_template
from flask import Blueprint
from flask import current_app
from random import randint

bp = Blueprint("site", __name__)


@bp.route("/")
def index():
    print("entrei na funcao main")
    current_app.logger.debug("Entrei na funcao main")

    nums = [
        randint(0, 1100), 
        randint(0, 1100), 
        randint(0, 1100), 
        randint(0, 1100), 
        randint(0, 1100),
        randint(0, 1100), 
        randint(0, 1100),        
        ]

    title = "CodeFoods"
    subtitle = "Subtitulo"
    columns = [0, 1, 2, 3, 4]

    return render_template("index.html", site_name=title, site_subtitle=subtitle, numeros=nums, columns=columns)


# @bp.route("/sobre")
# def about():
#     return render_template("about.html")

@bp.route("/sobre")
def about():
    return render_template("about.html")


@bp.route("/restaurantes")
def restaurants():
    return render_template("restaurants.html")
