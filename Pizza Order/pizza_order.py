print("welcome to the pizza delivery service.......")

size=input("what size pizza do you want? S, M or L \n").lower()
add_peparoni = input("Do you want to add peparoni? Y or N \n").lower()
extra_cheese = input("Do you want to add extra cheese? Y or N \n").lower()

if size == "s":
    if add_peparoni == "y":
        if extra_cheese == "y":
            m=15+2+1
            print("your final bill is $",m)
        else:
            m=15+2
            print("Your final bill is $",m)
    elif add_peparoni == "n":
        if extra_cheese == "n":
            m=15
            print("your final bill is $",m)
        else:
            m=15+1
            print("Your final bill is $",m)
elif size == "m":
    if add_peparoni == "y":
        if extra_cheese=="y":
            m=15+3+1
            print("your final bill is $", m)
        else:
            m=15+3
            print("your final bill is $",m)
    elif add_peparoni == "n":
        if extra_cheese == "n":
            m=20
            print("Your final bill is $",m)
        else:
            m=20+1
            print("your final bill is $",m)
elif size == "l":
    if add_peparoni == "y":
        if extra_cheese=="y":
            m=25+3+1
            print("your final bill is $", m)
        else:
            m=25+3
            print("your final bill is $",m)
    elif add_peparoni == "n":
        if extra_cheese == "n":
            m=25
            print("Your final bill is $",m)
        else:
            m=25+1
            print("your final bill is $",m)

else:
    print("please enter correct option, try again letter")            