'''
You are given a string .
Your task is to verify that  is a floating point number.

https://www.hackerrank.com/challenges/introduction-to-regex/

a valid float number must satisfy all of the following requirements:

 Number can start with +, - or . symbol.
For example:
✔
+4.50
✔
-1.0
✔
.5
✔
-.7
✔
+.4
✖
 -+4.5

 Number must contain at least  decimal value.
For example:
✖
 12.
✔
12.0  

 Number must have exactly one . symbol.
 Number must not give any exceptions when converted using .
'''
import re

def check_pattern(input_str):
    pattern = r"^[\+\-]?(\d+\.\d+|\.\d+)$"
    if re.match(pattern, input_str):
        print("True")
    else:
        print("False")

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = input()
        check_pattern(n)
    