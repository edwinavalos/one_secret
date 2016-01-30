from flask import Blueprint, render_template, request

mod = Blueprint('views', __name__)

@mod.route('/')
def index():
    test = "this is a test"
    return render_template('index.html', test=test)
