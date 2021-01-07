import bs4
from bs4 import BeautifulSoup
import requests
import random
from random import randint
import json

def GetPicture(search):
	url = 'https://www.google.com/search?q=' + search + '&tbm=isch'
	request = requests.get(url)
	bs = BeautifulSoup(request.text, "html.parser")
	AllImages = bs.findAll("img")
	return AllImages[randint(1, len(AllImages))]['src']
	
