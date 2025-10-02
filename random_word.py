import random

words = ["python","java","software","hardware","visual","dream","technology"]
secret_word = random.choice(words)
estimate = ["_"]*len(secret_word)
right = 5

print("Welcome to Word Game!")
print(f"The word is :"," ".join(estimate))


while right > 0 and "_" in estimate:
    letter = input("Enter a letter:").lower()
    
    if letter in secret_word:
        for i in range(len(secret_word)):
            if secret_word[i] == letter:
                estimate[i] = letter
                
        print("True Word is: "," ".join(estimate))
    else:
        right -= 1
        print(f"Wrong! Remaining rights:{right}")       
        
if "_" not in estimate:
    print("Well Done, Word:", secret_word)
else:
    print("You lost :(. Word:",secret_word)