class Car:
    def __init__(self, registration_number, max_speed):
        self.registration_number = registration_number
        self.max_speed = max_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate(self, change):
        self.current_speed += change
        if self.current_speed < 0:
            self.current_speed = 0
        elif self.current_speed > self.max_speed:
            self.current_speed = self.max_speed

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

def main():
    electric = ElectricCar("ABC-15", 180, 52.5)
    gasoline = GasolineCar("ACD-123", 165, 32.3)

    electric.accelerate(100)
    gasoline.accelerate(120)

    electric.drive(3)
    gasoline.drive(3)

    print(f"Electric car {electric.registration_number} travelled {electric.travelled_distance} km with {electric.battery_capacity} kWh battery")
    print(f"Gasoline car {gasoline.registration_number} travelled {gasoline.travelled_distance} km with {gasoline.tank_volume} L tank")

if __name__ == "__main__":
    main()
