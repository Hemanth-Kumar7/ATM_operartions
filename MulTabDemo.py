#MulTabDemo.py <---------- Main Program (HANDLING OF EXCEPTIONS)
from MulTabOperation import table
from MulTabExcept import ZeroInputError,NegNumInputError
try:
    n = int(input("Enter a Number for generating Mul Table:"))
    table(n)    #Function Call ----- gives  either result or exception
    print("------------------- OR ------------------------")
    for i in range(1, 11):
        print("\t{} * {} = {}".format(n, i, n * i))
except ValueError:
    print("Don't enter alnums,strs and symbols for Mul Table:")
except ZeroInputError:
    print("Don't Enter Zero for Mul Tab:")
except NegNumInputError:
    print("Don't Enter -Ve Num for Mul Tab:")

