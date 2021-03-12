from flask import render_template, request, redirect
from App import app

@app.route('/')
def index():
    return render_template('base.html', title='RPS - The Game')

@app.route('/game')
def create_game():
    return render_template('game.html', title='RPS - The Game')

@app.route('/scores')
def return_scores():
    return render_template('scores.html', title='RPS - The Game')


