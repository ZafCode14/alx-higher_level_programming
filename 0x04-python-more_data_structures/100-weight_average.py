#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    sum1 = 0
    sum2 = 0
    for i in my_list:
        sum1 += i[0] * i[1] 
    for i in my_list:
        sum2 += i[1]
    return sum1 / sum2
