result_score_dict = {"X": 0, "Y": 3, "Z": 6}
pick_score_dict = {
    "A-X": 3, "A-Y": 1, "A-Z": 2, "B-X": 1, "B-Y": 2, "B-Z": 3, "C-X": 2, "C-Y": 3, "C-Z": 1
}

total_score = 0
with open("day-2-rock-paper-scissors/input.txt", encoding="utf8") as f:
    for line in f:
        p1, p2 = line.split()
        result_score = result_score_dict[p2]
        pick_score = pick_score_dict[f"{p1}-{p2}"]
        total_score += (pick_score + result_score)

print(total_score)
