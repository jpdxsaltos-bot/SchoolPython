class Elevator:
    def __init__(self, bottom_floor, top_floor):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.current_floor = bottom_floor

    def floor_up(self):
        if self.current_floor < self.top_floor:
            self.current_floor += 1
            print(f"Elevator is now at floor {self.current_floor}")

    def floor_down(self):
        if self.current_floor > self.bottom_floor:
            self.current_floor -= 1
            print(f"Elevator is now at floor {self.current_floor}")

    def go_to_floor(self, floor):
        while self.current_floor != floor:
            if self.current_floor < floor:
                self.floor_up()
            else:
                self.floor_down()

class Building:
    def __init__(self, bottom_floor, top_floor, number_of_elevators):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.elevators = [Elevator(bottom_floor, top_floor) for _ in range(number_of_elevators)]

    def run_elevator(self, elevator_number, destination_floor):
        if 1 <= elevator_number <= len(self.elevators):
            print(f"Running elevator {elevator_number} to floor {destination_floor}")
            self.elevators[elevator_number - 1].go_to_floor(destination_floor)
        else:
            print("Invalid elevator number.")

    def fire_alarm(self):
        print("Fire alarm activated! Moving all elevators to bottom floor.")
        for i, elevator in enumerate(self.elevators, start=1):
            elevator.go_to_floor(self.bottom_floor)
            print(f"Elevator {i} has reached bottom floor.")


building = Building(0, 10, 3)
building.run_elevator(1, 5)
building.run_elevator(2, 7)
building.run_elevator(3, 3)
building.run_elevator(1, 0)
building.fire_alarm()
