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

class ElectricCar(Car):
    def __init__(self, registration_number, max_speed, battery_capacity):
        super().__init__(registration_number, max_speed)
        self.battery_capacity = battery_capacity

class GasolineCar(Car):
    def __init__(self, registration_number, max_speed, tank_volume):
        super().__init__(registration_number, max_speed)
        self.tank_volume = tank_volume

class Race:
    def __init__(self, name, distance, cars):
        self.name = name
        self.distance = distance
        self.cars = cars

    def hour_passes(self):
        for car in self.cars:
            speed_change = random.randint(-10, 15)
            car.accelerate(speed_change)
            car.drive(1)

    def print_status(self):
        print(f"Race: {self.name}")
        print(f"{'Reg No.':10} {'Max Speed':10} {'Current Speed':15} {'Distance Travelled':20}")
        for car in self.cars:
            print(f"{car.registration_number:10} {car.max_speed:<10} {car.current_speed:<15} {car.travelled_distance:<20.2f}")
        print()

    def race_finished(self):
        for car in self.cars:
            if car.travelled_distance >= self.distance:
                return True
        return False

def exercise_9():
    print("Exercise 9: Basic Car class demo")
    car = Car("ABC-123", 142)
    car.accelerate(30)
    car.accelerate(70)
    car.accelerate(50)
    print(f"Current speed after accelerations: {car.current_speed} km/h")
    car.accelerate(-200)
    print(f"Speed after emergency brake: {car.current_speed} km/h\n")

def exercise_10():
    print("Exercise 10: Basic Car Race simulation")
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

    print(f"Race finished after {hour} hours.")
    print(f"{'Reg No.':10} {'Max Speed':10} {'Current Speed':15} {'Distance Travelled':20}")
    for car in cars:
        print(f"{car.registration_number:10} {car.max_speed:<10} {car.current_speed:<15} {car.travelled_distance:<20.2f}")
    print()

def exercise_10_extended():
    print("Exercise 10 Extended: Race class simulation")
    cars = []
    for i in range(1, 11):
        max_speed = random.randint(100, 200)
        reg_num = f"ABC-{i}"
        cars.append(Car(reg_num, max_speed))

    race = Race("Grand Demolition Derby", 8000, cars)
    hours = 0

    while not race.race_finished():
        race.hour_passes()
        hours += 1
        if hours % 10 == 0:
            race.print_status()

    race.print_status()
    print(f"Race finished after {hours} hours.\n")

def exercise_11b():
    print("Exercise 11B: Car inheritance with ElectricCar and GasolineCar")
    e_car = ElectricCar("ABC-15", 180, 52.5)
    g_car = GasolineCar("ACD-123", 165, 32.3)

    e_car.accelerate(60)
    e_car.drive(3)
    g_car.accelerate(80)
    g_car.drive(3)

    print(f"Electric Car {e_car.registration_number} travelled {e_car.travelled_distance} km with battery {e_car.battery_capacity} kWh")
    print(f"Gasoline Car {g_car.registration_number} travelled {g_car.travelled_distance} km with tank volume {g_car.tank_volume} liters\n")

def main():
    exercise_9()
    exercise_10()
    exercise_10_extended()
    exercise_11b()

if __name__ == "__main__":
    main()
