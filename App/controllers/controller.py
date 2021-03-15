from flask import render_template, request, redirect
from App.models.game import *
from App.models.player import *
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

@app.route('/rock/scissors')
def return_rock_win():
    return render_template('rock/scissors.html', title='RPS - The Game')

@app.route('/game', methods=['POST'])
def add_player():
    playername = request.form['name']
    new_player = Player(name= playername, choice= 0)
    create_player(new_player)

    return render_template('game.html', title='RPS - The Game')
