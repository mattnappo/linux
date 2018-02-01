# -*- coding: utf-8 -*-
import os, sys, random, walls
class Room():
	def __init__(self, room, location, TYPE):
		self.values = []
		self.room = room
		self.TYPE = TYPE
		self.strength = False
		self.hack = False
		self.fix = False
		self.location = location
		for x in range(5):
			self.values.append([])
			for y in range(4):
				self.values[x].append("[ ]")
	def regenerate(self):
		for x in range(len(self.values)):
			for y in range(len(self.values[x])):
				self.values[x][y] = "[" + chr(random.randint(65, 90)) + "]"
		for x in range(10):
			self.values[random.randint(0, 4)][random.randint(0,3)] = "[" + self.TYPE + "]"
	def startSplitter(self, OPEN, CLOSE):
		for x in range(len(self.values)):
			for y in range(len(self.values[x])):
				self.values[x][y] = OPEN + chr(random.randint(65, 90)) + CLOSE
		for x in range(10):
			self.values[random.randint(0, 4)][random.randint(0,3)] = OPEN + self.TYPE + CLOSE
		self.printer()
	def start(self):
		if self.strength == True:
			self.startSplitter("{", "}")
		else:
			self.startSplitter("[", "]")
	def boarder(self):
		os.system("clear")
		print("╔══════════════════════╗")
		print("║ "+self.room+" LOCATED AT "+self.location+" ║")
		print("╚══════════════════════╝")
		print("╔═════════════════╗")
		print("║ "+self.values[0][0]+" "+self.values[0][1]+" "+self.values[0][2]+" "+self.values[0][3]+" ║")
		print("║ "+self.values[1][0]+" "+self.values[1][1]+" "+self.values[1][2]+" "+self.values[1][3]+" ║")
		print("║ "+self.values[2][0]+" "+self.values[2][1]+" "+self.values[2][2]+" "+self.values[2][3]+" ║")
		print("║ "+self.values[3][0]+" "+self.values[3][1]+" "+self.values[3][2]+" "+self.values[3][3]+" ║")
		print("║ "+self.values[4][0]+" "+self.values[4][1]+" "+self.values[4][2]+" "+self.values[4][3]+" ║")
		print("╚═════════════════╝")
	def printboard(self):
		if self.hack == True:
			for x in range(100):
				self.regenerate()
				self.boarder()
			os.system("clear")
			print("╒══ ══════ ════ ══  ═╗")
			print(" │ S6\%oa l0C4Xt1q    ║")
			print("╚═══█ ════ ════|══  ══╒")
			print("╔ ═════| ═════ |═  ═╒")
			print("║ |X|X |X||X|     ║")
			print(" | |X| |X||X| |X|   ║")
			print("║ |X| |X||X| |X| ║")
			print("║ |X| |X| |X| |X| ║")
			print("| |XX|  |X| |X| ║")
			print("╚════ ;════'═════ #%═══╝")

			print("You have hacked this room!")
			while True:
				x = input("Would you like to [F]ix this room, or [D]estroy the system? ")
				if x == "F" or x == "f":
					self.fix = True
					self.hack = False
					self.printboard()
				elif x == "D" or x == "d":
					print("GOODBYE!!!")
					break
			self.hack = False
			self.fix = False
		elif self.fix == True:
			for x in range(100):
				self.regenerate()
				self.boarder()
		else:
			self.boarder()
	def printer(self):
		self.printboard()
		while True:
			x = input("Would you like to [R]egenerate, [C]hange strength, [H]ack, or [E]xit this " + self.room + "? ")
			if x == "R" or x == "r":
				self.start()
			elif x =="C" or x == "c":
				if self.strength == True:
					self.strength = False
				else:
					self.strength = True
				self.start()
			elif x == "H" or x == "h":
				if self.strength == True:
					print("This room cannot be hacked! It is too strong!")
				else:
					if self.hack == True:
						self.start()
					else:
						self.hack = True
						self.start()
			elif x == "E" or x == "e":
				game.where()
				break
class Game():
	def __init__(self):
		self.board = []
		self.rooms = []
		self.xcoord = 0
		self.ycoord = 0
		self.loc = ""
		self.roomNumber = 0
		# create board
		for x in range(3):
			self.board.append([])
			for y in range(3):
				self.board[x].append("[ ]")
	def printerFOR(self):
		os.system("clear")
		for y in range(len(self.board), 0, -1):
			for x in range(len(self.board[y])):
				print(self.board[y][x], end="")
			print()
	def printer(self):
		os.system("clear")
		print("3	" + self.board[2][0], end="")
		print(self.board[2][1], end="")
		print(self.board[2][2])

		print("2	" + self.board[1][0], end="")
		print(self.board[1][1], end="")
		print(self.board[1][2])

		print("1	" + self.board[0][0], end="")
		print(self.board[0][1], end="")
		print(self.board[0][2])
		print("         1  2  3 ")
	def where(self):
		while True:
			os.system("clear")
			what = input("[B]uild or [I]nspect? ")
			if what == "B" or what == "b":
				self.build()
			elif what == "I" or what == "i":
				self.inspect()
				self.where()
	def inspect(self):
		self.printer()
		place = input("Where would you like to inspect\nformat: x-coord:y-coord? ")
		xcoord = int(place[0])-1
		ycoord = int(place[2])-1


# WORK ON THIS CODE TO SAVE THE VAULT OBJ TO THE LIST
# EVENTUALLY MAKE IT SAVE TO A TEXT FILE
		if self.board[ycoord][xcoord] == "[$]":
			room = self.rooms[0]
			room.start()
		elif self.board[ycoord][xcoord] == "[#]":
			room = self.rooms[0]
			room.start()



		elif self.board[ycoord][xcoord] == "[ ]":
			print("That spot is empty!")
		else:
			print("Didn't find that location")
	def build(self):
		while True:
			'''PUT TRY STATEMENT HERE'''
			self.printer()
			place = input("Welcome! Where would you like to build\nformat: x-coord:y-coord? ")
			self.xcoord = int(place[0])-1
			self.ycoord = int(place[2])-1
			self.placer()
	def placer(self):
		while True:
			TYPE = input("Would you like to build a [V]ault, or a [S]ecret room? ")
			if TYPE == "V" or TYPE == "v" or TYPE == "Vault" or TYPE == "vault":
				self.board[self.ycoord][self.xcoord] = "[$]"
				self.loc = str(self.xcoord+1) + ":" + str(self.ycoord+1)
				room = Room("VAULT", self.loc, "$")
				self.rooms.append(room)
				room.start()
				break
			elif TYPE == "S" or TYPE == "s" or TYPE == "Secret room" or TYPE == "Secret Room" or TYPE == "secret room":
				self.board[self.ycoord][self.xcoord] = "[#]"
				self.loc = str(self.xcoord+1) + ":" + str(self.ycoord+1)
				room = Room("SROOM", self.loc, "#")
				self.rooms.append(room)
				room.start()
				break
			else:
				print("What was that? ")
		self.printer()
		self.where()
game = Game()
game.where()
