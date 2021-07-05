row=int(input())
for i in range(1, row+1):
    for j in range(1, i+1):
        print(j, end="  ")
    print()
for k in range(1, row+1):
    space = row - k
    print(space * '-', end="  ")