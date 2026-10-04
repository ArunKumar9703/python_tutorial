from flask import Flask, render_template, request, jsonify,json
from datetime import datetime


app = Flask(__name__)

#Returns a simple "Hello, World!" message when the root URL is accessed.
@app.route('/')
def hello():
    return "Hello, World!"
#Returns the current date and time in the format "Day_of_Week HH:MM:SS".
@app.route('/Datetime')
def get_Datetime():
    day_of_week = datetime.today().strftime('%A')
    current_time = datetime.now().strftime('%H:%M:%S')    
    return day_of_week + " " + current_time

#Given a JSON file named 'data.json', this route reads the data from the given parameter and returns it as a JSON response.
@app.route('/greet')
def greet():
    data = {
        "Name":"John Doe", 
        "Age":"30",
        "message":"Hello This is a Json Response from Flask",
          }
    return jsonify(data)
#Given a JSON file named 'data.json', this route reads the data from the Url  and returns it as a JSON response.
@app.route('/Details')
def Details():
    name = request.args.get('name')
    age = request.args.get('age')
    result = {
        "Name": name,
        "Age": age
    }
    return jsonify(result)

#Given a JSON file named 'data.json', this route writes a sample data to the file and returns it as a JSON response.
@app.route('/Data')
def Data():
    data = {
        "Name": "John Doe",
        "Age": 30,
        "City": "New York"
    }
    with open('data.json', 'w') as f:
        json.dump(data, f)
    return jsonify(data)

#Given a JSON file named 'data.json', this route reads the data from the file and returns it as a JSON response.
@app.route('/read_data')
def read_data():
    with open('data.json', 'r') as f:
        data = json.load(f)
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
