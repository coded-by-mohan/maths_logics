# A simple program which prints any table fron 1 to N continuously
while True :
    n = input("which table you want ? or type x to quit: ")
    if n.lower() == "x":
        print("program stopped")
        break
    if n.isdigit():
        n = int(n)
        for i in range (1,11):
            print(f"{n} X {i} = {n*i}")

    else:
        print(" enter a valid number or type x to quit")