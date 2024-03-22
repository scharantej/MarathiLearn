
# Import Flask and other necessary modules
from flask import Flask, render_template, request, redirect, url_for

# Initialize the Flask application
app = Flask(__name__)

# Define the routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/lessons')
def lessons():
    return render_template('lessons.html')

@app.route('/lesson1')
def lesson1():
    return render_template('lesson1.html')

@app.route('/exercises')
def exercises():
    return render_template('exercises.html')

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
