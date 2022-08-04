from flask import Flask,jsonify,request
import calculation # python calculation.py
app = Flask(__name__)

@app.route('/')
def test_flask():
    print("We are testing Flask")
    return jsonify({"Message" : "Successful"})

@app.route('/emp_name')
def emp_name():
    print("Employee Name API")
    return jsonify({"Message" : "Employee Name API Successful"})




if __name__ == "__main__":
    app.run()