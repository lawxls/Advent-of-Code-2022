calories = []
with open("day-1-calorie-counting/input.txt", encoding="utf8") as f:
    elf_cal = 0
    for line in f:
        try:
            elf_cal += int(line)
        except ValueError:
            calories.append(elf_cal)
            elf_cal = 0

print(sum(sorted(calories)[-3:]))
