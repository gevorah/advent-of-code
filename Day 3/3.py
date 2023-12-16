import re

def engine(text: str):
  cols = text.find('\n') + 1
  result = 0
  for value in re.finditer(r'\d+', text):
    left = value.start() - 1
    if left < 0 or text[left] == '\n': # \n1.+
      left += 1

    right = value.end()
    if right >= len(text) or text[right] == '\n': # +.1\n
      right -= 1

    top = list(range(left - cols, right - cols + 1))
    bottom = list(range(left + cols, right + cols + 1))

    search = top + bottom + [left, right]

    for symbol in re.finditer(r'[^\n\.\d]', text):
      if symbol.start() in search:
        result += int(value.group())
        break

  return result


with open('Day 3/input', 'r') as f:
  text = ''.join(f.readlines())
  print(engine(text))