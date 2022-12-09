# python program to check if given is a member of fibonacci series
import math
# A utility function that returns true if x is perfect square
def isPerfectSquare(x):
    s = int(math.sqrt(x))
    return s * s == x
# Returns true if n is a Fibonacci Number, else false
def isFibonacci(n):
    # n is Fibonacci if one of 5*n*n + 4 or 5*n*n - 4 or both
    # is a perfect square
    return isPerfectSquare(5 * n * n + 4) or isPerfectSquare(5 * n * n - 4)
# A utility function to input number which has to be cheak
def inputnum():
    i = int(input("Enter a vaild number"))
    if isFibonacci(i):
        print(i, "is valid")
    else:
        print(i, "not valid")
    determind()
# A utility to ask user to be in the program or to exit
def determind():
    s = input("Enter Yes to be in the program and No to exit")
    if s.upper() == "YES":
        inputnum()
    elif s.upper() == "NO":
        print("Thank You Have a nice day!!")
        quit()
    else:
        print("invaild input please check input")
        determind()
# Calling the determind function to start the program
i = int(input("Enter a vaild number"))
if isFibonacci(i):
    print(i, "is valid")
else:
    print(i, "not valid")
determind()