# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

def hangman():
    import random
    
    word = ["cat", "bag", "bot", "cog"]
    
    wordind = random.randint(0,4)
    word = word[wordind]
    
    wrong = 0
    stages = ["",
              "_____     ",
              "|         ",
              "|     |   ",
              "|     o   ",
              "|    /|\  ",
              "|    / \  ",
              "|         "
              ]
    rletters = list(word)
    board = ["_"] * len(word)
    win = False
    print("Welcome to Hangman!")
    
    while wrong < len(stages) - 1:
        print("\n")
        msg = "1文字を予想してください"
        char = input(msg)
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = "$"
        else:
            wrong += 1
        print(" ".join(board))
        e = wrong + 1
        print("\n".join(stages[0:e]))
        if "_" not in board:
            print("You win!")
            print(" ".join(board))
            win = True
            break
        
    if not win:
        print("\n".join(stages[0:wrong+1]))
        print("You lose! The answer is {}.".format(word))
        
hangman()