from getpythonfiles.getbypath import *

wersja = 2.0
print(f"Witaj w systemie HavcOS {wersja}!\n")
print("Wybierz opcję:\n")
print("1. Uruchom Kalkulator.")
print("2. Uruchom program To Do.")
print("3. Uruchom Program Notatnik.")
print("4. Uruchom Program CleverBot.")
print("5. Wyjdź z systemu HavcOS.")

opcja = input("Co chcesz zrobić? ")
path = fixedpath

if opcja == "1":
    file(f"{path}/aplikacje/kalkulator.py")

if opcja == "5":
    exit()

if opcja == "3":
    file(f"{path}/notatnik.py")