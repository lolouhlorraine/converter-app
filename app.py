from flask import Flask
from flask.templating import render_template
from controller.route import converter

def error_handler(e):
    return render_template("index.html")

app = Flask(__name__)
app.register_blueprint(converter)
app.register_error_handler(500, error_handler)
