import numpy
'''
1. Asks the user to enter a number “x”
2. Asks the user to enter a number “y”
3. Prints out number “x”, raised to the power “y”.
4. Prints out the log (base 2) of “x”.
'''

x = int(input("enter x: "))
y = int(input("enter y: "))

print("X**y =", x**y)
print("log(x) =", numpy.log(x))