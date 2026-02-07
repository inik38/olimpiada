a = int(input())

if a>0:
    while a % 2 == 0:
        a= a//2
    if a == 1:
        print("YES")

    else:
        print("NO")

else:
    print("NO")