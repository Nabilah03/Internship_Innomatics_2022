# -*- coding: utf-8 -*-
"""5. Re.start() & Re.end().ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1EkGasLexoUEUCTx-NSowY9Rg8pbef81o
"""

import re

string = input()
substring = input()

x = re.compile(substring)
y = x.search(string)

if not y: 
    print('(-1, -1)')
    
while y:
    print('({0}, {1})'.format(y.start(), y.end() - 1))
    y = x.search(string, y.start() + 1)