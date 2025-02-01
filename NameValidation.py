#NameValidation()  <------- File and Module Name {HITTING OF EXCEPTION}
from NameExcept import EmptyStrError, SpaceError, InvalidNameError
def Validation(name):  #Guido Van Rossum
    if(len(name)==0):
        raise EmptyStrError
    elif(name.isspace()):
        raise SpaceError
    else:
        words=name.split()     #Guido Van Rossu7
        res=True  #valid
        for word in words:   #Guido,Van,Rossu7
            if(not word.isalpha()):
                res=False  #invalid
                break
        if(res):  #if(True) --- return name if(False) ------- it goes to else part
            return name
        else:
         raise InvalidNameError




