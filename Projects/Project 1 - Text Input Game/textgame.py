print("Welcome to my first game!")
print("This game is suitable for all ages! Although rather short.")

answer = input("Please choose between these 3 different backgrounds - 'Farmer', 'Adventurer', 'Royal Guard': ")
def choice1(answer):
    if (answer.lower() == "farmer") or (answer.lower() == "adventurer") or (answer.lower() == "royal guard") :
        confirm_bckgrnd = input("You have chosen the " + answer + " backstory, would you like to proceed? - Please enter 'yes' to continue or 'no' to stop: ")
        if confirm_bckgrnd == "yes":
            return True
        else:
            print("If you would like to change backstories please restart the program.")
            return False
    else:
        print("We apologize, but we currently do not have that backstory")
        return False


def context(answer):
    print("bruh")

print(choice1(answer))