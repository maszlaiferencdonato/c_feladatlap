mertekegyseg = input("Milyen mértékegységben adod meg: ")
atvaltando_szam = float(input("Írd be az átváltandó számot: "))

if mertekegyseg == "MB":
    eredmeny = atvaltando_szam / 1024
    print(f"Az eredmény: {eredmeny} GB")
elif mertekegyseg == "GB":
    eredmeny = atvaltando_szam * 1024
    print(f"Az eredmény: {eredmeny} MB")

