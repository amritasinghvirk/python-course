def add_numbers(a, b):
    """Return the sum of two numbers."""
    return a + b


def main():
    try:
        x = float(input("Enter the first number: "))
        y = float(input("Enter the second number: "))
    except ValueError:
        print("Please enter valid numbers.")
        return

    result = add_numbers(x, y)
    print(f"The sum is: {result}")


if __name__ == "__main__":
    main()
