m1, m2, m3 = input().split()

m1 = int(m1)
m2 = int(m2)
m3 = int(m3)
                 
if 93<m1<728 and 93<m2<728 and 93<m3<728:
    if m1>=m2>=m3 or m1>=m3>=m2:
        print(m1)
    elif  m2>=m1>=m3 or m2>=m3>=m1:
        print(m2)
    elif m3>=m2>=m1 or m3>=m1>=m2:
        print(m3)
                 
else:
    print("Error")