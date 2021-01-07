import bs4
from bs4 import BeautifulSoup
import requests
from GetPicture import GetPicture
import random
from random import randint
import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.upload import VkUpload
import json
from io import BytesIO

class ChatBot():

	def __init__(self, user_id, vk):
		self.vk = vk
		self._USER_ID = user_id
		self._USER_NAME = self._get_user_name_from_vk_id(user_id)
		self._commands = [['привет', 'хай', 'хэлоу', 'здарово', 'здравствуйте', 'здравствуй']]

	def _get_user_name_from_vk_id(self, user_id):
		request = requests.get("https://vk.com/id"+str(user_id))
		bs = bs4.BeautifulSoup(request.text, "html.parser")
		user_name = self._get_last_first_name(bs.findAll("title")[0])
		return user_name.split()[0]

	def new_message(self, message):

		#Приветствие
		if message.lower() in self._commands[0]:
			a = ("Привет, " + self._USER_NAME + "!") if self._USER_ID!=139711346 else "Лера!Лера!Лера!Лера!Лера!Лера!Лера!Лера!Лера!Лера!Лера!Лера!Лера!Лера!Лера!"
			return {'user_id': self._USER_ID, 'message': a, 'random_id': randint(-100000, 100000)}

		#Стоп-слово
		elif message.lower() == 'стоп':
			import dgbvgd
		else:
			return {'user_id': self._USER_ID, 'message': "Не понимаю о чем ты...", 'random_id': randint(-100000, 100000)}

		#


	@staticmethod
	def _get_last_first_name(tegs_str):
		res = ""
		for i in tegs_str.get_text():
			if i == ' ':
				break
			else:
				res+=i 
		return res
