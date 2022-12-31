with open("day-6-tuning-trouble/input.txt", "r") as f:
    string = f.readlines()[0]
    for wrap, i in enumerate(range(len(string)), start=14):

        if len(set(string[i:wrap])) != 14:
            continue

        print(i + 14)
        break
