# -*- coding: utf-8 -*-
"""4. String Validators.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1EkGasLexoUEUCTx-NSowY9Rg8pbef81o
"""

def a(s):
    for i in range(len(s)):
        if(s[i].isalnum()):
            return True;
            break;
    return False;
        
def b(s):
    for i in range(len(s)):
        if(s[i].isalpha()):
            return True;
            break;
    return False;

def c(s):
    for i in range(len(s)):
        if(s[i].isdigit()):
            return True;
            break;
    return False;

def d(s):
    for i in range(len(s)):
        if(s[i].islower()):
            return True;
            break;
    return False; 
     
def e(s):
    for i in range(len(s)):
        if(s[i].isupper()):
            return True;
            break;
    return False;

if __name__ == '__main__':
    s = input()
    x= a(s)
    y = b(s)
    nums = c(s)
    lower = d(s)
    upper = e(s)
    print(x)
    print(y)
    print(nums)
    print(lower)
    print(upper)