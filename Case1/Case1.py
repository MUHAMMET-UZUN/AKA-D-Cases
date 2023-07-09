import random

kullaniciAdlari = ["super","cool","handsome","crazy","prime","strongest","clear"]

def KullaniciOlustur():
    kelime1 = kullaniciAdlari[random.randint(0, len(kullaniciAdlari)-1)]
    kelime2 = kullaniciAdlari[random.randint(0, len(kullaniciAdlari)-1)]
    print("\n" + kelime1 + " " + kelime2 + "\n")


while(True):
    print("Press enter button to create random username (type \"x\" for exit)")
    i = input()
    if i == "x" :
        break
    KullaniciOlustur()