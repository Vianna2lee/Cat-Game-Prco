cat_attributes = {
    "intelligence": 80,
    "energy": 90,
    "weight": 10,
    # change the inital values above
}

print("Welcome to my cat game!!")

# Take the user inputs for name and colour:
name = input("Enter name:")
colour = input("Enter colour")
# ...

# start the while loop
while True:
    # Finish the string below
    option = input("What would you like to do? 1. Play with your cat 2. Train your cat 3. Put it to sleep 4. show stats")

    if option == '1':
        # change the cat's attributes here
        cat_attributes["energy"]=cat_attributes["energy"]-2
        cat_attributes["weight"]=cat_attributes["weight"]-0.001
    elif option == '2':
        cat_attributes["energy"]=cat_attributes["energy"]-5
        cat_attributes["weight"]=cat_attributes["weight"]-0.01
    elif option =="3":
        cat_attributes["energy"]=cat_attributes["energy"]+10
        cat_attributes["intelligence"]=cat_attributes["intelligence"]+0.1
    else:
        print(cat_attributes)

    # finish off the if statements below
    if cat_attributes['energy'] < 0:
        pass
    # elif ...
    
