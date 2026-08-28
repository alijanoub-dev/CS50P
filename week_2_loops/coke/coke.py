def main():
    amount_due = 50

    while amount_due > 0:
        print(f"Amount Due: {amount_due}")
        insert_coin = int(input("Insert Coin: "))

        if insert_coin in [25, 10, 5]:
            amount_due -= insert_coin

    print(f"Change Owed: {abs(amount_due)}")

main()