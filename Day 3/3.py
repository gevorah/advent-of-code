import re

def engine(text: str):
  for value in re.finditer(r'\d+', text):
    print(value)  



with open('Day 3/test', 'r') as f:
  text = ''.join(f.readlines())
  engine(text)