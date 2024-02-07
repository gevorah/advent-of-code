import re
import math

def compute(paper: str):
  times, records = paper.split('\n')
  times = map(int, re.findall(r'\d+', times))
  records = map(int, re.findall(r'\d+', records))

  ways = []
  for time, record in zip(times, records):
    ways.append(beatIt(time, record))
  
  return math.prod(ways)

def beatIt(time, record):
  # -hold^2 + time*hold = record
  delta = time**2 - (-4*-record)
  x1 = math.ceil((-time + math.sqrt(delta)) / -2)
  x2 = math.ceil((-time - math.sqrt(delta)) / -2)

  d1 = -x1**2 + time*x1
  if d1 == record: x1 += 1

  return x2 - x1

def computeEnhanced(paper: str):
  time, record = paper.split('\n')
  time = int(re.sub(r'[^\d+]', '', time))
  record = int(re.sub(r'[^\d+]', '', record))

  return beatIt(time, record)

with open('Day 6/input', 'r') as f:
  file = f.read()
  print(compute(file))
  print(computeEnhanced(file))
