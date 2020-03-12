Allfoodlist = []
keys = []

import csv
import random

with open('food.csv', 'r', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=';')
    for y, line in enumerate(reader):
        for x, ingredient in enumerate(line):
            if y == 0:
                keys.append(ingredient)
                Allfoodlist.append([])
            if y > 0:
                Allfoodlist[x].append((ingredient))

for i, category in enumerate(Allfoodlist):
    category = list(filter(None, category))
    category = [ingredient.capitalize() for ingredient in category]
    Allfoodlist[i] = category
