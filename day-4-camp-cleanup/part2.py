count = 0
with open("day-4-camp-cleanup/input.txt", encoding="utf8") as f:
    for line in f:
        range1, range2 = line.strip().split(",")
        r1 = tuple(int(i) for i in range1.split("-"))
        r2 = tuple(int(i) for i in range2.split("-"))

        set1 = set(range(r1[0], r1[1] + 1))
        set2 = set(range(r2[0], r2[1] + 1))

        if set1.intersection(set2):
            count += 1

print(count)
