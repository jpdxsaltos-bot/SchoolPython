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
        distance = self.current_speed * hours
        self.travelled_distance += distance

def print_car_details(car, title="Car details"):
    print(f"\n=== {title} ===")
    print("Registration number:", car.registration_number)
    print("Maximum speed:", car.maximum_speed, "km/h")
    print("Current speed:", car.current_speed, "km/h")
    print("Travelled distance:", car.travelled_distance, "km")

car = Car("ABC-123", 142)

print_car_details(car, "Before any acceleration or driving")

car.accelerate(30)
print_car_details(car, "After accelerating by +30 km/h")

car.accelerate(70)
print_car_details(car, "After accelerating by +70 km/h")

car.accelerate(50)
print_car_details(car, "After accelerating by +50 km/h")

car.accelerate(-200)
print_car_details(car, "After emergency brake (-200 km/h)")

car.accelerate(100)
car.drive(1.5)
print_car_details(car, "After accelerating to 100 km/h and driving 1.5 hours")

car.accelerate(-50)
car.drive(2)
print_car_details(car, "After slowing down by 50 km/h and driving 2 hours")
