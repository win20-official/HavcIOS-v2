import os as o

fixedpath = fr'"{o.getcwd()}"'

def file(name):
    if o.name == "nt":
        return o.system(f"python {name}")
    else:
        return o.system(f"python3 {name}")

def fixedclear():
    if o.name == "nt":
        return o.system("cls")
    else:
        return o.system("clear")