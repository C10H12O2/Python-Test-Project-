side = 4
i = 0
while i < side:
    j = 0
    while j < side:
        if i == 0 or i == side - 1 or j == 0 or j == side - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
        j += 1
    print()
    i += 1