class Car:
    def __init__(self, regnumber, topspd):
        self.regnumber = regnumber
        self.topspd = topspd
        self.speed = 0
        self.odometer = 0
        print("uusi auto luotettu")

    def accelerate(self, delta_speed):
        if self.topspd > self.speed + delta_speed > 0:
            self.speed = self.speed + delta_speed
        elif self.speed + delta_speed > self.topspd:
            self.speed = self.topspd
        else:
            self.speed = 0

    def matka(self, tunti):
        self.odometer = tunti * self.speed + self.odometer


car1 = Car("abc-123", 142)
car1.accelerate(30)
car1.accelerate(70)
car1.accelerate(50)
print(f"Current speed is {car1.speed}")
car1.odometer = 2000
car1.matka(5)
print(f"Current travel is {car1.odometer}")
