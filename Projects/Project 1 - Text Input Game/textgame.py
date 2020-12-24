'''
Welcome to my first python based text game!
'''
import time



def choice1(answer):
    if (answer == "farmer") or (answer == "adventurer") or (answer == "royal guard") :
        confirm_bckgrnd = input("You have chosen the " + answer + " backstory, would you like to proceed? - Please enter 'yes' to continue or 'no' to stop: ")
        if confirm_bckgrnd == "yes":
            print(context(answer))
            return "Thank you for playing my game!"  
        return "If you would like to change backstories please restart the program."
    else:
        return "We apologize, but we currently do not have that backstory. Please restart the program to choose a valid backstory."


def context(answer):
    if answer == "farmer":
        print("You're a humble farmer, your family has tilled your lands for generations.")
        time.sleep(2)
        print("For 18 years, the beautiful scenery of the Swiss plains have served as your home.")
        time.sleep(2)
        print("The mountains and forests, as your playground. And your farm, as your training grounds")
        time.sleep(2)
        print("As a farmhand you've learnt how to deal with animals. Through your adventures in the forests, you know what fruits are the best to eat. And through your escapades in the mountains, you've learnt how the upper limits of yout abilities.")
        time.sleep(3)
        print("But you want more! You want the thrill of adventure, you crave for it.")
        time.sleep(2)
        print("You decide that you want to leave your farm for pastures new")
        time.sleep(2)
    #if answer == "adventurer":
        
    #if answer == "royal guard":
    return "bruh"


print("Welcome to my first game!")
print("This game is suitable for all ages! Although rather short.")

answer = input("Please choose between these 3 different backgrounds - 'Farmer', 'Adventurer', 'Royal Guard': ").lower()
print(choice1(answer))