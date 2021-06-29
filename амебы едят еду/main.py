import pygame, sys, time, os
import random

def sign(x):
	return x/abs(x) if x!=0 else 0

def rand(a, b):
	return random.randint(a, b)

def draw_score(surf, text, size, x, y):
    font = pygame.font.Font(pygame.font.match_font('arial'), size)
    text_surface = font.render(text, True, (0, 0, 0))
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)

class Ameba():
	ID = 0
	def __init__(self, x, y, size):
		self.id = Ameba.ID; Ameba.ID+=1
		self.x = x; self.y = y; self.size = size
		self.ameba = pygame.Surface((size,size))
		self.ameba.fill((255,0,0))

		self.scores = 0
		self.visibility = 50
		self.age = 0 

	def print(self):
		print (self.x, self.y, self.size)

	def get_data(self):
		return self.ameba

	def get_coordinates(self):
		return int(self.x), int(self.y)

	def set_coordinates(self, x, y, MAX_WIDTH, MAX_HIGHT):
		if x>0 and x+self.size<=MAX_WIDTH:
			self.x = x
		elif x<=0:
			self.x = 0
		else:
			self.x = MAX_WIDTH-self.size
		if y>0 and y+self.size<=MAX_HIGHT:
			self.y = y
		elif y<=0:
			self.y = 0
		else:
			self.y = MAX_HIGHT-self.size

	def get_x(self):
		return self.x
	
	def get_y(self):
		return self.y

	def get_scores(self):
		return self.scores

	def set_scores(self, a):
		self.scores = a

	def get_visability(self):
		return self.visibility

	def set_visability(self, a):
		self.visibility = a

	def get_age(self):
		return self.age

	def set_age(self, a):
		self.age = a

class Food():
	ID = 0
	def __init__(self, tupple, size):
		self.id = Food.ID; Food.ID+=1
		self.x = tupple[0]; self.y = tupple[1]; self.size = size
		self.food = pygame.Surface((size,size))
		self.food.fill((0,0,0))

	def __str__(self):
		return '({}, {})'.format(self.x, self.y)

	def get_data(self):
		return self.food

	def get_coordinates(self):
		return self.x, self.y

	def get_x(self):
		return self.x
	
	def get_y(self):
		return self.y

	def get_id(self):
		return self.id


class II():

	def game(self):
		pygame.init()

		FLAG = True
		PRESSKEY = False
		MAX_WIDTH = 1280
		MAX_HIGHT = 720
		AMEBA_COUNT = 20
		PAUSE = False

		amebas = []
		foods = []

		for i in range(AMEBA_COUNT):
			amebas.append(Ameba(rand(0, 1270), rand(0, 710), 5))

		window = pygame.display.set_mode((MAX_WIDTH, MAX_HIGHT))
		screen=pygame.Surface((MAX_WIDTH, MAX_HIGHT))

		while FLAG:
			for e in pygame.event.get():
				# выход из игры
				if e.type == pygame.QUIT:
					FLAG=False
				# пауза по нажатию на пробел
				if e.type == pygame.KEYDOWN:
					if e.key == 32:
						PAUSE = not PAUSE
				# ручное добавление пищи мышью
				if e.type == 5: #mousekeydown
					foods.append(Food(pygame.mouse.get_pos(), 5))

			if not PAUSE:
				screen.fill((255, 255, 255))
				# случайное добавление еды
				if random.randint(-3, 3)==3:
					foods.append(Food((rand(0, 1270), rand(0, 710)), 5))

				# прорисовка еды и удаление той, что находится под амебами
				for food in foods:
					for a in amebas:
						if a.get_coordinates() == food.get_coordinates():
							a.set_scores(a.get_scores()+1)
							foods.pop(foods.index(food)); break
						else:
							screen.blit(food.get_data(), food.get_coordinates())

				# прорисовка амеб и их движение
				for a in amebas:

					# размножение
					if a.get_scores()==10:
						amebas.append(Ameba(a.get_x(), a.get_y(), 5))
						amebas[-1].set_visability(int(a.get_visability()*random.uniform(0.1,2)))
						a.set_scores(0)

					# повышение возраста
					a.set_age(a.get_age()+0.1)
					if a.get_age()>=rand(200, 500):
						amebas.pop(amebas.index(a)); break

					# движение и поведение амеб
					if len(foods)==0:
						a.set_coordinates(a.get_x()+rand(-1, 1), a.get_y()+rand(-1, 1), MAX_WIDTH, MAX_HIGHT)
					else:
						def nearest_food_index():
							min_food_index_and_dist = ()
							for food in foods:
								lenth = abs(a.get_x()-food.get_x())+abs(a.get_y()-food.get_y())
								mas1 = (foods.index(food), lenth)
								if min_food_index_and_dist == () or min_food_index_and_dist[1] > lenth:
									min_food_index_and_dist = mas1

							return min_food_index_and_dist[0]

						a_nearest_food_index = nearest_food_index()
						def lenx():
							if 0 < abs(a.get_x()-foods[a_nearest_food_index].get_x()) < a.get_visability():
								return (sign(a.get_x()-foods[a_nearest_food_index].get_x())) 
							else:
								return random.randint(-1, 1)
						def leny():
							if 0 < abs(a.get_y()-foods[a_nearest_food_index].get_y()) < a.get_visability():
								return (sign(a.get_y()-foods[a_nearest_food_index].get_y())) 
							else:
								return random.randint(-1, 1)

						a.set_coordinates(a.get_x()-lenx(), a.get_y()-leny(), MAX_WIDTH, MAX_HIGHT)

					screen.blit(a.get_data(), a.get_coordinates())
					pygame.draw.circle(screen, (230, 50, 230), a.get_coordinates(), a.get_visability(), 1)	

				draw_score(screen, "Бактерии: " + str(len(amebas)), 18, 1200, 700)
				window.blit(screen, (0, 0))

			pygame.display.update()

		pygame.quit()

A = II()
A.game()