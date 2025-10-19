import random

class Car:
    def __init__(self, registration_number, maximum_speed):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate(self, change):
        new_speed = self.current_speed + change
        if new_speed > self.maximum_speed:
            self.current_speed = self.maximum_speed
        elif new_speed < 0:
            self.current_speed = 0
        else:
            self.current_speed = new_speed

    def drive(self, hours):
        self.travelled_distance += self.current_speed * hours

def print_cars(cars):
    print(f"{'Reg. No.':<10} {'Max Speed':<10} {'Current Speed':<15} {'Distance':<10}")
    for car in cars:
        print(f"{car.registration_number:<10} {car.maximum_speed:<10} {car.current_speed:<15} {car.travelled_distance:<10.2f}")

cars = []
for i in range(1, 11):
    max_speed = random.randint(100, 200)
    reg_num = f"ABC-{i}"
    cars.append(Car(reg_num, max_speed))

race_finished = False
hour = 0

while not race_finished:
    hour += 1
    for car in cars:
        speed_change = random.randint(-10, 15)
        car.accelerate(speed_change)
        car.drive(1)
        if car.travelled_distance >= 10000:
            race_finished = True
    print(f"\n--- After hour {hour} ---")
    print_cars(cars)

print("\nRace finished!")
print_cars(cars)
