import os
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import psycopg2



app = Flask(__name__)



ENV = 'dev'

if ENV == 'dev':
    app.debug = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:123456789@localhost/employees'
else:
    app.debug = False
    app.config['SQLALCHEMY_DATABASE_URI'] = ''

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class Employee(db.Model):
    __tablename__ = 'employees'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200))
    email = db.Column(db.String(200), unique=True)
    phone = db.Column(db.String(10))

    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone
    



@app.route('/')
def Index():
    return render_template('index.html')

@app.route('/insert', methods = ['POST'])
def insert():
 
    if request.method == 'POST':
 
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
 
 
        data = Employee(name, email, phone)
        db.session.add(data)
        db.session.commit()

        return redirect(url_for('Index'))

        



if __name__ == '__main__':
    app.run()