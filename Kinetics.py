import math
def two_rate_2_ea():
    r1=float(input("Enter the first rate constant:"))
    t1=float(input("Enter the temp of first rate constant:"))
    r2=float(input("Enter the second rate constant:"))
    t2=float(input("Enter the temp of second rate constant:"))
    e=(math.log((r2/r1),math.e)*8.314*t1*t2)/(t2-t1)
    return e
def two_rate_2_Arh_const():
    e=two_rate_2_ea()
    k=float(input("Enter rate constant:"))
    t=float(input("Enter the temp of that rate constant:"))
    a=k/(pow(math.e,((-e)/(8.314*t))))
    return a
def arh_cons():
    print("Please Put all in SI")
    e=float(input("Enter the Activation Energy: "))
    t=float(input("Enter the temperature in Kelvin: "))
    k=float(input("Enter the  rate Constant: "))
    a=k/(pow(math.e,((-e)/(8.314*t))))
    return a
def ea():
    print("Please Put all in SI")
    a=float(input("Enter the Arhenious Constant: "))
    t=float(input("Enter the temperature in Kelvin: "))
    k=float(input("Enter the  rate Constant: "))
    e=(math.log(a,math.e)-math.log(k,math.e))*8.314*t
    return e
def collision_temp():
    print("Please Put all in SI")
    e=float(input("Enter the Activation Energy: "))
    a=float(input("Enter the Arhenious Constant: "))
    k=float(input("Enter the  rate Constant: "))
    t=e/((math.log(a,math.e)-math.log(k,math.e))*8.314)
    return t

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
def time_relation(x,y):
    n=math.log(100/(100-x),math.e)/math.log(100/(100-y),math.e)
    return n
print("Hello this is a calculator to solve any kind of numeric problem of Chemistry's Chemical Kinetics\n\n Created by Slacker_Deb")
k=int(input("Press 1 if you want to calculate Rate related Items or Press 2 to Calculte Relation b/w two terms\nPress 3 to Calculate Special Cases of FOK\nPress 4 to calculate Collision Related Problem: "))
if k==1:
    c=0
    while(c!=5):
        order=int(input("Enter the order of reaction: "))
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
elif k==2:
    i=0
    while i<5:
        i=int(input("Press 1 to calculate relations b/w two different time completion\nEnter your Choice: "))
        if i==1:
            m=float(input("Enter the percentage of completion of first reaction: "))
            n=float(input("Enter the percentage of completion of second reaction: "))
            r= time_relation(m,n)
            print("Time of completion of ",m,"percentage is: ",r," times the time of completion of ",n,"percentage\n\n\n")
        else:
            print("Exiting")
elif k==4:
    j=0
    while j!=5:
        j=int(input("Enter 1 to calculate Arhenious Factor\nEnter 2 to find Activation Energy\nPress3 to Find Temp\nPress 4 to find Something using the relation b/w them\nPress 5 to Exit\nEnter your Choice: "))
        if j==1:
            r=arh_cons()
            print("Arhenious Constant is: ",r)
        elif j==2:
            r=ea()
            print("Activation Energy is: ",r)
        elif j==3:
            r=collision_temp()
            print("Temp is: ",r)
        elif j==4:
            y=0
            while y!=5:
                y=int(input("press 1 if you need to calculate Activstion energy wrt two rate constant\n Press 2 to calculate Arhenious factor from two rate consatnts:\nPress 3 to calculate One rate constant from other rate constant\nPRess 4 to calculate temperature of A rate with the help of other rate constant at different temparature:\nPress 5 to exit:  "))
                if y==1:
                    r=two_rate_2_ea()
                    print("Activation energy is: ",r)
                elif y==2:
                    r=two_rate_2_Arh_const()
                    print("Arhenious Constant is: ",r)
                elif y==5:
                    print("Exiting")
        elif j==5:
            print("Exiting...")
elif k==5:
    print("Good bye")
