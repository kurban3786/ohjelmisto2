import random
from prettytable import PrettyTable

class Car:
    def __init__(self, rekisterinumero, huippunopeus, nopeus, kokonaismatka):
        self.kokonaismatka = kokonaismatka
        self.nopeus = nopeus
        self.huippunopeus = huippunopeus
        self.rekisterinumero = rekisterinumero

    def kiihtyvyys(self, nopeuden_muunnos):
        if self.nopeus + nopeuden_muunnos >= 0 and self.nopeus + nopeuden_muunnos <= self.huippunopeus:
            self.nopeus = self.nopeus + nopeuden_muunnos

        elif self.nopeus + nopeuden_muunnos < 0:
            self.nopeus = 0

        elif self.nopeus + nopeuden_muunnos > self.huippunopeus:
            self.nopeus = self.huippunopeus

    def matka_aika(self, tunti):
        self.kokonaismatka = self.kokonaismatka + (self.nopeus * tunti)

class Race:
    def __init__(self, nimi, pituuskm, autolista):
        self.nimi = nimi
        self.pituuskm = pituuskm
        self.autolista = autolista

    def tunti(self):
        for i in self.autolista:
            i.kiihtyvyys(random.randint(-10, 15))
            i.matka_aika(1)

    def lista(self):
        x = PrettyTable()
        x.field_names = ["Rekisterinumero", "Huippunopeus", "Hetkellinen nopeus", "Kokonais matka"]
        for u in self.autolista:
            x.add_row([f"{u.rekisterinumero}",f"{u.huippunopeus}KM/H",f"{u.nopeus}KM/H",f"{u.kokonaismatka}KM"])
        print(x)

    def yli(self):
        for u in self.autolista:
            if u.kokonaismatka >= self.pituuskm:
                return True

# Pääohjelma
cars = []
for i in range(10):
    cars.append(Car(f"ABC-{i + 1}", random.randint(100, 200), 0, 0))

kisa = Race("TOPSPEED", 8000, cars)

kierros1 = 1
stop = False
print("Kierros 1")
while not stop:
    kisa.tunti()
    stop = kisa.yli()
    if kierros1 % 10 == 0:
        kisa.lista()
        print(f"Kierros {kierros1}")
    kierros1 += 1
kisa.lista()