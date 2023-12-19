import re

def decipher(almanac: list[str]):
  split_regex = r'(?:\d+\s)+\d+'
  seeds, *maps = re.findall(split_regex, ''.join(almanac))

  seeds = list(map(int, re.findall(r'\d+', seeds)))
  
  lowest = []

  for seed in seeds:
    for ranges in maps:
      for values in ranges.split('\n'):
        dst, src, i = list(map(int, re.findall(r'\d+', values)))
        if src <= seed < src + i:
          seed = dst + (seed - src)
          break
    lowest.append(seed)
  
  lowest.sort(reverse=True)
  return lowest.pop()

with open('Day 5/input', 'r') as f:
  file = f.readlines()
  print(decipher(file))