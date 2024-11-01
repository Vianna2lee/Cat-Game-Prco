cat_attributes = { 
    "intelligence": 60,
    "energy": 45,
    "weight": 10,
    "happiness": 30
}

print("Welcome to my cat game!!")

# Take the user inputs for name and colour:
name = input("Enter name: ")
colour = input("Enter colour: ")
age= input("Enter age: ")


# start the while loop
while True:
    # Finish the string below
    option = input("What would you like to do? 1. Play with your cat 2. Train your cat 3. Put it to sleep 4. Feed your cat 5.show stats 6 end program: ")

    if option == '1':
        # change the cat's attributes here
        cat_attributes["energy"]-=5
        cat_attributes["weight"]-=0.2
        cat_attributes["intelligence"]-=3
        cat_attributes["happiness"]+=5
        print(f"You played with {name}")

    elif option == '2':
        cat_attributes["energy"]-=6
        cat_attributes["weight"]-=0.5
        cat_attributes["happiness"]-=4
        print(f"You trained {name}")

    elif option =="3":
        cat_attributes["energy"]+=10
        cat_attributes["intelligence"]+=3
        cat_attributes["happiness"]+=4
        print(f"{name} took a nap.")

    elif option =="4":
        cat_attributes["energy"]+=3
        cat_attributes["weight"]+=4
        cat_attributes["happiness"]+=5
        print(f"You fed {name}")

    elif option=="5":
        print(f"{name}'s stats {cat_attributes}")

    elif option=="6":
        print(f"{name}'s stats {cat_attributes}")
        print("Thanks for playing")
        break
    else:
        print("Plese only enter 1/2/3/4/5/6")

    # finish off the if statements below
    if cat_attributes['energy'] <=0:
        print(cat_attributes)
        print(f"{name}s energy level is too low. It has passed away ...")
        break
    elif cat_attributes["intelligence"] <=0:
        print(cat_attributes)
        print(f"{name} is not smart enought to do anything...")
        break
    elif cat_attributes["happiness"]<=0:
        print(cat_attributes)
        print(f"{name} is depressed. It left you to find a better life...")
        break
    elif cat_attributes["weight"]<=0:
        print(cat_attributes)
        print(f"{name}is too light, it floated away...")
        break
    elif cat_attributes["weight"]>80:
        print(cat_attributes)
        print(f"{name} is overweight and needs to exercise ")
        
    

#end
