#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 20 19:37:29 2025

@author: xuzikang
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 12:17:46 2024

@author: Sophie.Norman
"""
def choose_move(num):
    move = ""
    while move not in ["rock", "paper", "scissors"]:
        input("player1 make your move (rock, paper, scissors): ")
    return move

outcomes = {
    "rock" : "scissors",
    "scissors" : "paper",
    "paper" : "rock"}

while True:
    player1 = choose_move(1)
    player2 = choose_move(2)
	
    winner_message = ""
    if player1 == player2:
        winner_message = "The outcome is a tie"
    elif outcomes[player1] == player2:
        winner_message="player1 wins"
        
    else:
        winner_message = "player2 wins"
        
        print(winner_message)
        again = ""
        while again not in ["y", "n"]:
            again = input("Do you want to play again? (y/n): ")
            if again == "n":
                break