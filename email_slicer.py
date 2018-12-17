# Get user's email ID
get_email = input("What is your email ID?: ")

#slice out username
get_username = get_email[:get_email.index("@")]

#slice out domain name
get_domain = get_email[get_email.index("@") +1:]

#format message
string = "Username is {} and domain is {}".format(get_username,get_domain)

#display output message
print(string)
