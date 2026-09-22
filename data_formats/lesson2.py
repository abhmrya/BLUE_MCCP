import csv

with open("data/users.csv", newline="") as file:
    reader = csv.reader(file)

    for row in reader:
        print(row)