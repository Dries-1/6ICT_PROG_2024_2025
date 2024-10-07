def vergelijker(x, y):
    "PRINT of x groter, kleiner of gelijk is aan y"
    if x > y:
        print(f"{x} is groter dan {y}")
    elif x < y:
        print(f"{x} is kleiner dan {y}")
    else:
        print(f"{x} is gelijk aan {y}")

vergelijker(4, 3)  # 4 is groter dan 3
vergelijker(2, 9)  # 2 is kleiner dan 9
vergelijker(6, 6)  # 6 is gelijk aan 6
