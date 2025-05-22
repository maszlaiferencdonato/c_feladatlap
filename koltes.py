penz=int(input("Írd be, hogy mennyi pénzed van: "))


while penz > 0:
        koltes=int(input("Mennyit szeretnél költeni belőle: "))

        if koltes<=penz:
            penz=penz-koltes
            print(f"Ennyi pénzed maradt: {penz}")  
        else:
            print("Ennyit nem költhetsz, nincs ennyi pénzed")




        