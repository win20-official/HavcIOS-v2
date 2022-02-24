import os
from getpythonfiles import getbypath

wersja = 2.0
print(f"Witaj w systemie HavcOS {wersja}!")
print("")
print("Wybież opcję:")
print("")
print("1. Uruchom Kalkulator.")
print("2. Uruchom program To Do.")
print("3. Uruchom Program Notatnik.")
print("4. Uruchom Program CleverBot.")
print("5. Wyjdź z systemu HavcOS.")

opcja = input("Co chcesz zrobić? ")
path = os.getcwd()

if(opcja == "1"):
    getbypath.file(f"{path}/Kalkulator.py")

if(opcja == "5"):
    exit()

if(opcja == "3"):
    getbypath.file(f"{path}/Notatnik.py")



