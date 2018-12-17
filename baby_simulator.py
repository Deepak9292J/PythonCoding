import random

questions = ["Why is the sky blue?: " , "Why chalk is tasty?: " , "Why am I so cute?: "]
question = random.choice(questions)
answer = input(question).strip().lower()

while answer != "just because":
    answer = input("Why? :").strip().lower()
        
print("Oh..okay!")
