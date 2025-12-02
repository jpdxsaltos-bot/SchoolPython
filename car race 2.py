import random


class Car:
    def __init__(self, registration_number, max_speed):
        self.registration_number = registration_number
        self.max_speed = max_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate(self, change):
        self.current_speed += change
        if self.current_speed > self.max_speed:
            self.current_speed = self.max_speed
        elif self.current_speed < 0:
            self.current_speed = 0

    def drive(self, hours):
        self.travelled_distance += self.current_speed * hours

cars = []
for i in range(1, 11):
    max_speed = random.randint(100, 200)
    car = Car(f"ABC-{i}", max_speed)
    cars.append(car)

race_distance = 10000
hours = 0

while True:
    for car in cars:
        speed_change = random.randint(-10, 15)
        car.accelerate(speed_change)
        car.drive(1)

    hours += 1
    finished = any(car.travelled_distance >= race_distance for car in cars)
    if finished:
        break

print(f"{'Reg':<10} {'Max Speed':<10} {'Curr Speed':<12} {'Distance':<10}")
for car in cars:
    print(f"{car.registration_number:<10} {car.max_speed:<10} {car.current_speed:<12} {car.travelled_distance:<10}")