from flask import Flask
from controller.route import converter

# register blueprints from controller folder
app = Flask(__name__)
app.register_blueprint(converter)