def main():
    UserInput = input()
    print(convert(UserInput))

def convert(text):
    return text.replace(":)", "🙂").replace(":(", "🙁")

main()
