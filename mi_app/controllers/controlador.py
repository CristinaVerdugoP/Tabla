from flask import Flask, render_template
from mi_app import app

@app.route('/')
def hola_mundo():
    return 'Hola Mundo!'

@app.route('/tabla')
def tabla():
    users = [
    {'first_name' : 'Michael', 'last_name' : 'Choi'},
    {'first_name' : 'John', 'last_name' : 'Supsupin'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
    return render_template("index.html", usuarios = users)