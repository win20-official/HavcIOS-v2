from getpythonfiles.getbypath import *
fixedclear()

print("...::Kalkulator v1::...")
 
def dodawanie(num1, num2):
   return num1 + num2

def mnozenie(num1, num2):
    return num1 * num2

print("")
print("...::Menu::...")
print("1. Dodawanie   ")
print("2. Mnożenie    ")

opcja = input("Co chcesz zrobić?")
path = fixedpath

if opcja == "1":
    a = float(input("Podaj liczbe: "))
    b = float(input("Podaj liczbe: "))
    print(f"{a} + {b} = {dodawanie(a, b)}")
    halo = input("Czy chcesz powrócić do HavcOS? (Dostępna tylko opcja: Tak) ")

if opcja == "2":
    a = float(input("Podaj liczbe: "))
    b = float(input("Podaj liczbe: "))
    print(f"{a} * {b} = {mnozenie(a, b)}")
    halo = input("Czy chcesz powrócić do HavcOS? (Dostępna tylko opcja: Tak) ")

if halo == "Tak":
    file(f"./{path}/main.py")