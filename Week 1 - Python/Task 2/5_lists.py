# -*- coding: utf-8 -*-
"""5. Lists.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1EkGasLexoUEUCTx-NSowY9Rg8pbef81o
"""

if __name__ == '__main__':
    N = int(input())
    list1 = [];
    for i in range(0,N):
        x = input().split();
        if x[0] == "print":
            print(list1)
        elif x[0] == "insert":
            list1.insert(int(x[1]),int(x[2]))
        elif x[0] == "remove":
            list1.remove(int(x[1]))
        elif x[0] == "pop":
            list1.pop();
        elif x[0] == "append":
            list1.append(int(x[1]))
        elif x[0] == "sort":
            list1.sort();
        else:
            list1.reverse();