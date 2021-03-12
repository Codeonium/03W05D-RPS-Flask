from flask import render_template, request, redirect
from App import app

@app.route('/')
def index():
    return render_template('base.html', title='RPS - The Game')
