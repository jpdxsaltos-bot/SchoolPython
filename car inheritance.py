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

def main():
    e_car = ElectricCar("ABC-15", 180, 52.5)
    g_car = GasolineCar("ACD-123", 165, 32.3)

    e_car.accelerate(60)
    e_car.drive(3)
    g_car.accelerate(80)
    g_car.drive(3)

    print(f"Electric Car {e_car.registration_number} travelled {e_car.travelled_distance} km")
    print(f"Gasoline Car {g_car.registration_number} travelled {g_car.travelled_distance} km")

if __name__ == "__main__":
    main()
