from flask import Flask, render_template, request
import requests
from waitress import serve
import os
import random
import csv


def numberize(text):
    try:
        return int(text)
    except:
        return 0

def readit():
    f = open('./data/table.csv', encoding = 'utf-8')
    r = csv.reader(f, delimiter=';')
    lines = []
    for line in r:
        lines.append({'name': line[0], 'year': numberize(line[1]), 'result': numberize(line[2])})
    return lines

def editstring(text):
    text = text.replace(" ", "").lower()
    return text

def calculate(name, year):
    lines = readit()
    for line in lines:
        n = line['name'] 
        y = line['year']
        if (year == y and editstring(name) == editstring(n)):
            return line['result']
    return random.randint(50,110)

app = Flask(__name__)
@app.route('/')
def get_main_page():
    return render_template('index.html')

@app.route('/calc')
def get_calculation():
    try: 
        name = request.args.get('name')
        year = request.args.get('year')
        age = calculate(name, year)
        return {'status': 'valid', 'age': age}
    except:
        return {'status': 'invalid'}


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    serve(app, host="0.0.0.0", port=port)