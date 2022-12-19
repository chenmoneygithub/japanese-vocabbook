import csv
import random
import re

from flask import Flask, render_template, request

app = Flask(__name__)

def parse_vocab():
    with open('vocab.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        res = []
        for row in csv_reader:
            elements = re.split(r"\t+", row[0])
            res.append((elements[0], elements[1]))
    return res



@app.route('/', methods=['GET', 'POST'])
def index():
    vocabs = parse_vocab()
    if request.method == 'POST':
        if request.form.get('action1') == 'VALUE1':
            return render_template('index.html', vocabs=vocabs)
    elif request.method == 'GET':
        return render_template('index.html', vocabs=[])