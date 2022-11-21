class Hissi:
    def __init__(self, eka, vika, tamahetkinen):
        self.eka = eka
        self.vika = vika
        self.tamahetkinen = 1

    def mene_ylos(self):
        self.tamahetkinen += 1

    def mene_alas(self):
        self.tamahetkinen -= 1

    def mene(self, kerros):
        if kerros > self.vika or kerros < self.eka:
            print(f"ei ole kerrosta {kerros}")
            return True
        else:
            while self.tamahetkinen != kerros:
                if self.tamahetkinen < kerros:
                    Hissi.mene_ylos(self)
                elif self.tamahetkinen:
                    Hissi.mene_alas(self)
            print(f"Hissi on siirtynyt kerrokseen: {self.tamahetkinen}")

hissi = Hissi(1, 10, 1)
hissi.mene(10)
hissi.mene(1)