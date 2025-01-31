from AopOperations import addop,subop,mulop,divop,modop,expop
from AopMenu import menu
import sys

menu()
ch=int(input("Enter Ur Choice:"))
print("------------------------------------")
match(ch):
        case 1:
            addop()
        case 2:
            subop()
        case 3:
            mulop()
        case 4:
            divop()
        case 5:
            modop()
        case 6:
            expop()
        case 7:
            print("Thnx for using me")
            sys.exit()



