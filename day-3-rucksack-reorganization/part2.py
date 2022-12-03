import string

letters = string.ascii_lowercase + string.ascii_uppercase
item_priorities = {l: i for i, l in enumerate(letters, start=1)}

priority_sum = 0
with open("day-3-rucksack-reorganization/input.txt", encoding="utf8") as f:
    rucksacks = f.readlines()
    for i in range(3, len(rucksacks) + 3, 3):
        group = rucksacks[i - 3:i]

        item = next(iter(set(group[0].strip()).intersection(group[1].strip(), group[2].strip())))
        priority_sum += item_priorities[item]

print(priority_sum)
