#file name must be app.py
from flask import Flask, jsonify, render_template, url_for, request, redirect
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

#@my_app.route("/")
#def helloWorld():
 #   return "<b>my first Flask application in action!</b>"

@my_app.route('/json') #http://localhost:5000/json
def json_example():
    return jsonify(message="Hello, JSON!")
    #return {"message": "Hello, JSON!"}  #if not using jsonify

@my_app.route('/htmlTemplate')  
def indexabc():
    return render_template('index.html')  # folder name must be "templates" for render_template function to recgonize

@my_app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        #return 'hello' 
        task_content = request.form['content']
        new_task = Todo(content = task_content) #create a object inside Todo class

        try:
            db.session.add(new_task)
            db.session.commit()
            return redirect('/')
        except:
            return 'There was an issue adding your task'
              
    else:
        tasks = Todo.query.order_by(Todo.date_created).all() #list out all tasks
        return render_template('index.html', tasks=tasks) #task variable in index.html = task variable here"

@my_app.route('/delete/<int:id>')
def delete(id):
    task_to_delete = Todo.query.get_or_404(id)  #if id didn't exict, it will be 404
    
    try:
        db.session.delete(task_to_delete)
        db.session.commit()
        return redirect('/')
    except:
        return 'There was a problem deleting that task'

@my_app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    task = Todo.query.get_or_404(id)
    if request.method == 'POST':
        task.content = request.form['content'] #what is this line doing ar...

        try:
            db.session.commit()
            return redirect('/')
        except:
            return 'There was an issue updating your task'
    else:
        return render_template('update.html', task=task)

if __name__ == '__main__':
    my_app.run(debug=True)
    # Cmd To run the app: flask run:
