from FigMenu import menu
from Rectangle import rarea
from Triangle import tarea
from Square import sarea
from Circle import carea
import sys

menu()
ch=input("Enter Ur Choice:")
print("---------------------------------------")
match(ch):
        case "R":
            rarea()
        case "T":
            tarea()
        case "S":
            sarea()
        case "C":
            carea()
        case "E":
            print("Thnx for Utilizing my services")
            sys.exit()


