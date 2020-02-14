from flask import Blueprint, render_template, redirect, url_for

home = Blueprint('home', __name__)

@home.route('/')
def honme():
    return redirect(url_for('home.index'))

@home.route('/index')
def index():
    return render_template('index.html')
