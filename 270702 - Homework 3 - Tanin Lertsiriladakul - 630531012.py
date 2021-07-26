# -*- coding: utf-8 -*-
"""
Created on Sun Jul 18 13:44:45 2021

@author: ASUS
"""
#Game : Take X sticks from the pile
print("Take X sticks from the pile")
pile = int(input("How many sticks (N) in the pile:\t"))
print(f"There are {pile} sticks in the pile.")
sticks = int(input("Maximum stick, you can take from the pile :\t"))
name = (input("What is  your name :"))

while pile > 0 :
    #Player1 turn
    if pile == 1:
        print(f"{name}, take the last sticks. \nI, smart computor win!!!")
        break
    #player condition
    player1 = int(input("How many sticks you will take :\t"))
    a = sticks + 1
    b = sticks - sticks
    if (player1 > a ) or (player1 <= b) :
        print(f"No you take wrong number! You can take 1 to {a}")
    else:    
        pile = pile - player1
        print(f"There are {pile} sticks in the pile")

        #PC turn
        if pile == 1:
            print(f"I, smart computer, take the last sticks. \n{name} win I, smart computor, am sad T_T")
            break
        #PC condition
        if pile%(sticks + 1) == 0:
            pc = sticks
            if pile%3 == 0:
                pc = 2
        elif pile%(sticks + 1) == 1 :
            pc = sticks - 1 
        elif pile%(sticks + 1) == 2 :
            if pile == 2 :
                pc = 1
            else :
                pc = sticks - 2
        elif pile%3 == 0:
            pc = 2
        elif pile%(sticks - 1) == 1 :
            pc = sticks - 1 
        elif pile%(sticks - 1) == 2 :
            if pile == 2 :
                pc = 1
            else :
                pc = sticks - 2
        else : 
            pc = 1
        
        #output put pc turn
        pile = pile - pc
        print(f"I, smart computor, take :\t{pc} \nThere are {pile} sticks in the pile")
        