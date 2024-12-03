import re

def parse_input(file):
  regex = r'\d+'
  matches = [list(map(int, re.findall(regex, report))) for report in file.split('\n')]
  return matches

def analyze(file):
  reports = parse_input(file)
  count = 0
  for report in reports:
    is_ascending = None
    for a, b in zip(report, report[1:]):
      diff = a - b
      if not is_valid(diff, is_ascending):
        is_ascending = None
        break
      is_ascending = (diff < 0)
    count += is_ascending is not None
  return count
  
def is_valid(diff, is_ascending):
  if 0 < diff <= 3:
    return is_ascending is not True
  elif -3 <= diff < 0:
    return is_ascending is not False
  return False

with open("input", "r") as f:
  file = f.read()
  print(analyze(file))