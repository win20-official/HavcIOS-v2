from getpythonfiles.getbypath import *
fixedclear()

print("...::NOTATNIK v2::...\n")
print("Co chcesz zrobić?")
print("1. Zrób Notatkę")
print("2. Wyjdź z Notatnika")
print("3. Nowe rzeczy")

choice = input("Co chcesz zrobić?")
path = fixedpath

if choice == "1":
    plik = open("notes.txt", "w", encoding="utf-8")
    write = input("Napisz swoją Notatkę: ")
    plik.write(write)
    fixedclear()

if choice == "2":
    file(f"./{path}/main.py")
    fixedclear()

if choice == "3":
    print("Naprawiono problem z nie działającym zapisywaniem notatek.")
    print("Dodano wsparcie dla Linuxa itp.")