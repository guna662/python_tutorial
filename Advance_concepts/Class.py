# Creating bluePrint

class ToyCar:
    def __init__(self, color, speed,brand):
        self.color = color
        self.speed = speed
        self.brand=brand

    def show_details(self):
        print(f"This toy car is {self.color} and runs at {self.speed} km/h brand is {self.brand}")

# creating toys based on blue print
car1=ToyCar("red",20,"audi")
car2=ToyCar("white",60,"tata")


car1.show_details()
car2.show_details()