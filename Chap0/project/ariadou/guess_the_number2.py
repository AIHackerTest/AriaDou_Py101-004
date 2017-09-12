# -*- coding: utf-8 -*-
import random
import itertools


# 生成非0开头的全排列4位数
def createPermutation():
    permutation_raw = itertools.permutations(range(10), 4)
    # 注意这里生成的数组中包含的是元组
    permutation = list(filter(lambda x: x[0] > 0, permutation_raw))
    return permutation


# 读取用户输入
def getInput(i, permutation):
    try:
        input_x = int(input(str(i + 1) + " > "))
    except ValueError:
        print ("Hey! I said number!")
    else:
        # 将输入的4位数转化为单个数字组成的元组
        x = tuple(map(int, tuple(str(input_x))))
        # 判断一维元组是否包含在二维元组中
        if x in permutation:
            return x
        elif 1000 < input_x < 9999:
            print ("I told you we need 4 different numbers! Different!")
        else:
            print ("Hey! It's out of range!")
    return getInput(i, permutation)


print ("""
Guess four different numbers between 0 and 9.
You have 10 chances to guess.
Good luck!
""")
permutation = createPermutation()
answer = random.choice(permutation)
for i in range(10):
    A = B = 0
    x = getInput(i, permutation)
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
