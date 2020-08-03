from app import app
from flask import render_template, request, redirect
from app.modules.player import Player
from app.modules.game import players

@app.route('/')
def index():
    return render_template('index.html', title = 'Home', players = players)

@app.route('/add_player', methods = ['POST'])
def add_player():
    player_1 = request.form['player_1']
    player_2 = request.form['player_2']
    choice_player_1 = request.form['choice_player_1']
    choice_player_2 = request.form['choice_player_2']
    return redirect('/')

