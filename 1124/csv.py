f = open("data.csv ", "r")

for line in f.readlines():
    line = line.strip()

    print(line)
    parts = line.split(",")

    for part in parts:
        print(" ", part)