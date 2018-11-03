#Importing here
import winsound
import time
import os
#defining blank screen
def blank():
    i = 0
    while(i < 100):
        print("")
        i += 1
        time.sleep(0.001)
def spc():
    print("")
    print("")
    print("")
#defining Menu, use blank() before using Menu for best effect.
def Menu():
    print("1. Start the game")
    print("2. Settings")
    print("3. Help")
    print("4. Exit")
    action = input("")
    if(action == "1" or action == "Start" or action == "start" or action == "start the game" or action == "Start the game"):
        os.system("C:/python/python.exe C:/python/TBG_game.py")
    if( action == "2" or action == "settings" or action == "Settings"):
         Settings()
    if( action == "3" or action == "help" or action == "Help"):
         Help()
    if( action == "4" or action == "exit" or action == "Exit"):
        Exit()
    else:
        blank()
        Menu()


# Settings
def Settings():
    blank()
    print("1.text and background color")
    print("2.coming soon")
    print("3.coming soon")
    action = input("")
    if (action == "1"):
        spc()
        print("first choose a text color:")
        print("0.black")
        print("1.blue")
        print("2.green")
        print("3.aqua")
        print("4.red")
        txtcolor = input("")
        spc()
        print("now choose a background color:")
        print("0.black")
        print("1.blue")
        print("2.green")
        print("3.aqua")
        print("4.red")
        bckgroundcolor = input("")
        os.system("color " + bckgroundcolor + txtcolor)
        input("")
        
# Help
def Help():
    blank()
    print("this game is a 'choose your own adventure' textbased horror/scare game.")
    print("you get a scenario, and you choose one of 2(or more) things.")
    print("and then if you choose a, you will get to a scenario based on that.")
    print("heres an example.")
    spc()
    print("you see a wall infront of you, and a hallway that goes to the left and right of you.")
    print("will you go left or right?")
    action = input("")
    if (action == "left" or action == "Left"):
        spc()
        print("you chose to walk left. as you turn around to go left, you hear a faint sound behind you.")
        print("you begin walking forward, and you see a chest. will you open it?")
        action = input("")
        if(action == "yes" or action == "Yes"):
            spc()
            print("you open it, and a sword pops out and stabs you in the chest.")
        if(action == "no" or action == "No"):
            spc()
            print("you choose not to open the chest, but look around the chest and see that behind it is a mechanism that seems like it")
            print("could have killed you if you had opened it. on a shelf to the right of you theres a bag. you take the bag and look inside")
            print("and inside there are 20 gold coins.")
            input("")
    if(action == "right" or action == "Right"):
        spc()
        print("you turn left around the corner and you see a demon, staring into your soul.")
        print("you turn around and try to outrun it, but it catches up with you and tear a hole in your chest,")
        print(" and the last thing you see before everything turns black is your still beating heart in the demons hand.")
        input("")
    if(action == ""):
        spc()
        print("if you choose not to write anything, you wont go further in the game.")
        print("please, refrain from pressing enter without writing either left, right, forward, backwards, yes, no, or other actions")
        print("you get the option to choose.")
        print("at this point i have not made a working mechanism for fixing the error, but if it happens, im sorry.")
        input("")
    print("and thats how the game would work.")
    print("you will get thrown back to the menu now.")
    input("")
# Exit
def Exit():
    print("bye")
    blank()


# # # # the game from here - add def's and imports up there/\# # # # 



#fake startup
print("Booting - menu starting")
print("*loading profile info*")
time.sleep(2)

#progress to finish fake loading, consider making a skip?
i = 0
progress = 0
while (i < 100):
    progress += 1
    i += 1
    print(str(progress) + "%")
    time.sleep(0.05)

print("")
print("")
print("                              TBG ver.1.23.55 - license and ownership Th4t0n3f15h")
print("BIOS Version 2.43")
print("                                                                                  group name:")
print("                                                                                  -D34DF15H")
print(" Currently Running blueberry pythagoras vers. 1.23")
print("")
print("")
print("menu loading")
import startupsound
blank()
Menu()