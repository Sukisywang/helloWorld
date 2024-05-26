#file name must be app.py
from flask import Flask, jsonify, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

my_app = Flask(__name__)
my_app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///test.db' # create & specify database location
db = SQLAlchemy(my_app) # initalize database 

class Todo(db.Model): # create a db model
    id = db.Column(db.Integer, primary_key=True) #set up an id column
    content = db.Column(db.String(200), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        return '<Task %r>' %self.id



@my_app.route("/")
def helloWorld():
    return "<b>my first Flask application in action!</b>"

@my_app.route('/json')
def json_example():
    return jsonify(message="Hello, JSON!")
    #return {"message": "Hello, JSON!"}  #if not using jsonify

@my_app.route('/htmlTemplate')
def indexabc():
    return render_template('index.html')  # folder name must be "templates" for render_template function to recgonize

if __name__ == '__main__':
    my_app.run(debug=True)
    # Cmd To run the app: flask run