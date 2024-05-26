#file name must be app.py
from flask import Flask, jsonify, render_template, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']-'sqlite'

@app.route("/")
def helloWorld():
    return "<b>my first Flask application in action!</b>"

@app.route('/json')
def json_example():
    return jsonify(message="Hello, JSON!")
    #return {"message": "Hello, JSON!"}  #if not using jsonify

@app.route('/htmlTemplate')
def indexabc():
    return render_template('index.html')  # folder name must be "templates" for render_template function to recgonize

if __name__ == '__main__':
    app.run(debug=True)
    # CLI To run the app: flask run