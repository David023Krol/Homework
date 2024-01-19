#1. ÚLOHA - převod celsia na fahrenheit

Teplota = float(input("Zadej teplotu: "))
Výsledek = (Teplota*9/5) + 32

print("Teplota ve Fahrenheitech je:",(Výsledek))

#2. ÚLOHA - vypočet faktoriálu čísla:

Cislo = int(input("Zadej číslo: "))
faktorial = 1
for i in range(1, Cislo + 1):
    faktorial *= i

print(f"Faktoriál tohoto čísla je:", (faktorial))

#3. ÚLOHA - zjístí zda se jedná o čtverec nebo obdelník, vypíše délku stran

a = input("Zadej velikost a ")
b = input("Zadej velikost b ")

if a == b:
   print("Čtverec má delku strany ",a,"cm")
else:
   print("Obdelník má délku strany ",a,"cm", b, "cm")

#4. ÚLOHA - převod m/s na km/h

speed_ms = float(input("Zadej m/s: "))

speed_kmh = speed_ms * 3600 / 1000

print(speed_ms, "m/s je ", speed_kmh, "km/h")

temp_1 = 11
temp_2 = 21
temp_3 = 1

avg_temp = (temp_1 + temp_2 + temp_3*2) / 4

#5. ÚLOHA - výpis prvočísek

def je_prvocislo(cislo):
    if cislo < 2:
        return False
    for i in range(2, int(cislo**0.5) + 1):
        if cislo % i == 0:
            return False
    return True

n = int(input("Zadejte počet prvočísel: "))
prvocisla = [cislo for cislo in range(2, n*10) if je_prvocislo(cislo)]

print("Prvních", n, "prvočísel:", prvocisla[:n])

#6. ÚLOHA - generování náhodného hesla

import random
import string

delka_hesla = int(input("Zadejte délku hesla: "))
heslo = ''.join(random.choices(string.ascii_letters + string.digits, k=delka_hesla))

print("Vygenerované heslo:", heslo)

#7. ÚLOHA - výpočet průměru seznamu čísel

seznam = [float(x) for x in input("Zadejte seznam čísel oddělených mezerou: ").split()]
prumer = sum(seznam) / len(seznam)

print("Průměr seznamu je:", prumer)

#8. ÚLOHA - největší společný dělitel dvou čísel

def nsd(a, b):
    while b:
        a, b = b, a % b
    return a

cislo1 = int(input("Zadejte první číslo: "))
cislo2 = int(input("Zadejte druhé číslo: "))
vysledek = nsd(cislo1, cislo2)

print("Největší společný dělitel čísel", cislo1, "a", cislo2, "je:", vysledek)

#9. ÚLOHA - generování jednoduchého grafu pomocí hvězdiček

vyska = int(input("Zadejte výšku grafu: "))
for i in range(1, vyska + 1):
 print('*' * i)

#10. ÚLOHA - zjistí zda je zadaný rok přestupný 
 
rok = int(input("Zadejte rok: "))
prestupny = (rok % 4 == 0 and rok % 100 != 0) or (rok % 400 == 0)
if prestupny:
    print(f"Rok {rok} je přestupný.")
else:
    print(f"Rok {rok} není přestupný.")