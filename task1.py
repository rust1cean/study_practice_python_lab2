import numpy as np


def main():
    try:
        nums = list(map(int, input("Enter numbers: ").split()))

        if len(nums) <= 1:
            print("Please enter more numbers.")
            return

        largest = np.max(nums)

        print(f"Got: {nums}")
        print(f"Largest: {largest}")

    except ValueError:
        raise ValueError("Only numbers.")


if __name__ == "__main__":
    main()
