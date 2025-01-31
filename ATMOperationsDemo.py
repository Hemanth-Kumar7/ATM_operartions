from ATMExcept import DepositError, WithDrawError, InSuffFundError
from ATMMenu import menu
from ATMOperations import deposit, withdraw,balenq
while(True):
    try:
        menu()
        ch = int(input("Enter Ur Choice:"))
        match(ch):
            case 1:
                try:
                    deposit()
                except DepositError:
                        print("Don't Deposit -Ve and Zero Amount in the account -----try again")
                except ValueError:
                    print("Dont Enter alnums,str and special symbols")
            case 2:
                try:
                    withdraw() #Function Call --- result or exception
                except WithDrawError:   #-5 and 0
                    print("Don't Enter -Ve and Zeroes for WithDraw Amount")
                except ValueError:    # h7 and &^
                    print("Dont Enter alnums,str and special symbols")
                except InSuffFundError:
                    print(" Ur Account does not have sufficient amount--- re enter the amount")
            case 3:
                balenq()
            case 4:
                print("Thnx for Using Program")

    except ValueError:
        print(" Don't enter alnums,strs and special symbols for choice---try again")











