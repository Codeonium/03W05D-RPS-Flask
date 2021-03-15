
from App.models.player import *
import random


player1 = Player("Duck", "rock")
player2 = Player("Rabbit", "scissors")

players = [player1, player2]

def create_player(player):
    players.append(player)

def player_one_choice(player1, choice1):
    return choice1

def player_two_choice(player2, choice2):
    return choice2

def computer_choice():
    my_choice = ['&#9994;', '&#9995;', '&#9996;']
    return(random.choices(my_choice))

#  lost