count = 0
with open("day-4-camp-cleanup/input.txt", encoding="utf8") as f:
    for line in f:
        range1, range2 = line.strip().split(",")
        r1 = tuple(int(i) for i in range1.split("-"))
        r2 = tuple(int(i) for i in range2.split("-"))

        if r1[0] >= r2[0] and r1[1] <= r2[1]:
            count += 1
            continue

        if r2[0] >= r1[0] and r2[1] <= r1[1]:
            count += 1

print(count)
