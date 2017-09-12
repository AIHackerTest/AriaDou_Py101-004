# -*- coding: utf-8 -*-
import random
import re


# 生成答案
def getAnswer():
    answer = random.sample(range(10), 4)
    if answer[0] == 0:
        return getAnswer()
    return answer


# 读取用户输入
def getInput(i):
    x = input(str(i + 1) + " > ")
    if (not re.compile(r'^[1-9]\d{3}$').match(x)) or len(set(x)) < 4:
        print ("请输入开头不为0的4位数，并且每一位互不相同哟~")
        return getInput(i)
    return list(map(int, list(x)))


print ("""
Guess four different numbers between 0 and 9.
You have 10 chances to guess.
Good luck!
""")
answer = getAnswer()
for i in range(10):
    A = B = 0
    x = getInput(i)
    for n in range(4):
        if x[n] == answer[n]:
            A += 1
        elif x[n] in answer:
            B += 1
        else:
            pass
    print (str(A) + "A" + str(B) + "B")
    if A == 4:
        print ("Win!!!")
        break
    if i == 9:
        print ("Oops.Game over.")
