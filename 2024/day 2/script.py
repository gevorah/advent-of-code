import re

def parse_input(file):
  regex = r'\d+'
  matches = [list(map(int, re.findall(regex, line))) for line in file.split('\n')]
  return matches

def is_safe(report, tolerance=0):
  for i, (a, b) in enumerate(zip(report, report[1:])):
    if not 1 <= a - b <= 3:
      if tolerance == 0: return False
      return any(is_safe(report[:j] + report[j+1:], tolerance - 1) for j in (i, i+1))
  return True

def analyze(reports, tolerance=0):
  count = 0
  for report in reports:
    if is_safe(report, tolerance) or is_safe(report[::-1], tolerance):
      count += 1
  return count

with open("input", "r") as f:
  reports = parse_input(f.read())
  print(analyze(reports))
  print(analyze(reports, 1))