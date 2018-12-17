vowels = 0
consonants = 0
for letters in "beautiful":
	if letters.lower() in "aeiou":
		vowels = vowels + 1
	else:
		consonants = consonants +1

print("Vowels are {}".format(vowels))
print("consonants are {}".format(consonants))
