def main():
    user_input = input("Input: ").strip()
    new_user_input = ""

    for letter in user_input:
        if letter.lower() not in ["a", "e", "i", "o", "u"]:
            new_user_input += letter

    print(f"Output: {new_user_input}")

if __name__ == "__main__":
    main()