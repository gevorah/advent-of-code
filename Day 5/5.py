import re
from functools import reduce

def compute(seed, ranges):
  for values in ranges.split('\n'):
    dst, src, i = map(int, re.findall(r'\d+', values))
    if src <= seed < src + i:
      return dst + (seed - src)
  return seed

def decipher(almanac: str):
  split_regex = r'(?:\d+\s)+\d+'
  seeds, *maps = re.findall(split_regex, almanac)

  seeds = list(map(int, re.findall(r'\d+', seeds)))

  return min(reduce(compute, maps, int(seed)) for seed in seeds)

with open('Day 5/input', 'r') as f:
  file = f.read()
  print(decipher(file))