# Importing flask module in the project
from flask import Flask, jsonify, request
from data import data

# Create an object of the Flask class
app = Flask(__name__)

# The route() function of the Flask class 
@app.route("/")
# ‘/’ URL is bound with first_flask function.
def index():
    return jsonify({
        "data": data,
        "message": "success"
    }), 200

# Define a function with different endpoint
@app.route("/planet")
def planet():
    name = request.args.get("name")
    planet_data = next(item for item in data if item['name'] == name)
    return jsonify({
        "data": planet_data,
        "message": "success"
    }), 200

# Run using debug argument
if __name__ == "__main__":
    app.run(debug=True)
