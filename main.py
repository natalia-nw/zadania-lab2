# zad 1
lista = ["łyżwiarstwo", "kolarstwo", "siatkówka"]
lista.reverse()
lista.append("koszykówka")
lista.append("piłka nożna")
print(lista)

# zad 2
slownik = {"str.": "strona", "np.": "na przykład", "nr": "numer", "itp.": "i tym podobne"}
print(slownik)
print(slownik.keys())
print(slownik.values())

# zad 3
gry = {"LOL": "Legue of Legends", "CS": "Counter Strike"}
print(gry)

# zad 4
zdanie = input("Wprowadz zdanie: ")
print(zdanie.count("a"))

# zad 5
import sys as system
system.stdout.write("wpisz liczbę a: ")
a = system.stdin.readline()
system.stdout.write("wpisz liczbę b: ")
b = system.stdin.readline()
system.stdout.write("wpisz liczbę c: ")
c = system.stdin.readline()

a = int(a)
b = int(b)
c = int(c)

wynik = pow(a, b) + c

system.stdout.write(str(wynik))

# zad 6
a = input("podaj pierwszą liczbę: ")
b = input("podaj drugą liczbę: ")
c = input("podaj trzecią liczbę: ")

a = int(a)
b = int(b)
c = int(c)

if (a > b) & (a > c):
    print("liczba a jest największa")
elif (b > a) & (b > c):
    print("liczba b jest największa")
else:
    print("liczba c jest największa")

# zad 7
lista = [2, 5, 3.4, 6, 7.67, 9, 1.08]
for x in lista:
    print(pow(x, 2))

# zad 8
parzyste = []
z = 0
while z != 10:
    if z % 2 == 0:
        parzyste.append(z)
    z += 1
print(parzyste)

# zad 9
lista = [1, 2, 3, 4, 5]
i = 0
while i < len(lista):
    if lista[i] % 2 == 0:
        print("E")
        i = i+1
    else:
        print("EEEEEE")
        i = i+1

# zad 10
import math
print("podaj liczbe: ")
liczba = input()
liczba = int(liczba)

try:
    pierwiastek = math.sqrt(liczba)
    print(pierwiastek)
except ValueError:
    print("błąd")