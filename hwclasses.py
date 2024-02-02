class Car :
    def __init__(self, mdl, brd, ful,clr):
        self.model = mdl
        self.brand = brd
        self.fuel = ful
        self.color = clr

    def set_color(self, clr):
        self.color = clr

    def get_color(self):
        return self.color

    def show_car(self):
        print(self.model)
        print(self.brand)
        print(self.fuel)
        print(self.color)

class suv(Car):
    def __init__(self,to,tn):
        self.turbo = to
        self.transmission = tn
    

car = Car("BMW i5 M60 xDrive","BMW","Electric","black")

q = int(input("Would you like to display the full specs of the car? Or do you want to view the spec specifically? 1 = full 0 = specefic: "))

if q == 1:
    car.show_car()

if q == 0:
    qtwo = int(input("Which specs do you want to view specifically? 1 = Model 2 = brand 3 = fuel 4 = color: "))

if qtwo == 1:
    print(car.model)

if qtwo == 2:
    print(car.brand)

if qtwo == 3:
    print(car.fuel)

if qtwo == 4:
    print(car.color)




           

        