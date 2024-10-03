from car import Car

def main():
    car1: Car = Car("Skoda", 260, 165)
    car1.show_parameters()
    car1.throttle(-50)
    car1.throttle(500000)

if __name__ == "__main__":
    main()