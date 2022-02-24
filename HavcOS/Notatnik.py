import os
from getpythonfiles import getbypath

print("...::NOTATNIK V2::...")
print("")
print("Co chcesz zrobić?")
print("1. Zrób Notatkę")
print("2. Wyjdź z Notatnika")
print("3. Nowe rzeczy")

choice = input("Co chcesz zrobić?")
path = os.getcwd()


if choice == "1":
    plik = open("notes.txt", "w", encoding="utf-8")
    wrajt = input("Napisz swoją Notatkę: ")
    plik.write(wrajt)
    os.system("cls")

if choice == "2":
    getbypath.file(f"{path}/Main.py")
    os.system("cls")

if choice == "3":
    print("Naprawiono problem z nie działającym zapisywaniem notatek")