import requests
import os
from pprint import pprint
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv('API_KEY')

city = input('Enter a City: ')
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather?appid='+str(API_KEY)+"&q="+city

weather_data = requests.get(BASE_URL).json()
pprint(weather_data)