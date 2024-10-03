class Car:
    def __init__(self, name, horse_power, top_speed):
        self.name: str = name
        self.horse_power: int = horse_power
        self.top_speed: int = top_speed
        self.speed: int = 0

    def show_parameters(self) -> None:
        print(f"Car {self.name} has {self.horse_power}hp and top speed of {self.top_speed}km/h")
        
    def throttle(self, speed: int) -> None:
        self.speed += speed

        if self.speed > self.top_speed:
            self.speed = self.top_speed
        if self.speed < 0:
            self.speed = 0

        print(self.speed)