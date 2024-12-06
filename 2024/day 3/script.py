import re

def compute(memory):
  pattern = re.compile(r'mul\((\d+),(\d+)\)')
  instructions = pattern.findall(memory)
  return sum(int(a) * int(b) for a, b in instructions)

def compute_enhanced(memory):
  pattern = re.compile(r'don\'t\(\).*?do\(\)', flags=re.DOTALL)
  memory = pattern.sub('', memory)
  return compute(memory)

with open("input", "r") as f:
  content = f.read()
  print(compute(content))
  print(compute_enhanced(content))
