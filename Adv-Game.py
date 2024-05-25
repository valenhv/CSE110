# Student: Valentina Hernandez Vera
# Creativity: Used def, lists and while. More then three levels.

def get_input(prompt, options):
    while True:
        user_input = input(prompt).strip().upper()
        if user_input in options:
            return user_input
        print("Invalid input. Please try again.")

def start_game():
    print("Get the fish")
    start_game = get_input("Start? (Y/N): ", ["Y", "N"])
    if start_game == "Y":
        kitchen_adventure()
    elif start_game == "N":
        print("Some other time then.")

def kitchen_adventure():
    print("You wake up from your nap enticed by the smell of fish coming from the kitchen.")
    print("However, you're feeling really sleepy... What do you do? (KITCHEN/SLEEP)")
    choice = get_input(">> ", ["KITCHEN", "SLEEP"])
    if choice == "KITCHEN":
        print("You set out on your adventure to the kitchen!")
        print("But one of your owner's kids wants to play with you!")
        play_with_kid()
    elif choice == "SLEEP":
        print("You go back to sleep... Hours pass... When you wake up, you find out your family ate all the fish. You lose!")

def play_with_kid():
    choice = get_input("Will you play with her? (YES/NO) >> ", ["YES", "NO"])
    if choice == "YES":
        print("You play along for a while but then get tired of it. Thinking about the fish, you go back to your adventure.")
    elif choice == "NO":
        print("Sorry kid, but the fish is more important!")
        get_fish()

def get_fish():
    print("You arrived at the kitchen, and there's a big salmon waiting for you!! Except it's not, your owner doesn't want you to eat it. So they give you other food you don't really want right now...")
    choice = get_input("What do you choose? (FISH/CATFOOD/DON'T EAT) >> ", ["FISH", "CATFOOD", "DON'T EAT"])
    if choice == "CATFOOD":
        print("You settle for the bowl of cat food... It's not that bad, but not really what you wanted.\nYour owner's family is eating the fish now. You lose!")
    elif choice == "DON'T EAT":
        print("Oh! Now you're forcing your owner to give you the fish! He won't let you be hungry, so he reluctantly gives you what you wanted... You win!")
    elif choice == "FISH":
        print("You have to get it your way! The owner is really pushy, though!")
        print("Do you distract them with something or go straight to the fish? (DISTRACT/FISH)")
        choice = get_input(">> ", ["DISTRACT", "FISH"])
        if choice == "FISH":
            print("Despite all odds, you get the fish. You win!")
        elif choice == "DISTRACT":
            print("You try to distract your owner by pretending to play with him...")
            print("After a while, he's in another room. You take your chance and get the fish. You win!")

start_game()