import re
from functools import cmp_to_key

def compute(hands: str):
  split_regex = r'(\w{5}) (\d+)'
  hands, bids = zip(*re.findall(split_regex, hands))
  hands = zip(hands, map(int, bids), [count(hand) for hand in hands])
  srt_hands = sorted(hands, key=cmp_to_key(cmp_hands))
  return sum(rank * bid for rank, (_,bid,_) in enumerate(srt_hands, 1))

def count(hand: str):
  counter = {}
  for card in hand:
    counter[card] = counter.get(card, 0) + 1
  return sorted(counter.values(), reverse=True)

def cmp_hands(a, b):
  cards = '23456789TJQKA'

  cnt_a, cnt_b = a[2], b[2]
  if cnt_a != cnt_b:
    if max(cnt_a, cnt_b) == cnt_a: return 1
    if min(cnt_a, cnt_b) == cnt_a: return -1
  
  for card_a, card_b in zip(a[0], b[0]):
    if card_a == card_b: continue
    idx_a, idx_b = cards.index(card_a), cards.index(card_b)
    if idx_a > idx_b: return 1
    if idx_a < idx_b: return -1

with open('Day 7/input', 'r') as f:
  file = f.read()
  print(compute(file))
