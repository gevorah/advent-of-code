import re


def calibration(text: str):
    regex = r"\d"
    values = re.findall(regex, text)
    return int(values[0] + values[-1])


def calibrationEnhanced(text: str):
    digits = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    regex = r"(?=(\d|" + "|".join(digits) + "))"
    values = re.findall(regex, text)

    first = values[0] if values[0].isdigit() else str(digits.index(values[0]) + 1)
    last = values[-1] if values[-1].isdigit() else str(digits.index(values[-1]) + 1)
    return int(first + last)


with open("day 1/input", "r") as f:
    result = 0
    for line in f.readlines():
        result += calibrationEnhanced(line)
    print(result)
