# coding: utf8

import bs4
from bs4 import BeautifulSoup
import requests
import random
from random import randint

url = 'https://mail.ru/'
A = True
Spisok = []


while A:
	request = requests.get(url)
	bs = BeautifulSoup(request.text, "html.parser")
	Headers = bs.findAll("a", {"class": "news__list__item__link"})

	for i in Headers:
		if len(i.findAll("span"))!=0 and (i.findAll("span")[0].text + ":  " + i["href"] in Spisok) == False:
			text = i.findAll("span")[0].text + ":  " + i["href"]
			Spisok.append(text)
			# print (text + "\n")
			savefile = open('MailNewsParcer.txt', 'a')
			savefile.write(text + "\n")
			savefile.close()


