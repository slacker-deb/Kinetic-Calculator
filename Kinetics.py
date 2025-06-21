import math
def time(o):
    print("Please put all in same unit for correct result: ")
    ai=float(input("Enter the value of innitial concentration: "))
    k=float(input("Enter the rate constant: "))
    f=int(input("Type 1 if you know Final Conc or 2 if you know percentage of completion: "))
    if f==2:
        p=float(input("Enter the precentage of completion: "))
        af=ai*(100-p)/100
    else:
        af=float(input("Enter final concentration: "))
    if o!=1:
        t=((1/(o-1))*((1/(af**(o-1)))-(1/(ai**(o-1)))))/k
    else:
        t=math.log((ai/af),math.e)/k
    return t
def constant(o):
    print("Please put all in same unit for correct result: ")
    ai=float(input("Enter the value of innitial concentration: "))
    t=float(input("Enter the time: "))
    f=int(input("Type 1 if you know Final Conc or 2 if you know percentage of completion: "))
    if f==2:
        p=float(input("Enter the precentage of completion: "))
        af=ai*(100-p)/100
    else:
        af=float(input("Enter final concentration: "))
    if o!=1:
        k=((1/(o-1))*((1/(af**(o-1)))-(1/(ai**(o-1)))))/t
    else:
        k=math.log((ai/af),math.e)/t
    return k
def final_conc(o):
    print("Please put all in same unit for correct result: ")
    ai=float(input("Enter the value of innitial concentration: "))
    t=float(input("Enter the time: "))
    k=float(input("Enter the rate constant: "))
    if o!=1:
        af=(1/((k*t*(o-1))+(1/(ai**(o-1)))))**(1/(o-1))
    else:
        af=ai*(math.e**(-k*t))
    return af
def innitial_conc(o):
    print("Please put all in same unit for correct result: ")
    af=float(input("Enter the value of final concentration: "))
    t=float(input("Enter the time: "))
    k=float(input("Enter the rate constant: "))
    if o!=1:
        ai=(1/((1/(af**(o-1)))-(k*t*(o-1))))**(1/(o-1))
    else:
        ai=af*(math.e**(k*t))
    return ai
print("Hello this is a calculator to solve any kind of numeric problem of Chemistry's Chemical Kinetics")
order=int(input("Enter the order of reaction: "))
c=0
while(c!=5):
    c=int(input("Enter 1 to calculate value of time:\nEnter 2 to calculate value of rate constant:\nEnter 3 to calculate value of Final Concentration:\nEnter 4 to calculate value of Innitial Concentration:\nEnter 5 to leave:\nEnter your choice: "))
    if c==1:
        r=time(order)
        print("***** Time of completion: *****",r,"\n\n\n")
    elif c==2:
        r=constant(order)
        print("***** Rate constant of reaction: *****",r,"\n\n\n")
    elif c==3:
        r=final_conc(order)
        print("***** Final Concentration of Reactant: *****",r,"\n\n\n")
    elif c==4:
        r=innitial_conc(order)
        print("***** Innitial Concentration of Reactant: *****",r,"\n\n\n")
    else:
        print("Exiting:")