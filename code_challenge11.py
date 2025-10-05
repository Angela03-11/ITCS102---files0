print(" \t\t " "*", end=" ")
for e in range(1, 11, 1):
    for g in range(10, e, -1):
        print(" ", end=" ")
    for o in range(1, e, 1):
        print("*", end=" ")
    for b in range(1, e, 1):
        print("*", end=" ")
    print()