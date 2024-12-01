import re

def parse_input(file):
  regex = r'(\d+)\s+(\d+)'
  matches = re.findall(regex, file)

  left, right = zip(*matches)
  left = list(map(int, left))
  right = list(map(int, right))

  return left, right

def calculate_distance(file):
  left, right = parse_input(file)
  pairs = zip(sorted(left), sorted(right))
  return sum(abs(a - b) for a, b in pairs)

def calculate_similarity_score(file):
  left, right = parse_input(file)
  return sum(x * right.count(x) for x in left)

with open("input", "r") as f:
  file = f.read()
  print(calculate_distance(file))
  print(calculate_similarity_score(file))