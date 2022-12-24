x=int(input("Enter the number: "))
try:
    quotient, remainder = divmod(x, 0)
    print (quotient)
except ZeroDivisionError:
    print ("You can't divide by zero!");