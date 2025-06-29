import numpy as np


def create_row(size: int, shift: int):
    row = np.zeros(size, dtype=int)
    row[shift] = 1
    row[size - shift - 1] = 1

    return row


def main():
    n = int(input("Enter matrix size: "))

    if n < 0:
        raise ValueError("Only positive numbers :)")

    matrix = [create_row(n, i) for i in range(n)]

    for row in matrix:
        print(row)


if __name__ == "__main__":
    main()
