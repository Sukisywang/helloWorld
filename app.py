from flask import Flask
from flask import jsonify
app = Flask(__name__)
@app.route("/")
def helloWorld():
    return "<b>my first Flask application in action!</b>"

@app.route('/json')
def json_example():
    return jsonify(message="Hello, JSON!")
    #return {"message": "Hello, JSON!"}  #if not using jsonify

if __name__ == '__main__':
    app.run(debug=True)