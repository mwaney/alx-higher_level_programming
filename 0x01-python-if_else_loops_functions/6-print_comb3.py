#!/usr/bin/python3
for i in range(0, 10):
    for j in range(i + 1, 10):
        comb = f"{i}{j}"
        if i == 8 and j == 9:
            print(comb)
        else:
            print(comb, end = ", ")
