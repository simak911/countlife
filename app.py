from flask import Flask, render_template, request
import requests
from waitress import serve
import os
import random
import csv
import hashlib

def gethash(name, year):
    input_str = f"{name}-{year}"
    hash_bytes = hashlib.sha256(input_str.encode('utf-8')).digest()
    hash_int = int.from_bytes(hash_bytes[:4], 'big')
    result = 50 + (hash_int % 61)
    return result

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
        print(year,y,name,n,editstring(name) == editstring(n), year == y, type(year), type(y))
        if (year == y and editstring(name) == editstring(n)):
            return line['result']
    return gethash(name, year)

app = Flask(__name__)
@app.route('/')
def get_main_page():
    return render_template('index.html')

@app.route('/calc')
def get_calculation():
    try: 
        name = request.args.get('name')
        year = numberize(request.args.get('year'))
        age = calculate(name, year)
        return {'status': 'valid', 'age': age}
    except:
        return {'status': 'invalid'}

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    serve(app, host="0.0.0.0", port=port)