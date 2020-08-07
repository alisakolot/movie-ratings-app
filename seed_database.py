"""Script to seed database."""

import os 
import json
from random import choice, randint
from datetime import datetime

import crud
import model
import server

os.system('dropdb ratings')
# More code will go here

os.system('dropdb ratings')
os.system('createdb ratings')


with.open('data/movies.json') as f:
    movie_data = json.loads(f.read())
    