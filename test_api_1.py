# import flask
from flask import Flask,jsonify,request

app = Flask(__name__)

@app.route('/')
def test_flask_1():
    print('hello world')

    return jsonify({'name':'shubham'})

if __name__=='__main':
    app.run()

# @app.route('/name')
# def name():
#     print('studebt name')
#     # return 'student name is '
#     return jsonify({'name':'shubham'})


