import re
from flask import Flask,jsonify,request
import calculation # python calculation.py
import config

app = Flask(__name__)


#################################################################
###################### Addition API #############################
#################################################################
@app.route('/addition')
def addition():
    print("Addition API")
    data = request.get_json()

    print("*"*70)
    print("Data:",data)
    print("*"*70)

    a = int(data['A'])
    b = int(data['B'])
    add = calculation.get_addition(a,b)
    return jsonify({"Message" : f"Addition is {add}"})


#################################################################
################ Multiplication API #############################
#################################################################
@app.route('/multiplication')
def multiplication():
    print("multiplication API")
    # print("Hello")
    print("hello Python")
    data = request.form

    print("*"*70)
    a = eval(data['a'])
    b = eval(data['b'])
    print(f"a == {a} , b == {b}") # a = 100, b= 20
    print("*"*70)

    mul = calculation.get_multiplication(a,b)

    return jsonify({"Message" : f"Multiplication is {mul}"})


if __name__ == "__main__":
    app.run(host= '0.0.0.0', port=config.PORT_NUMBER,debug=True)