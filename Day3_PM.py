### Day 3 code on hackerrank python platform

# Hello World
if __name__ == '__main__':
    print("Hello, World!")

#if else



import math
import os
import random
import re
import sys
n = int(input().strip())

if n % 2 == 1:
    print("Weird")
else:
    if 2 <= n <= 5:
        print("Not Weird")
    elif 6 <= n <= 20:
        print("Weird")
    else:
        print("Not Weird")


import sys
n=int(input())
if n%2==1 or n in range(5,21):
    print("Weird")
else:
    print("Not Weird")


# 3rd Approach even odd then use
n=int(input())
if n%2!=0:
    print("Weird")
else:
    if 2<=n<=5:
        print("Not Weird")
    elif 6<=n<=20:
        print("Weird")
    else:
        print("Not Weird")

# Arithematic Operators
if __name__ == '__main__':
    a = int(input())
    b = int(input())


# Division
if __name__ == '__main__':
    a = int(input())
b = int(input())

# integer division
print(a // b)  
print(a / b)  

# Loops
if __name__ == '__main__':
    n = int(input())
    
    for i in range(n):
        print(i*i)


