import re
from functools import cmp_to_key

def compute(hands: str, cmp):
  split_regex = r'(\w{5}) (\d+)'
  hands, bids = zip(*re.findall(split_regex, hands))
  hands = zip(hands, map(int, bids), [count(hand) for hand in hands])
  srt_hands = sorted(hands, key=cmp_to_key(cmp))
  return sum(rank * bid for rank, (_,bid,_) in enumerate(srt_hands, 1))

def count(hand: str):
  counter = {}
  for card in hand:
    counter[card] = counter.get(card, 0) + 1
  key = lambda item: (item[0], item[1])
  return {k:v for k, v in sorted(counter.items(), key=key)}

def cmp_hands(a, b):
  cards = '23456789TJQKA'

  cnt_a = sorted(a[2].values(), reverse=True)
  cnt_b = sorted(b[2].values(), reverse=True)
  
  return cmp(cards, a[0], b[0], cnt_a, cnt_b)

def cmp_hands_enhanced(a, b):
  cards = 'J23456789TQKA'

  cnt_a, cnt_b = a[2], b[2]
  cnt_a[max(cnt_a, key=cnt_a.get)] += cnt_a.pop('J', 0)
  cnt_b[max(cnt_b, key=cnt_b.get)] += cnt_b.pop('J', 0)

  cnt_a = sorted(cnt_a.values(), reverse=True)
  cnt_b = sorted(cnt_b.values(), reverse=True)

  return cmp(cards, a[0], b[0], cnt_a, cnt_b)

def cmp(cards: str, hand_a: list, hand_b: list, cnt_a: list[int], cnt_b: list[int]):
  if cnt_a != cnt_b:
    if max(cnt_a, cnt_b) == cnt_a: return 1
    if min(cnt_a, cnt_b) == cnt_a: return -1

  for card_a, card_b in zip(hand_a, hand_b):
    if card_a == card_b: continue
    idx_a, idx_b = cards.index(card_a), cards.index(card_b)
    if idx_a > idx_b: return 1
    if idx_a < idx_b: return -1

with open('Day 7/test', 'r') as f:
  file = f.read()
  print(compute(file, cmp_hands))
  print(compute(file, cmp_hands_enhanced))
