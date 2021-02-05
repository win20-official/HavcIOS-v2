import os, Main

print("...::NOTATNIK V1::...")
print("")
print("Co chcesz zrobić?")
print("1. Zrób Notatkę")
print("2. Wyjdź z Notatnika")

choice = input("Co chcesz zrobić?")

plik = open("notes.txt", "w", encoding="utf-8")
wrajt = plik.write = input("Napisz swoją Notatkę: ")

if(choice == "1"):
    wrajt
    os.system("cls")

if(choice == "2"):
    Main
    os.system("cls")
