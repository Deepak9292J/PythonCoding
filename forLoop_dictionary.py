#dictionary where male has a list of students and female has a list  of students
students = {
    "male" : ["Deepak", "Shubham" , "Happy"],
    "female" : ["Timsy" , "Meet" , "Srishti"]
    }

#Getting the keys of all the items
for key in students.keys():

    #Checking each name in that key
    for name in students[key]:

        #Checking if the name contains the letter "a"
        if "a" in name:

            #If the name contains letter "a", then we are printing only that name
            print(name)
    
    
