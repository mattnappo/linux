"""MAKE CARS.DLL READ FROM THE <CAR>.DLL FILE, INSTEAD OF ONLY WRITING WHEN CAR IS CREATED."""
"""MAKE OPTION TO REMOVE CAR"""
import os
class Car():
	def __init__(self):
		self.all = []
		self.cars = []
		self.list = []
	def printSummaries(self):
		print()
		print("Cars currently inventoried: ")
		with open("cars.dll", "r") as xFile:
			strList = xFile.readlines()
			for x in range(len(strList)):
				print(strList[x], end="")
			print()
	def loadInventory(self):
		while True:
			self.printSummaries()
			carChoice = input("Which car would you like to view (please give car number)? Or [E]xit? ")
			if os.path.isfile(carChoice + ".dll") == True:
				xxx = carChoice + ".dll"
				with open(xxx, "r") as xFile:

					strList = xFile.read()
					strList = str(strList)
					strList = strList[1:-1]
					for x in strList:
						if x == ",":
							strList = strList.replace(x, '')
						if x == "'":
							strList = strList.replace(x, '')
						self.list = strList.split(" ")
					for items in self.list:
						self.all.append(items)
					self.printCar()
				while True:
					changeLog = input("Would you like to change anything? [D]elete car? ")
					if changeLog == "yes" or changeLog == "y":
						changeWhat = eval(input("Change [1]Year, [2]Make, [3]Model, [4]Color, [5]Rims, [6]Tires, [7]Interior, [8]Price, [9]Dealer, [10]Registration, [11]Notes and comments? "))
						changeTo = input("Change current " + self.all[changeWhat] + " to what? ")
						self.all[changeWhat] = changeTo
						fff = self.all[0] + ".dll"
						os.remove(fff)
						with open(fff, "w") as xFile:
							xFile.write(str(self.all))
							print("Car " + self.all[0] + " successfully updated.")
					elif changeLog == "D" or changeLog == "d":
						xFileCab = self.all[0] + ".dll"
						os.remove(xFileCab)
						print("Car successfully Deleted.")
					elif changeLog == "no" or changeLog == "n":
						break
			elif carChoice == "E" or carChoice == "e" or carChoice == "Exit" or carChoice == "exit":
				break
			else:
				print("That car number is invalid!")
				break
	def printCar(self):
		print("Car Number: "+self.all[0])
		print("Year: "+self.all[1])
		print("Make: "+self.all[2])
		print("Model: "+self.all[3])
		print("Color: "+self.all[4])
		print("Rims and Brakes: "+self.all[5])
		print("Tires: "+self.all[6])
		print("Interior: "+self.all[7])
		print("Price: "+self.all[8])
		print("Dealer: "+self.all[9])
		print("Registration: "+self.all[10])
		print("Notes and comments: " + self.all[11] + "\n")
		input("Press Enter to Continue")

	def saveCar(self):
		htg0 = self.all[0]+".dll"
		with open(htg0, "w") as xFile:
			xFile.write(str(self.all))
		with open("cars.dll", "a") as xFile:
			VARCHAR = " "
			xFile.write(self.all[0] + VARCHAR + self.all[1] + VARCHAR + self.all[2] + VARCHAR + self.all[3])
			xFile.write("\n")
		print("Car " + self.all[0] + " successfully added to inventory.")

	def cSaveCar(self):
		while True:
			confirm = input("Do you want to review car before adding to inventory? ")
			if confirm == "y" or confirm == "yes":
				os.system("cls")
				self.printCar()
				self.saveCar()
				break
			elif confirm == "n" or confirm == "no":
				os.system("cls")
				self.saveCar()
				break

	def buildCar(self): 
	    carNumber = input("Enter car number: ")
	    year = input("Enter year: ")
	    make = input("Enter make: ")
	    model = input("Enter model: ")
	    color = input("Enter color: ")
	    rims = input("Enter type of rims and brakes: ")
	    tires = input("Enter type of tires: ")
	    interior = input("Enter interior: ")
	    price = input("Enter price: ")
	    dealer = input("Enter name of dealer: ")
	    registration = input("Enter registration number: ")
	    notes = input("Any other notes or comments: ")
	    self.all = [carNumber, year, make, model, color, rims, tires, interior, price, dealer, registration, notes]
	    self.cSaveCar()

while True:
    action = input("Welcome! Would you like to [V]iew inventory or [A]dd car: ")
    if action == "V" or action == "v":
        car = Car()
        car.loadInventory()
    elif action == "A" or action == "a":
        car = Car()
        car.buildCar()