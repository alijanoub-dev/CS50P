def main():
    x, y = get_two_int()
    fuel_percentage = round((x / y) * 100)

    if fuel_percentage >= 99:
        print("F")
    elif fuel_percentage <= 1:
        print("E")
    else:
        print(f"{fuel_percentage}%")


def get_two_int():
    while True:
        try:
            user_input = input("Fraction: ").split("/")
            x = int(user_input[0])
            y = int(user_input[1])

        except (ValueError, ZeroDivisionError, IndexError):
            pass

        else:
            if x <= y:
                return x, y


if __name__ == "__main__":
    main()