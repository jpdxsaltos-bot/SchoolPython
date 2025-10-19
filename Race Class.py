import random

class Car:
    def __init__(self, registration_number, max_speed):
        self.registration_number = registration_number
        self.max_speed = max_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate(self, change_speed):
        self.current_speed += change_speed
        if self.current_speed > self.max_speed:
            self.current_speed = self.max_speed
        if self.current_speed < 0:
            self.current_speed = 0

    def drive(self, hours):
        self.travelled_distance += self.current_speed * hours

class Race:
    def __init__(self, name, distance_km, cars):
        self.name = name
        self.distance_km = distance_km
        self.cars = cars

    def hour_passes(self):
        for car in self.cars:
            change = random.randint(-10, 15)
            car.accelerate(change)
            car.drive(1)

    def print_status(self):
        print(f"Race: {self.name} - Distance: {self.distance_km} km")
        print(f"{'Reg. No':<10} {'Max Speed':<10} {'Current Speed':<14} {'Distance':<10}")
        for car in self.cars:
            print(f"{car.registration_number:<10} {car.max_speed:<10} {car.current_speed:<14} {car.travelled_distance:<10.2f}")

    def race_finished(self):
        for car in self.cars:
            if car.travelled_distance >= self.distance_km:
                return True
        return False

def main():
    cars = []
    for i in range(1, 11):
        max_speed = random.randint(100, 200)
        reg_num = f"ABC-{i}"
        cars.append(Car(reg_num, max_speed))

    race = Race("Grand Demolition Derby", 8000, cars)

    hours_passed = 0
    while not race.race_finished():
        race.hour_passes()
        hours_passed += 1
        if hours_passed % 10 == 0:
            race.print_status()
            print()
    race.print_status()

if __name__ == "__main__":
    main()
