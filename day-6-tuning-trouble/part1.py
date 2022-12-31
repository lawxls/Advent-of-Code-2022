with open("day-6-tuning-trouble/input.txt", "r") as f:
    string = f.readlines()[0]
    for wrap, i in enumerate(range(len(string)), start=4):

        if len(set(string[i:wrap])) != 4:
            continue

        print(i + 4)
        break
