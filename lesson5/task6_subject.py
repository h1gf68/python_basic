result = {}
with open("task6_subject", "r") as subject:
    for line in subject:
        sub = line.split(":")
        numbers = ''.join(filter(lambda s: (s.isdigit() or s == ' '), sub[1]))
        result[sub[0]] = sum([int(i) for i in numbers.split()])

print(result)
