known_users = ["Deepak" , "Timsy", "Meet", "Amisha", "Ritu", "Manish"]

while True:
    print("Hi! My name is Travis! ")
    name = input("What is your name?: ").strip().capitalize()
    if name in known_users:
        print("Hello {}! Your name is identified!".format(name))
        remove = input("Would you like your name to be removed from the security system?: (y/n) ").strip().lower()
        if remove == "y":
            known_users.remove(name)
            print(known_users)
        else:
            print("No Worries!")
        
    else:
        print("Hello {}! Your name is not identified!".format(name))
        add_user = input("Would you like your name to be added to the security system?: (y/n) ").strip().lower()
        if add_user == "y":
            known_users.append(name)
            print(known_users)
        else:
            print("No Worries!")
