import os, Kalkulator, Notatnik

print("Witaj w systemie HavcOS!")
print("")
print("Wybież opcję:")
print("")
print("1. Uruchom Kalkulator.")
print("2. Uruchom program To Do.")
print("3. Uruchom Program Notatnik.")
print("4. Uruchom Program CleverBot.")
print("5. Wyjdź z systemu HavcOS.")

opcja = input("Co chcesz zrobić? ")
os.system("cls")

if(opcja == "1"):
    Kalkulator

if(opcja == "5"):
    exit()

if(opcja == "3"):
    Notatnik

os.system("cls")

