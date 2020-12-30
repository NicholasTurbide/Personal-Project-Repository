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
        print("\nYou're a humble farmer, your family has tilled your lands for generations.")
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
        print("So you set off on an adventure of a lifetime, not knowing when you will come back.")
    elif answer == "adventurer":
        print("\nYou've ventured through dozens of tombs and temples")
        time.sleep(2)
        print("Adventure is in your blood, discovery is in your spirit, and thrill is in your body")
        time.sleep(2)
        print("Once more, you are setting off on an adventure, not knowing what awaits you, or when you will return to your home.")
        time.sleep(2)
        print("")
    #if answer == "royal guard":
    print(first_encounter(answer))
    return ""

def first_encounter(answer):
    if answer == "farmer":
        print("\nAfter having gathered your things, you leave bright and early.")
        time.sleep(2)
        print("You take the scenic route, taking in the scenery memories flood in like a hurricane.")
        time.sleep(2)
        print("You remember the first time you went on one of your woodland adventures.")
        time.sleep(2)
        print("\n***Flasback***")
        time.sleep(2)
        forest_inp1 = input("You are faced with 2 paths, the path on the right sounds like there is a waterfall nearby, the path to the left has a clearing in the forests - (Left/Right): ").lower()
        if forest_inp1 == "left":
            print("You walk towards the clearing, eyeing down the area, trying to see if there are any animals nearby")
            time.sleep(2)
            print("You spot a snowshoe hare, a species that shouldn't be on this continent!")
            time.sleep(2)
            print("You follow the hare")
        if forest_inp1 == "right":
            print("WIP")
    return ""


print("Welcome to my first game!")
print("This game is suitable for all ages! Although rather short.")

answer = input("Please choose between these 3 different backgrounds - 'Farmer', 'Adventurer', 'Royal Guard': ").lower()
print(choice1(answer))