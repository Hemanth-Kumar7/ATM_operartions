from ATMExcept import DepositError, WithDrawError, InSuffFundError
bal=500.00
def deposit():
    damt=float(input("Enter Ur Deposit Amount:"))
    if(damt<=0):  #exception
        raise DepositError
    else:
        global bal
        bal=damt+bal
        print(" Ur Account xxxxxxx123 Credited INR:{}".format(damt))
        print("Now Ur Account xxxxxx123 Remaining INR:{}".format(bal))

def withdraw():
    global bal
    wamt=float(input("Enter the WithDraw Amount:"))
    if(wamt<=0):  #exception -2 and 0
        raise WithDrawError
    if(wamt+500>bal):  #1000+500>1000
            raise InSuffFundError
    else:
        bal=bal-wamt
        print("Ur Account xxxxxx123 is Debitted INR:{}".format(wamt))
        print("Now Ur Account xxxxxx123 Currently INR:{}".format(bal))
def balenq():
        print("Ur Account xxxxxxx123 Current INR:{}".format(bal))






