from NameExcept import InvalidNameError, EmptyStrError, SpaceError
from NameValidation import Validation
try:
    name=input("Enter Ur Name:")
    res=Validation(name)   #Function Call  result or exception
except InvalidNameError:
    print("Invalid Name ------ try again")
except EmptyStrError:
    print(" Ur Name should not be empty --- try again")
except SpaceError:
    print(" Don't Enter Space for Name --- try again")
else:
    print(" '{}' is Valid Name".format(res))
