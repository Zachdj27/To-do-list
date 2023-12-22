from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

def create_app():
    app = Flask(__name__)

    return app

class Todo(db.Model):
    #id of each entry
    id = db.Column(db.Integer, primary_key=True)
    #content holds each task
    #nullable=False to disable creating empty task
    content = db.Column(db.String(200), nullable=False)
    #when task is complete
    completed = db.Column(db.Integer, default = 0)
    #bookeeping
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        #every time you make a new element, it returns a new Task and the id of the Task
        return '<Task %r>' % self.id

@app.route("/", methods=['POST', 'GET'])
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)