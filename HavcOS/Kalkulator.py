import os
from getpythonfiles import getbypath

print("...::Kalkulator v1::...")
 
def dodawanie(a, b):
   return a + b

def mnozenie(a, b):
    return a * b

print("")
print("...::Menu::...")
print("1. Dodawanie   ")
print("2. Mnożenie    ")


opcja = input("Co chcesz zrobić?")
path = os.getcwd()



if opcja == "1":
    a = float(input("Podaj liczbe: "))
    b = float(input("Podaj liczbe: "))
    print(a,"+",b,"=", dodawanie(a,b))
    halo = input("Czy chcesz powrócić do HavcOS? (Dostępna tylko opcja: Tak) ")

if opcja == "2":
    a = float(input("Podaj liczbe: "))
    b = float(input("Podaj liczbe: "))
    print(a,"*",b,"=", mnozenie(a,b))
    halo = input("Czy chcesz powrócić do HavcOS? (Dostępna tylko opcja: Tak) ")

if halo == "Tak":
    getbypath.file(f"{path}/Main.py")

os.system("cls")

  




 
 