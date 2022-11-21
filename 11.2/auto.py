class Auto:
    def __init__(self, reg, huippunopeus):
        self.reg = reg
        self.huippunopeus = huippunopeus
    def print(self):
        print(f"rekisteritunnus on: {self.reg}, huippunopeus: {self.huippunopeus} Km/h")


class Sahkoauto(Auto):
    def __init__(self, reg, huippunopeus, kapasitekw):
        super().__init__(reg, huippunopeus)
        self.kapasitekw = kapasitekw
    def print(self):
        super().print()
        print(f"akkukapasiteeti: {self.kapasitekw} Kwh")

class Polttomoottoriauto(Auto):
    def __init__(self, reg, huippunopeus, kapasitel):
        super().__init__(reg, huippunopeus)
        self.kapasitel = kapasitel
    def print(self):
        super().print()
        print(f"bensatankinkapasiteeti: {self.kapasitel} L")

auto1 = Sahkoauto("abv-968", 180, 65)
auto2 = Polttomoottoriauto("bib-987", 280, 60)

auto1.print()
auto2.print()

matka = auto1.huippunopeus * 3
print(matka)