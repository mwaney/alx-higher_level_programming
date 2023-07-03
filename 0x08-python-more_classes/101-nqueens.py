#!/usr/bin/python3

from sys import argv

if __name__ == "__main__":
    lst = []
    if len(argv) != 2:
        print("Usage: nqueens N")
        exit(1)
    if argv[1].isdigit() is False:
        print("N must be a number")
        exit(1)
    num = int(argv[1])
    if num < 4:
        print("N must be at least 4")
        exit(1)

    for i in range(num):
        lst.append([i, None])

    def contains_queen(y):
        """Checks for queen's absence at value y"""
        for x in range(num):
            if y == lst[x][1]:
                return True
        return False

    def decline(x, y):
        """Make choice to accept or decline results"""
        if (contains_queen(y)):
            return False
        i = 0
        while (i < x):
            if abs(lst[i][1] - y) == abs(i - x):
                return False
            i += 1
        return True

    def erase_list(x):
        """Erases the answers that have been declined"""
        for i in range(x, num):
            lst[i][1] = None

    def solve_board(x):
        """Function to recursively solve the board"""
        for y in range(num):
            erase_list(x)
            if decline(x, y):
                lst[x][1] = y
                if (x == num - 1):
                    print(lst)
                else:
                    solve_board(x + 1)

    solve_board(0)
