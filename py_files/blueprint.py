from flask import Blueprint, render_template

blueprint = Blueprint('blueprint', __name__)

@blueprint.route('/sonakshi')
def sonakshi():
    return render_template("team/sonakshi.html")

@blueprint.route('/khushi')
def khushi():
    return render_template("team/khushi.html")

@blueprint.route('/punnu')
def punnu():
    return render_template("team/punnu.html")

@blueprint.route('/shreya')
def shreya():
    return render_template("team/shreya.html")