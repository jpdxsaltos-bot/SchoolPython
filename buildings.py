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

    def go_to_floor(self, target_floor):
        while self.current_floor != target_floor:
            if self.current_floor < target_floor:
                self.floor_up()
            elif self.current_floor > target_floor:
                self.floor_down()

class Building:
    def __init__(self, bottom_floor, top_floor, num_elevators):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.elevators = []
        for i in range(num_elevators):
            self.elevators.append(Elevator(bottom_floor, top_floor))

    def run_elevator(self, elevator_number, target_floor):
        if 0 <= elevator_number < len(self.elevators):
            print(f"Running elevator {elevator_number} to floor {target_floor}")
            self.elevators[elevator_number].go_to_floor(target_floor)
        else:
            print("Invalid elevator number")

    def fire_alarm(self):
        print("Fire alarm activated! Returning all elevators to bottom floor.")
        for i, elevator in enumerate(self.elevators):
            print(f"Elevator {i} going to bottom floor")
            elevator.go_to_floor(self.bottom_floor)

def main():
    building = Building(0, 10, 3)

    building.run_elevator(0, 5)
    building.run_elevator(1, 8)
    building.run_elevator(2, 3)

    building.fire_alarm()

if __name__ == "__main__":
    main()
