pick_score_dict = {"X": 1, "Y": 2, "Z": 3}
result_score_dict = {
    "A-X": 3, "A-Y": 6, "A-Z": 0, "B-X": 0, "B-Y": 3, "B-Z": 6, "C-X": 6, "C-Y": 0, "C-Z": 3
}

total_score = 0
with open("day-2-rock-paper-scissors/input.txt", encoding="utf8") as f:
    for line in f:
        p1, p2 = line.split()
        pick_score = pick_score_dict[p2]
        result_score = result_score_dict[f"{p1}-{p2}"]
        total_score += (pick_score + result_score)

print(total_score)
