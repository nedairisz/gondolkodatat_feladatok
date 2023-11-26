import math
import random

# Kérj be egy 2 jegyű (nehezebb: 3 jegyű) számot, és írd ki space-kkel elválasztva a számjegyeit!
def szamjegyek():
    i: int=0
    szam:int = int(input("Adj egy 3 jegyu szamot!: "))
    while not(100<=szam and szam<=999):
        szam:int = int(input("Adj egy 3 jegyu szamot!: "))
    szam_str=str(szam)
    while i<len(szam_str):
        print(szam_str[i], end=" ")
        i+=1

# Egy tetszőleges Stringben meg kell számolni, hogy egy másik String hányszor fordul elő. 
# A feladat egyszerűsítése érdekében, most kis és nagybetűk között nem teszünk különbséget, bár azzal sem lenne túl bonyolult a feladat.
def szovegkezeles(szoveg:str):
    keresett_karakter: str = "e"
    karakterszam:int = szoveg.count("e")
    print(f"A szovegben {karakterszam} db {keresett_karakter} betu van!")


#A következő feladat több programban is előfordulhat. Adott két időpont, melyeknél óra:perc:másodperc formában vannak megadva az időpontok. 
#A kérdés az, hogy mennyi idő telt el a két időpont között. Az időpontok formátuma gyakorlatilag teljesen mindegy, csak feldolgozás kérdése, 
#hogy előállítsuk belőle a megfelelő adatokat:

#String ido1 = "7:35:40";
#String ido2 = "8:20:15";

#A feladat tehát: mennyi idő telt el a két időpont között? Nem kell semmilyen komoly beépített vagy 
#importált dátumkezelő osztályra gondolni, csak játék a számokkal. 0:44:35



#Sorsolj ki egy pozitív egész számot, ami legfeljebb 1 milliárd lehet. Add össze a szám számjegyeit, 
# majd a kapott szám számjegyeit ismét add össze. Addig ismételd, amíg egyetlen számjegy nem marad, majd írd ki a végeredményt. 
# Az ellenőrzés megkönnyítése érdekében a köztes eredményeket is írd ki!
#Példa: 13637648 - 38 - 11 -2

def szamjegyek_osszege():
    szam:int = math.floor(random.random()*999999991+10)
    i:int=0
    osszeg:int=0
    while szam >0:
        utolso_szamjegy = szam% 10
        szam=szam//10
        osszeg+=utolso_szamjegy
        print(osszeg)
        szam = osszeg
    print("Végeredmény:", szam)