scores = {
    "Kim": [80, 90, 70],
    "Lee": [100, 90, 85],
    "Park": [95, 85, 100]
}

averages = {name: sum(score) / len(score) for name, score in scores.items()}
print(averages)

names = [name for name, avg in averages.items() if avg >= 90]
print(names)