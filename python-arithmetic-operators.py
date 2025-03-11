'''
https://www.hackerrank.com/challenges/python-arithmetic-operators/

The first line contains the sum of the two numbers.
The second line contains the difference of the two numbers (first - second).
The third line contains the product of the two numbers.
Example


Print the following:

8
-2
15
'''
if __name__ == '__main__':
    print("Enter two numbers: ")
    a = int(input())
    b = int(input())
    
    print(a+b)
    print(a-b)
    print(a*b)