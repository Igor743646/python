import random
from random import randint

class Game_Field():

	def __init__(self, size):
		self.size = size
		self.field = [[["?", "0"] for i in range(size)] for j in range(size)]
		number_of_bomb = round(0.2*size*size) if size<10 else round(0.09*size*size)
		coordinates_of_bombs = [[randint(0, size-1), randint(0, size-1)] for i in range(number_of_bomb)]

		def uniq_elements(lst):
			for i in lst:
				if lst.count(i)>1: return False
			return True

		while uniq_elements(coordinates_of_bombs) is False:
			coordinates_of_bombs = [[randint(0, size-1), randint(0, size-1)] for i in range(number_of_bomb)]

		for i in coordinates_of_bombs:
			self.field[i[0]][i[1]][1]="@"
			if i[0]!=0 and i[1]!=0 and self.field[i[0]-1][i[1]-1][1]!='@': self.field[i[0]-1][i[1]-1][1] = str(int(self.field[i[0]-1][i[1]-1][1])+1)  
			if i[0]!=0 and self.field[i[0]-1][i[1]][1]!='@': self.field[i[0]-1][i[1]][1] = str(int(self.field[i[0]-1][i[1]][1])+1) 
			if i[1]!=0 and self.field[i[0]][i[1]-1][1]!='@': self.field[i[0]][i[1]-1][1] = str(int(self.field[i[0]][i[1]-1][1])+1) 
			if i[0]!=0 and i[1]!=self.size-1 and self.field[i[0]-1][i[1]+1][1]!='@': self.field[i[0]-1][i[1]+1][1] = str(int(self.field[i[0]-1][i[1]+1][1])+1) 
			if i[0]!=self.size-1 and i[1]!=0 and self.field[i[0]+1][i[1]-1][1]!='@': self.field[i[0]+1][i[1]-1][1] = str(int(self.field[i[0]+1][i[1]-1][1])+1) 
			if i[1]!=self.size-1 and self.field[i[0]][i[1]+1][1]!='@': self.field[i[0]][i[1]+1][1] = str(int(self.field[i[0]][i[1]+1][1])+1) 
			if i[0]!=self.size-1 and self.field[i[0]+1][i[1]][1]!='@': self.field[i[0]+1][i[1]][1] = str(int(self.field[i[0]+1][i[1]][1])+1) 
			if i[0]!=self.size-1 and i[1]!=self.size-1 and self.field[i[0]+1][i[1]+1][1]!='@': self.field[i[0]+1][i[1]+1][1] = str(int(self.field[i[0]+1][i[1]+1][1])+1) 

	def print_playermatr(self):
		for i in self.field:
			for j in i:
				print(j[0] + " ", end='')
			print()
		print()

	def print_debugmatr(self):
		for i in self.field:
			for j in i:
				print(j[1] + " ", end='')
			print()
		print()

	def open_cell(self, x, y):
		if x<0 or x>self.size-1 or y<0 or y>self.size-1: 
			print ("Неправильные координаты")
			return True
		self.field[x][y][0] = self.field[x][y][1]
		if self.field[x][y][0]=='@':
			print ("Вы проиграли. Попробуйте ещё!")
			return False
		if self.field[x][y][0]=='0':
			if x!=0 and y!=0: self.field[x-1][y-1][0] = self.field[x-1][y-1][1]  
			if x!=0: self.field[x-1][y][0] = self.field[x-1][y][1]
			if y!=0: self.field[x][y-1][0] = self.field[x][y-1][1]
			if x!=0 and y!=self.size-1: self.field[x-1][y+1][0] = self.field[x-1][y+1][1] 
			if x!=self.size-1 and y!=0: self.field[x+1][y-1][0] = self.field[x+1][y-1][1]
			if y!=self.size-1: self.field[x][y+1][0] = self.field[x][y+1][1]
			if x!=self.size-1: self.field[x+1][y][0] = self.field[x+1][y][1]
			if x!=self.size-1 and y!=self.size-1: self.field[x+1][y+1][0] = self.field[x+1][y+1][1]
		return True


SIZE = int(input("Введите размер поля: ")) 

Game = Game_Field(SIZE)

GAMEOVER = True
while GAMEOVER:
	
	MENU = int(input("Введите команду: ")); print("")

	if MENU == 0:
		GAMEOVER = False

	if MENU == 1:
		Game.print_playermatr()

	if MENU == 2:
		print ("Правила игры и меню")

	if MENU == 3:
		GAMEOVER = Game.open_cell(int(input("Введите x: ")), int(input("Введите y: ")))
		print()
		Game.print_playermatr()

	if MENU == 4:
		Game.print_debugmatr()