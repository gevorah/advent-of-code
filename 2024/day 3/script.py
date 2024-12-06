import re

def parse_input(file):
  pattern = re.compile(r'mul\((\d+)\,(\d+)\)')
  matches = pattern.findall(file)
  return [(int(a), int(b)) for a, b in matches]

def compute(instructions):
  return sum(a * b for a, b in instructions)

with open("input", "r") as f:
  instructions = parse_input(f.read())
  print(compute(instructions))
