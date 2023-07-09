import random

usernames = ["super","cool","handsome","crazy","prime","strongest","clear"]

def KullaniciOlustur():
    word1 = usernames[random.randint(0, len(usernames)-1)]
    word2 = usernames[random.randint(0, len(usernames)-1)]
    print("\n" + word1 + " " + word2 + "\n")


while(True):
    print("Press enter button to create random username (type \"x\" for exit)")
    i = input()
    if i == "x" :
        break
    KullaniciOlustur()