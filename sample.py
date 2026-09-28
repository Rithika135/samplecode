# sample.py

def greet(name):
    return f"Hello, {name}!"


def add_numbers(a, b):
    return a + b


def main():
    name = input("Enter your name: ")

    print(greet(name))

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    result = add_numbers(num1, num2)

    print(f"The sum is: {result}")


if __name__ == "__main__":
    main()