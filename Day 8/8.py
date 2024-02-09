import re
import math


def decipher(file: str):
    split_regex = r"\w+"
    inst, *nodes = re.findall(split_regex, file)
    nodes = {k: v for k, *v in zip(nodes[::3], nodes[1::3], nodes[2::3])}
    return inst, nodes


def compute(instructions: str, network: dict, start: str, end: str):
    pos = start
    steps = 0

    while True:
        for direction in instructions:
            if pos.endswith(end):
                return steps

            if direction == "L":
                pos = network[pos][0]
            else:
                pos = network[pos][1]

            steps += 1


def compute_enhanced(instructions: str, network: dict, start: str, end: str):
    start_keys = [key for key in network.keys() if key.endswith(start)]

    return math.lcm(
        *[compute(instructions, network, start_key, end) for start_key in start_keys]
    )


with open("Day 8/input", "r") as f:
    file = f.read()
    instructions, network = decipher(file)
    print(compute(instructions, network, "AAA", "ZZZ"))
    print(compute_enhanced(instructions, network, "A", "Z"))
