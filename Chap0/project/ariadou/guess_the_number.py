# -*- coding: utf-8 -*-
import random

# 读取用户输入
def getInput(i):
    try:
        input_x = int(input(str(i + 1) + ">"))
    except ValueError:
        print ("Hey! I said number!")
        return getInput(i)
    else:
        if  input_x < 0 or input_x >= 20:
            print ("Hey! It's out of range!")
            return getInput(i)
    return input_x


print ("""
Guess the number between 0 and 20.
You have 10 chances to guess.
Good luck!
""")
answer = random.randint(0, 19)
for i in range(10):
    x = getInput(i)
    if 0 <= x < answer:
        print ("It's smaller than the answer.")
    elif x == answer:
        print ("Correct!")
        break
    else:
        print ("It's bigger than the answer.")
    if i == 9:
        print ("Oops.Game over.")
