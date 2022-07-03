'''Write a program to find the factorial of a number using userdefined function.'''
def factorial(n):
    f=1
    for i in range(1,n+1):
        f=f*i
    return f
number=int(input("Enter number to find factorial of-"))
print("Factorial=",factorial(number))
