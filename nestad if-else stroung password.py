#interview
#stroung password
d=input("enter the charectar")
o=input("enter the charectar")
g=input("enter the number")  
if d=="A-Z":
    print("it is alfabet") 
    if o=="0-9":
       print("it is numrical") 
    elif g=="@#_" :
        print("it is specail charectar") 
    else:
        print("invailid") 
else:
    print(d+o+g) 
    print("strong password")                                     
