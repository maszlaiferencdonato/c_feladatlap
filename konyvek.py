konyvek = []

with open("konyvek-adatok.txt", "r", encoding="utf-8") as f:
    for sor in f:
        adatok = sor.strip().split(";")  
        konyvek.append(adatok)

# 1. feladat
print(f"1. A listában {len(konyvek)} db könyv található!")

# 2. feladat
mufaj =(input("Írj be egy műfajt: "))
db = 0
ossz_oldal = 0

for konyv in konyvek:
    if konyv[1].strip().lower() == mufaj:
        db += 1
        ossz_oldal += int(konyv[2]) 

print(f"2. {db} könyv tartozik ebbe a műfajba, összesen {ossz_oldal} oldalon.")

# 3. feladat

for konyv in konyvek:
    if 1600 <= int(konyv[3]) <= 1699 and konyv[1] == "színmű":
        print("1600 és 1699 között van színmű műfajban írt könyv")
        break

# 4. feladat