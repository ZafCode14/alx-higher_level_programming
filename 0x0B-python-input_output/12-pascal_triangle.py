#!/usr/bin/python3
"""Module with a function"""


def pascal_triangle(n):
    """Function that returns a list of lists of integers"""
    if n <= 0:
        return []

    tri_list = [[1]]
    while len(tri_list) != n:
        tri = tri_list[-1]
        temp = [1]
        for i in range(len(tri) - 1):
            temp.append(tri[i] + tri[i + 1])
        temp.append(1)
        tri_list.append(temp)
    return tri_list
