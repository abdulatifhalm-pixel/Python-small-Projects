pizza = input("what kind of pizza do you want ,s/m/l")
bill = 0
if pizza == "s":
    print("small pizza price is 150 af")
    bill += 150
    print("your bill is 150 af ")
elif pizza == "m":
    print("mild pizza price is 200 af")
    bill += 200
    print("your bill is 200 af ")
elif pizza == "l":
    print("large pizza price is 500 af")
    bill += 500
    print("your bill is 500 af ")
cheese = input("do you want extra cheese y/n")
if cheese == "y":
    bill += 20
    print("cheese price is 20af ")
    total_bill = bill + 20
