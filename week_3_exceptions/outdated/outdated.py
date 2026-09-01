def main():
    months = [
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ]

    while True:
        date = input("Date: ").strip()
        
        if "/" in date:
            try:
                m, d, y = map(int, date.split("/"))
                
                if 1 <= m <= 12 and 1 <= d <= 31:
                    print(f"{y:04}-{m:02}-{d:02}")
                    break

            except ValueError:
                pass

        elif "," in date:
            try:
                month_name, day, y = date.replace(",", "").split()

                if month_name in months:
                    m = months.index(month_name) + 1
                    d, y = int(day), int(y)

                    if 1 <= d <= 31:
                        print(f"{y:04}-{m:02}-{d:02}")
                        break

            except ValueError:
                pass

main()