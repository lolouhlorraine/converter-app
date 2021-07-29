from flask import render_template, request, Blueprint
from controller.convert import Converter

converter = Blueprint('converter', __name__)

@converter.route('/', methods= ['GET','POST'])
def decimal_to_hex():
    hex = ""
    if request.method == 'POST':
            decimal_val = int(request.form['decimal'])
            hex = Converter(abs(decimal_val)).convert_decimal()
            if decimal_val < 0:
                hex = "-" + hex
    return render_template('index.html', converted_val = hex)
    