print("welcome to the pizza delivery service.......")

size=input("what size pizza do you want? S, M or L \n").lower()
add_peparoni = input("Do you want to add peparoni? Y or N \n").lower()
extra_cheese = input("Do you want to add extra cheese? Y or N \n").lower()


bill = 0

if size == "s":
    bill+=15
elif size == "m":
    bill+=20
elif size == "l":
    bill+=25

if add_peparoni == "y":
    if size =="s":
        bill+=2
    else:
        bill+=3

if extra_cheese == "y":
    bill+=1

print(f"Final bill is ${bill}")