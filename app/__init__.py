from flask import Flask, render_template

app = Flask(__name__)

app.config.from_pyfile('./config.py')

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404

# 所有对象要在注册之前初始化，否则找不到该对象

from app.home import home

app.register_blueprint(home)