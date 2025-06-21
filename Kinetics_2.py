import math
def time(o):
    print("Please put all in same unit for correct result: ")
    ai=float(input("Enter the value of innitial concentration: "))
    k=float(input("Enter the rate constant: "))
    p=float(input("Enter the precentage of completion: "))
    af=ai*(100-p)/100
    if o!=1:
        t=((1/(o-1))*((1/(af**(o-1)))-(1/(ai**(o-1)))))/k
    else:
        t=math.log((ai/af),math.e)/k
    return t
def constant(o):
    print("Please put all in same unit for correct result: ")
    ai=float(input("Enter the value of innitial concentration: "))
    t=float(input("Enter the time: "))
    p=float(input("Enter the precentage of completion: "))
    af=ai*(100-p)/100
    if o!=1:
        k=((1/(o-1))*((1/(af**(o-1)))-(1/(ai**(o-1)))))/t
    else:
        k=math.log((ai/af),math.e)/t
    return k
    


print("Hello this is a calculator to solve any kind of numeric problem of Chemistry's Chemical Kinetics")
order=int(input("Enter the order of reaction: "))
c=0
while(c!=5):
    c=int(input("Enter 1 to calculate value of time:\nEnter 2 to calculate value of rate constant:\nEnter 3 to calculate value of Final Concentration:\nEnter 4 to calculate value of Innitial Concentration:\nEnter 5 to leave:\nEnter your choice: "))
    if c==1:
        r=time(order)
        print("***** Time of completion: *****\n\n\n",r)
    elif c==2:
        r=constant(order)
        print("***** Rate constant of reaction: *****\n\n\n",r)
    else:
        print("Exiting:")
