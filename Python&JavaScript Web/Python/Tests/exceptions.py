import sys

while True:
    try:  
        x = int(input("x: "))
        y = int(input("y: "))

        try:
            result = x / y
        except ZeroDivisionError:
            print("Error: Cannot divide by 0.")
            continue

    except ValueError:
        print("Error: Invalid input.")
        continue

    print(f"{x} / {y} = {result}")