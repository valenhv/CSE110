import random

ans_yes = ["Y", "YES"]
ans_no = ["N", "NO"]
invalid_ans = []

print("Start the game? (Y/N)")
start_game = input(">>")
invalid_ans += [start_game]

while start_game.upper() in ans_yes:

    magic_num = random.randint(1, 100)
    guess_list = []
    guess_num = ""
    guess_count = -1


    while guess_num != magic_num:
        print("What is your guess?")
        guess_num = int(input(">>"))
        guess_count = guess_count + 1
        guess_list += [guess_num]

        if guess_num < magic_num:
            print("Higher!")
        elif guess_num > magic_num:
            print("Lower!")
        else:
            print("Congrats!")
            print(f"It took you {guess_count} guesses. Without counting the correct one!")
            num_string = ", ".join(map(str,guess_list))
            # How the last line works (what I could assume):
            # We create a new variable (so it will be easier to put in a string later on)
            # .join(map(str,NAME_OF_LIST)) converts the list into a string, so I can put that into any other string I want
            # The ", " part is the string that goes after every item of the list until the last on. So, if I add that list to the string below, it will start and will end with its respective items. The difference is that after every item in the middle there will be a coma and a space.
            print(f"These are your guesses: " + num_string + ".")
            print("Play again?")
            start_game = input(">>")

while start_game.upper() in ans_no:
    print("Some other time then!")
    break