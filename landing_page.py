import csv
import random
import re

from flask import Flask

app = Flask(__name__)

def parse_vocab():
  with open('vocab.csv') as csv_file:
      csv_reader = csv.reader(csv_file, delimiter=',')
      line_count = 0
      res = []
      for row in csv_reader:
          elements = re.split(r"\t+", row[0])
          res.append((elements[0], elements[1]))
  return res



@app.route('/')
def hello():
    return 'Hello, World!'