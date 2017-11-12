print("please give two numbers, I'll divide them.")
print("enter 'q' to quit.")

while True:
    a = input("\nfirst one, a = ")
    if a == 'q' or a == 'Q':
        break
    b = input("second one, b = ")

    try:
        result = int(a) / int(b)
    except ValueError:
        print("Please input numeric values!")
    except ZeroDivisionError:
        print("Second argument to a division or modulo operation was zero!")
    else:
        print("divide result: " + str(result))
