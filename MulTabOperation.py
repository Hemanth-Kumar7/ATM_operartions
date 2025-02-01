#MulTabOperation <----- File and Module Name (HITTING OF EXCEPTIONS)
from MulTabExcept import ZeroInputError,NegNumInputError
def table(n):
    if(n==0):
        raise ZeroInputError
    elif(n<0):
        raise NegNumInputError
    else:
        print("="*50)
        print("Mul Table for: {}".format(n))
        print("="*50)
        for i in range(1,11):
            print("\t{} * {} = {}".format(n,i,n*i))
        print("="*50)

