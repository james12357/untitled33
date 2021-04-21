'''
@author:James
'''
__all__ = ["create_2d_table", "print_2d_table"]


def create_2d_table(line, column):
    tmp = []
    for i in range(line):
        tmp.append([])
    for j in range(len(tmp)):
        for r in range(column):
            tmp[j].append([])
    return tmp


def print_2d_table(table):
    for i in table:
        print(i)
