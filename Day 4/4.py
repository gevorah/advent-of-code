import re

def scratchcard(card: str):
  split_regex = r'(?:\d+\s+)+\d+|\d+'
  card, wins, nums = re.findall(split_regex, card)

  find_regex = r'\b(?:' + re.sub('\s+', '|', wins) + r')\b'
  matches = re.findall(find_regex, nums)

  return len(matches)

def points(file):
  result = 0
  for line in file.readlines():
    result += int(2 ** (scratchcard(line) - 1))
  return result

with open('Day 4/test', 'r') as f:
  print(points(f))
