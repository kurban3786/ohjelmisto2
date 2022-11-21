class Car:

    def __init__(self, regnumber, topspd):
        self.regnumber = regnumber
        self.topspd = topspd
        self.speed = 0
        self.odometer = 0


car1 = Car("abc-123", 142)
print(
    f"liscence plate: {car1.regnumber}, top speed: {car1.topspd}, current speed: {car1.speed}, distance travelled: {car1.odometer}.")
