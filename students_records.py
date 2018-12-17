students = {
            "Deepak": ["ID1" , 26 , "A grade"],
            "Ritu":["ID2" , 21 , "B grade"],
            "Rahul":["ID3" , 22 , "C grade"]
            }

print(students["Deepak"][0:])
print(students["Ritu"][1:])

altername_students = {
            "Deejay": {"ID" : "ID1" ,"age" : 26 , "grade" : "A grade"},
            "Happy":{"ID" : "ID2" ,"age" : 22 , "grade" : "B grade"},
            "Bond":{"ID" : "ID3" ,"age" : 27 , "grade" : "C+ grade"}
            }

print(altername_students["Deejay"]["age"])
print(altername_students["Deejay"]["age"] , altername_students["Happy"]["grade"] , altername_students["Bond"]["ID"])

