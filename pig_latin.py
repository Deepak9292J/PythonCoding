#Get sentence from user
original = input("Please enter as sentence: ").strip().lower()

# Break sentence into words.
words = original.split()

#Loop through words and convert to pig latin
new_words = []

for word in words:
    if word[0] in "aeiou":
        new_word = word + "yay"    
        new_words.append(new_word)
    else:
        new_word = word[1:] + word[0] + "ay"
        new_words.append(new_word)   

#stick words back together
output = " ".join(new_words)

#output the final string
print(output)
