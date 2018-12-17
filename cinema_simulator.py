films = {
    "Kya Kool Hai Hum": [19, 3],
    "Grand masti" : [20,10],
    "PK" : [25,10],
    "3 idiots" : [10,20],
    "Dangal" : [30, 10]
    }

while True:
    choice = input("Which film would you like to watch?: ").strip().title()
    if choice in films:
        age = int(input("How old are you?: ").strip())
        
        #Check user's age
        if age >= films[choice][0]:

            #Check seats availability
            if films[choice][1] > 0:
                print("Enjoy the film!")
                films[choice][1] = films[choice][1]-1
            else:
                print("We are sold out!")
        else:
            print("You are tool young to watch the film!")
    else:
        print("Film not available!")
        
        
