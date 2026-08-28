def main():
    camel_case = input("camelCase: ").strip()
    snake_case = ""

    for letter in camel_case:
        if letter.isupper():
            if snake_case == "":
                snake_case += letter.lower()
            else:
                snake_case += "_" + letter.lower()
        else:
            snake_case += letter

    print(f"snake_case: {snake_case}")

main()