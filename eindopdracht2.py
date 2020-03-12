from flask import Flask, url_for
from flask import render_template
from flask import abort
from markupsafe import escape
app = Flask(__name__)
from getfoods import *
import random

def getrandom(l):
    randomvalues = []
    for ingredient in Allfoodlist:
        ingredient = random.choice(ingredient)
        randomvalues.append(ingredient)
    return randomvalues

@app.route('/')
def getindexhtml():
    return render_template('index.html', 
    Allfoodlist = Allfoodlist,
    len = len(keys),
    key = keys,
    value = getrandom(Allfoodlist))

@app.route('/attributes')
def getattributeshtml():
    return render_template('attributes.html',
    Allfoodlist = Allfoodlist,
    len = len(keys),
    key = keys,
    value = getrandom(Allfoodlist))

@app.route('/attributes/<category>')
def getcategoryhtml(category):  

    for i, categories in enumerate(keys):
        if category in categories:
            y = i
            break

    if category in keys:
        return render_template("attributes.html", 
        len = len(keys),
        category = category, 
        key = keys,
        Allfoodlist = Allfoodlist,
        y = y)

    else:
        return abort(404)