import os
import time
def spc():
    print("")
    print("")
    print("")
def storya():
    os.system("cls")
    print('Everything is dark. You hear faint noises as you get on your feet.\
        you look around, searching for a light or a wall.')
    print('After some fumbling, you finally feel a wall. Its a stone wall, and you can feel the individual bricks.\
        Some of them are loose.')
    print('As you pull lightly on one of them, a certain degree of give indicates that you might be able to remove it.')
    print("If you pull harder...")
    action = input("do you pull the brick? ")
                        #correct 1
    if(action == "No" or action == "no"):
        spc()
        print("you choose not the pull out the brick.")
        print("you feel your way to one of the corners and sit down.")
        print("after what feels like an eternity, a sharp light blows the room lit.")
        print("you see there is a door next to the loose bricks.")
        print("")
        action = input("do you enter the room?")
                        #correct 2-nxtroom
        if(action == "yes" or action == "Yes"):
                room1a()

                        #death 2
        if(action == "no" or action == "No"):
                spc()
                print("you wait even longer in the corner of the room.")
                print("suddenly, you see spikes emerge from the roof.")
                print("you try to leave the room through the door, but it locks, and you get crushed.")
                input("")
                action = input("try again?")
                if(action == "yes" or action == "Yes"):
                    storya()
                if(action == "no" or action == "No"):
                    os.system("C:/python/python.exe C:/python/TBG_menu.py")

                        # death 1
    if(action == "yes" or action == "Yes"):
        spc()
        print("you pull the brick, and you fall backwards as the brick gives in.")
        print("behind the newly created hole you see a source of light.")
        print("you start removing the other bricks close by, and soon enough, you have made")
        print("a hole big enough to climb through.")
        print("as you climb through the hole, you hear a screeching sound, and watch in terror")
        print("as the hole gets smaller and smaller. you try to get through, but you end up")
        print("being too slow, and the wall crushes your ribcage and half of your body")
        print("flops to the ground on both sides.")
        input("")
        action = input("try again?")
        if(action == "yes" or action == "Yes"):
            storya()
        if(action == "no" or action == "No"):
            os.system("C:/python/python.exe C:/python/TBG_menu.py")

def room1a():
        os.system("cls")
        print("as you enter the next room, you look back and see the spikes from the ceiling mash the floor.")
        print("you get scared for a second, because you thought about staying in there.")
        print("'anyways' you think to yourself and shake it off. as you look at what is ahead of you in the next")
        print("room, see a shelf to the left of you, a bench with some mechanical parts on it to the right, and a")
        print("sign in front of you, that says 'to leave this room, you have to find my hidden passion. but beware,")
        print("if you get it wrong, your life shall end.'")
        print("'to the left, on the shelf, you shall find yourself.'")
        print("'to the right, on the bench, there are bolts and a wrench.'")
        print("and thats all it says.")
        action = input("should i go left to the shelf or right to the bench?")
        if (action == "shelf" or action == "Shelf" or action == "left" or action == "Left"):
                #correct shelf here
                spc()
                print("you see a note on the shelf. it says, 'press the button if you truly believe you chose correct.")
                print("you press the button, and a whirring mechanism makes the wall with the poster vanish into the floor.")
                input("")
                room2a()
                #wrong shelf here
        if(action == "bench" or action == "Bench" or action == "right" or action == "Right"):
                spc()
                print("you go to the right and look at the bench. theres a chair infront of you, with what looks")
                print("like comfortable cloth. you cant remember the last time you sat nicely, so you sit down infront of")
                print("the bench. as soon as you sit down, your hear a 'click' and your arms are locked in place. you try to ")
                print("stand up, but your legs get locked in the same way as your arms.")
                print("you hear a small buzzing sound, and then a ZAP.")
                input("")
                action = input("try again?")
                if(action == "yes" or action == "Yes"):
                    room1a()
                if(action == "no" or action == "No"):
                    os.system("C:/python/python.exe C:/python/TBG_menu.py")
def room2a():
    os.system("cls")
    print("as you step forward through the newly created doorframe, you trip over a wire set foot-high")
    print("and a hole opens in the floor, and you slip down a hatch.")
    print("when you finally hit the bottom, the slope gets closed behind a door.")
    print("only now do you realise how little clothes you have on, as this room is really cold.")
    print("you notice that on the ceiling, there are icecicles on the ceiling.")
    input("")






storya()
