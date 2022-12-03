import string

letters = string.ascii_lowercase + string.ascii_uppercase
item_priorities = {l: i for i, l in enumerate(letters, start=1)}

priority_sum = 0
with open("day-3-rucksack-reorganization/input.txt", encoding="utf8") as f:
    for line in f:
        items = line.strip()
        first_half = items[:len(items) // 2]
        second_half = items[len(items) // 2:]

        item = next(iter(set(first_half).intersection(second_half)))
        priority_sum += item_priorities[item]

print(priority_sum)
