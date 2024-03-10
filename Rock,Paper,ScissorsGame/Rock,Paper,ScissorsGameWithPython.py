# -*- coding: utf-8 -*-
"""
Created on Sun Mar 10 23:19:33 2024

@author: Lenovo
"""

import random

u_win = 0
pc_win = 0
draw = 0
values =["rock", "paper", "scissors"]

while True:
    u_input_val = input("Type: Rock, Paper, Scissors or press Q to quite \n").lower()
    if u_input_val == "q":
        break
        
    if u_input_val not in values:
        continue
    
    # 0 - Rock, 1 - Paper, 2 - scissors
    random_number = random.randint(0,2)
    pc_guess = values[random_number]
    
    print("Computer picked:", pc_guess)
    # User Win State Check
    if u_input_val == "rock" and pc_guess == "scissors":
        print("Win")
        u_win += 1
        
    elif u_input_val == "paper" and pc_guess == "rock":
        print("Win")
        u_win += 1
       
    elif u_input_val == "scissors" and pc_guess == "paper":
        print("Win")
        u_win += 1
  
    # Draw State Check   
    elif u_input_val == "rock" and pc_guess == "rock":
        print("Draw")
        draw += 1   
       
    elif u_input_val == "paper" and pc_guess == "paper":
        print("Draw")
        draw += 1   
        
    elif u_input_val == "scissors" and pc_guess == "scissors":
        print("Draw")
        draw += 1   
    # User Lose State Check
    else: 
        print("Lose")
        pc_win += 1
    
    
print("You Won",u_win,"Times")   
print("Pc Won",pc_win,"Times")  
print("Draw",draw,"Times") 

if u_win > pc_win:
    print("YOU WON !")
elif u_win == pc_win:
    print("DRAW")
else:
    print("YOU LOST")
    

    
    