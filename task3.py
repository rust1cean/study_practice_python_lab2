import numpy as np
from tabulate import tabulate


def get_matrix_size_from_input(file_name: str) -> tuple[int, int]:
    """
    Parse arguments from file by specified format:
    N=3, M=4
    """
    with open(file_name, "r") as file:
        try:
            args = file.read().replace(" ", "").split(",")
            args_dict = dict([x.strip().split("=") for x in args])

            n = int(args_dict["N"])
            m = int(args_dict["M"])

            return n, m

        except ValueError:
            raise ValueError("Cannot process arguments as integers.")

        except:
            raise ValueError("N or M was not specified.")


def main():
    n, m = get_matrix_size_from_input("input.txt")

    with open("result.txt", "w") as output:
        # Create NxM matrix 'A' with size random integers
        a_matrix = np.random.randint(low=n**m, size=(n, m))
        output.write("Matrix 'A':\n")
        output.write(tabulate(a_matrix))

        # Subtract each line's smallest value
        a_matrix = [row - np.min(row) for row in a_matrix]
        output.write("\n\nMatrix 'A' after subtracting by smallest value:\n")
        output.write(tabulate(a_matrix))

        # Create NxM matrix 'B'
        b_matrix = np.random.randint(low=n**m, size=(n, m))
        output.write("\n\nMatrix 'B':\n")
        output.write(tabulate(b_matrix))

        # Create NxM matrix 'C' where C = B - A
        c_matrix = b_matrix - a_matrix
        output.write("\n\nMatrix 'C', where C = B - A:\n")
        output.write(tabulate(c_matrix))


if __name__ == "__main__":
    main()
