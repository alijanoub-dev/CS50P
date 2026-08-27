def main():
    
    expression = input("Expression: ").strip()

    x, y, z = expression.split(" ")

    x = float(x)
    z = float(z)

    match y:
        case "+":
            result = x + z
        case "-":
            result = x - z
        case "*":
            result = x * z
        case "/":
            result = x / z

    print(f"{result:.1f}")

        
main()