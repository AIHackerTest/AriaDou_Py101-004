# -*- coding: utf-8 -*-
# input的作用是把输入当作字符串处理
print ("How old are you?",)
age = input()
print ("How tall are you?",)
height = input()
print ("How much do you weigh?",)
weight = input()

print ("So, you're %r old, %r tall and %r heavy." % (
    age, height, weight
))
