# Student: Valentina Hernandez Vera
# Exceeding requirements: Added difficulty levels. Also, the program now can tell when the user needs to input more (or less) letters, also made use of "continue" so the code wouldn't be so lenghty.

secret_word_easy = "apple"
secret_word_med = "pathway"
secret_word_hard = "outrageous"
secret_word_ext = "supercalifragilisticexpialidocious"
guess_count = 0

secret_word = ""

print("Welcome to the word guessing game!")
print("Rules: Type a word of the same length as the hint. Keep guessing until you make it!")
print("Choose the difficulty: EASY / MEDIUM / HARD / EXTREME")
chosen_difficulty = input(">>").upper()

if chosen_difficulty == "EASY":
    secret_word = secret_word_easy
elif chosen_difficulty == "MEDIUM":
    secret_word = secret_word_med
elif chosen_difficulty == "HARD":
    secret_word = secret_word_hard
elif chosen_difficulty == "EXTREME":
    secret_word = secret_word_ext
else:
    print("Invalid input.")

print("Your hint is:", "_ " * len(secret_word))

while True: # This will make the loop go on forever until the game is finished.
    user_guess = input(">>").lower()
    guess_count += 1

    if len(user_guess) < len(secret_word):
        print("You need a word with a few more letters.")
        print("Your hint is:", "_ " * len(secret_word))
        continue # Tells the program to go straight to the last part of the while, which is to display the hint again. This will repeat UNTIL the length of the word is correct.
    elif len(user_guess) > len(secret_word):
        print("You need a word with less letters.")
        print("Your hint is:", "_ " * len(secret_word))
        continue
    if user_guess == secret_word:
        print("Congratulations! You guessed it!")
        print(f"It took you {guess_count} tries.")
        break

    hint = ""
    for i in range(len(secret_word)):
        if user_guess[i] == secret_word[i]: # Checks if there's a correct letter in user_guess AND if it's in the correct position
            hint += user_guess[i].upper() # Rewrites the var hint so that the correct letter will be in CAPS now
        elif user_guess[i] in secret_word: # Checks if there's a correct letter in user_guess, but in the wrong position
             hint += user_guess[i] # Rewrites the hint variable to show the correct letter in the same wrong position
        else:
            hint += "_"
        hint += " "
    print(f"Your hint is: {hint}.")