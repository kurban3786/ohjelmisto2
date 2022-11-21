import random


class Car:
    def __init__(self, regnumber, topspd):
        self.regnumber = regnumber
        self.topspd = topspd
        self.speed = 0
        self.odometer = 0

    def accelerate(self, delta_speed):
        if self.topspd > self.speed + delta_speed > 0:
            self.speed = self.speed + delta_speed
        elif self.speed + delta_speed > self.topspd:
            self.speed = self.topspd
        else:
            self.speed = 0

    def matka(self, tunti):
        self.odometer = tunti * self.speed + self.odometer


cars = []
for i in range(10):
    cars.append(Car(f"ABC-{i+1}", random.randint(100, 200)))

someonewon = False
while not someonewon:
    for car in cars:
        car.accelerate(random.randint(-10, 15))
        car.matka(1)
        if car.odometer >= 10000:
            print(f"{car.regnumber} has won the race, the race lasted  hours.")
            someonewon = True
            break

