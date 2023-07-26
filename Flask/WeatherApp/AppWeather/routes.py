from flask import Flask
from . import app

@app.route('/')
@app.route('/home')
def home():
    return 'hi'