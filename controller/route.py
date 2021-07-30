from flask import render_template, request, Blueprint
from controller.convert import Converter

converter = Blueprint('converter', __name__)

@converter.route('/', methods= ['GET','POST'])
def decimal_to_hex():
    hex = ""
    if request.method == 'POST':
            decimal_val = int(request.form['decimal'])
            convert_decimal = Converter(abs(decimal_val))
            if abs(decimal_val) < 16:
                hex = convert_decimal.convert_small_decimal()            
            else:
                hex = convert_decimal.convert_big_decimal()
            if decimal_val < 0:
                hex = "-" + hex

    return render_template('index.html', converted_val = hex)
    