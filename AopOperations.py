def addop():
    print("ADDITION:")
    a=int(input("\tEnter First Number:"))
    b=int(input("\tEnter Second Number:"))
    c=a+b
    print("Sum of ({},{})={}".format(a,b,c))

def subop():
    print("SUBSTRACTION:")
    a=int(input("\tEnter First Number:"))
    b=int(input("\tEnter Second Number:"))
    c=a-b
    print("Sub of ({},{})={}".format(a,b,c))

def mulop():
    print("MULTIPLICATION:")
    a=int(input("\tEnter First Number:"))
    b=int(input("\tEnter Second Number:"))
    c=a*b
    print("Mul of ({},{})={}".format(a,b,c))

def divop():
    print("DIVISION:")
    a=int(input("\tEnter First Number:"))
    b=int(input("\tEnter Second Number:"))
    c=a/b
    print("Division of ({},{})={}".format(a,b,c))

def modop():
    print("Modulo Div (OR) Remainder:")
    a=int(input("\tEnter First Number:"))
    b=int(input("\tEnter Second Number:"))
    c=a%b
    print("Remainder of ({},{})={}".format(a,b,c))

def expop():
    print("EXPONENTIATION:")
    a=int(input("\tEnter First Number:"))
    b=int(input("\tEnter Second Number:"))
    c=a**b
    print("Square of ({},{})={}".format(a,b,c))
