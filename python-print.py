'''
Print the list of integers from  through  as a string, without spaces.

https://www.hackerrank.com/challenges/python-print/problem
'''

if __name__ == '__main__':
    n = int(input())
    for i in range(1, n+1):
        print(i, end="")