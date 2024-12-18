import re
from functools import reduce
import sys


def decipher(almanac: str):
    split_regex = r"(?:\d+\s)+\d+"
    seeds, *maps = re.findall(split_regex, almanac)

    seeds = list(map(int, re.findall(r"\d+", seeds)))

    return min(compute_loc(int(seed), maps) for seed in seeds)


def compute_loc(seed, maps):
    return reduce(compute_dst, maps, seed)


def compute_dst(seed, ranges):
    for values in ranges.split("\n"):
        dst, src, length = map(int, re.findall(r"\d+", values))
        if src <= seed < src + length:
            return dst + (seed - src)
    return seed


def decipher_enhanced(almanac: str):
    split_regex = r"(?:\d+\s)+\d+"
    seeds, *maps = re.findall(split_regex, almanac)

    seeds = re.findall(r"\d+\s\d+", seeds)

    locations = []
    for seed in seeds:
        start, length = map(int, re.findall(r"\d+", seed))
        locations.append(quick_search(start, length, maps))

    return min(locations)


def quick_search(start, length, maps):
    queue = [(start, length)]
    minLoc = sys.maxsize

    while queue:
        start, length = queue.pop()
        step = length // 2
        middle = start + step

        left = compute_loc(start, maps)
        mid = compute_loc(middle, maps)
        right = compute_loc(start + length, maps)

        minLoc = min(minLoc, left, mid, right)

        if length == 1:
            continue

        if left + step != mid:
            queue.append((start, step))

        if mid + (length - step) != right:
            queue.append((middle, length - step))

    return minLoc


with open("day 5/input", "r") as f:
    file = f.read()
    print(decipher(file))
    print(decipher_enhanced(file))
