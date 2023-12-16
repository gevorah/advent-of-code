import re

def scratchcard(text: str):
  split_regex = r'(?:\d+\s+)+\d+|\d+'
  card, wins, nums = re.findall(split_regex, text)

  find_regex = r'\b(?:' + re.sub('\s+', '|', wins) + r')\b'
  matches = re.findall(find_regex, nums)

  return int(2 ** (len(matches) - 1))

with open('Day 4/input', 'r') as f:
  result = 0
  for line in f.readlines():
    result += scratchcard(line)
  
  print(result)