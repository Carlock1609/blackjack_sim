#! python

import random
import os

total_sims = 0
even_num = 0
odd_num = 0


def sim2():
    global even_num
    global odd_num
    global total_sims

    for i in range(1, 1001):
        if i % 2 == 0:
            print(str(i) + " even number")
            even_num += 1
        else:
            print(str(i) + " odd number")
            odd_num += 1

    print("There are " + str(even_num) + " even numbers.")
    print("There are " + str(odd_num) + " odd numbers.")


# x = 4
# y = 2
# numofdiv = 0
# if x // y != 0:
#     x // y
#     numofdiv += 1
#
# print(numofdiv)

def sim3():
    global even_num
    global odd_num
    global total_sims

    for i in range(1, 10000):
        if i % 2 == 0:
            print(str(i) + " even number")
            even_num += 1
        else:
            print(str(i) + " odd number")
            odd_num += 1

    print("There are " + str(even_num) + " even numbers.")
    print("There are " + str(odd_num) + " odd numbers.")

sim3()
