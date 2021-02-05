import os, Main

print("...::Kalkulator ALPHA v1::...")
 
def dodawanie(a, b):
   return a + b

print("")
print("...::Menu::...")
print("1. Dodawanie   ")

opcja = input("Co chcesz zrobić?")

a = float(input("Podaj liczbe: "))
b = float(input("Podaj liczbe: "))

if(opcja == "1"):
    print(a,"+",b,"=", dodawanie(a,b))
    halo = input("Czy chcesz powrócić do HavcOS? (Dostępna tylko opcja: Tak) ")

if(halo == "Tak"):
    Main

os.system("cls")

  




 
 