### Day 5 Solving Questions on hackerrank python platform


#Q1Complete the function Solve me first to compute the sum of two integers
def solveMeFirst(a,b):
 return a+b
num1 = int(input())
num2 = int(input())
res = solveMeFirst(num1,num2)
print(res)

#Q2 Alice and Bob each created one problem for HackerRank. A reviewer rates the two challenges,
#awarding points on a scale from 1 to 100 for three categories: problem clarity, originality,
#and difficulty.

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the 'compareTriplets' function below.
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b

def compareTriplets(a, b):
    score_a = 0
    score_b = 0
    for x, y in zip(a, b):
        if x > y:
            score_a += 1
        elif x < y:
            score_b += 1
    return [score_a, score_b]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

#Q3 In this challenge, you need to calculate and print the sum of elements in an array,
#  considering that some integers may be very large.

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the 'aVeryBigSum' function below.
# The function is expected to return a LONG_INTEGER.
# The function accepts LONG_INTEGER_ARRAY ar as parameter.

def aVeryBigSum(ar):
    return sum(ar)
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = aVeryBigSum(ar)

    fptr.write(str(result) + '\n')

    fptr.close()



#Q4 Given a square matrix, calculate the absolute difference between the sums of its diagonals.
#For example, the square matrix arr  is shown below:
#1 2 3
#4 5 6
#9 8 9 

#!/bin/python3

import math
import os
import random
import re
import sys
# Complete the 'diagonalDifference' function below.
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.

def diagonalDifference(arr):
    n = len(arr)
    primary = sum(arr[i][i] for i in range(n))
    secondary = sum(arr[i][n - 1 - i] for i in range(n))
    return abs(primary - secondary)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()


#Q5 Given a time in -hour AM/PM format, convert it to military (24-hour) time.

#Note: - 12:00:00AM on a 12-hour clock is 00:00:00 on a 24-hour clock.
#- 12:00:00PM on a 12-hour clock is 12:00:00 on a 24-hour clock.

#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the 'timeConversion' function below.
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.

def timeConversion(s):
    period = s[-2:]       
    hour = int(s[:2])      
    minutes_seconds = s[2:-2] 
    
    if period == "AM":
        if hour == 12:
            hour = 0
    else:
        if hour != 12:
            hour += 12
    return f"{hour:02}{minutes_seconds}"
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()