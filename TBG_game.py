import time
import os


#choose game - def has to be first for some reason...
def start():   
    print("choose a story location.")
    print("1.Dungeon")
    print("2.Desert")
    print("3.more coming soon!")
    story = input("")
    if (story == "1" or story == "Dungeon" or story == "dungeon"):
        os.system("C:/python/python.exe C:/python/TBG_dungeon.py")
start()