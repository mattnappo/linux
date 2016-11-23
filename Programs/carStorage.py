class Car():
    def __init__(self):
				self.all = []
    
    def printCar(self):
        print("Car Number: "+self.carNumber)
        print("Make: "+self.make)
        print("Model: "+self.model)
        print("Year: "+self.year)
        print("Color: "+self.color)
        print("Rims: "+self.rims)
        print("Wheels: "+self.wheels)
        print("Interior: "+self.interior)
        print("Price: "+self.price)
        print("Dealer: "+self.dealer)
        print("Registration: "+self.registration)

        print("Summary for " + self.carNumber + ": ")
        for x in self.all:
            print(x, end=" ")
        input("Press Enter to Continue")

    def saveCar():
        with open(self.carNumber, "w") as xFile:
            xfile.write(self.all)
        print("Car number " + self.carNumber + " successfully added to inventory.")

    def cSaveCar(self):
        while True:
            confirm = input("Do you want to review car before adding to inventory? ")
            if confirm == "y" or "yes":
                self.printCar()
                self.saveCar()
            elif confirm == "n" or "no":
                self.saveCar()

    def buildCar(self): 
        carNumber = input("Enter car number: ")
        make = input("Enter make: ")
        model = input("Enter model: ")
        year = input("Enter year: ")
        color = input("Enter color: ")
        rims = input("Enter type of rims: ")
        wheels = input("Enter type of wheels: ")
        interior = input("Enter interior: ")
        price = input("Enter price: ")
        dealer = input("Enter name of dealer: ")
        registration = input("Enter registration number: ")
        self.all  

while True:
    action = input("Welcome! Would you like to [V]iew inventory or [A]dd car: ")
    if action == "V" or action == "v":
        print()
    elif action == "A" or action == "a":
        car = Car()
        car.buildCar()