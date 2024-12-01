import re

def calculate(lists):
  regex = r'(\d+)\s+(\d+)'
  matches = re.findall(regex, lists)

  left, right = zip(*matches)
  left = list(map(int, left))
  right = list(map(int, right))
  
  pairs = zip(sorted(left), sorted(right))
  return sum(abs(a - b) for a, b in pairs)

with open("input", "r") as f:
  file = f.read()
  print(calculate(file))