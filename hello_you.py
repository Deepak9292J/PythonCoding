#Ask user for name
name = input("What is your name? ")
print(name)

#Ask user for age
age = input("What is your age?" )
print(age)

#Ask user for City
city = input("What is your city? ")
print(city)

#Ask user abiut hobbies
hobbies = input("What are youe hobbies? ")
print(hobbies)

#Create output text
string = "My name is {}. I am {} years old. I am from {} city. My Hobbies are {}"
output = string.format(name, age, city, hobbies) 

#Print output to screen
print(output)
