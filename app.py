from pymongo import MongoClient
from flask import Flask, render_template, request, jsonify,json
from datetime import datetime
from flask_cors import CORS
from pymongo.errors import PyMongoError
import pymongo
import json
import os
from dotenv import load_dotenv

load_dotenv()

MONGO_URI = os.getenv('MONGO_URI')
client=pymongo.MongoClient(MONGO_URI)
db = client.my_test_database
Collection = db['flask-tutorial']

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
        "Name": "Arun Kumar",
        "Age": 30,
        "City": "India"
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

@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/Submit', methods=['POST'])
def submit(): 
    try:
        formdata = dict(request.form)
        existing_record = Collection.find({"_id": 0})
        if Collection.find_one({"name": formdata.get("name")}):
            return render_template('index.html', error=str("Data already exists in the database"))
        Collection.insert_one(formdata)
        return render_template("Success.html")
    except Exception as e:
        print(f"Error: {e}")
        return render_template('index.html', error=str(e))
    
@app.route("/Success")
def success():
    return render_template("success.html")

  
if __name__ == '__main__':
    app.run(debug=True)