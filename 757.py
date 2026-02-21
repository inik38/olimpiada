import sys

sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')

while True:
    try:
        c, h, o = input().split()

        c = int(c)
        h = int(h)
        o = int(o)
        
        c = c//2
        h = h//6

        if c<=h<=o or c<=o<=h:
            print(c)
        elif h<=c<=o or h<=o<=c:
            print(h)
        elif o<=c<=h or o<=h<=c:
            print(o)
    except EOFError:
        break