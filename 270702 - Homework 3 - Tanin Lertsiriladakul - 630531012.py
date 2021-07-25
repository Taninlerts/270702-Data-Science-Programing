# -*- coding: utf-8 -*-
"""
Created on Sun Jul 18 13:44:45 2021

@author: ASUS
"""
#Game : Take X sticks from the pile
print("Take X sticks from the pile")
pile = int(input("How many sticks (N) in the pile:\t"))
print(f"There are {pile} sticks in the pile.")
name = (input("What is  your name :"))

while pile > 0 :
    #Player1 turn
    if pile == 1:
        print(f"{name}, take the last sticks. \nI, smart computor win!!!")
        break
    #player condition
    player1 = int(input("How many sticks you will take (1 or 2):\t"))
    if (player1 > 2 ) or (player1 <= 0) :
        print("No you take wrong number! You can take 1 or 2")
    else:    
        pile = pile - player1
        print(f"There are {pile} sticks in the pile")

        #PC turn
        if pile == 1:
            print(f"I, smart computer, take the last sticks. \n{name} win I, smart computor, am sad T_T")
            break
        #PC condition
        if pile%3 == 0:
            pc = 2
            if pile == 3 :
                pc = 2
            else :
                pc = 1
        else:
            pc = 1
        
        #output put pc turn
        pile = pile - pc
        print(f"I, smart computor, take :\t{pc} \nThere are {pile} sticks in the pile")
        