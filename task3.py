import sys

sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')

while True:
    try:
        x1, y1, r1, x2, y2, r2 = input().split()

        x1 = int(x1)
        y1 = int(y1)
        r1 = int(r1)
        x2 = int(x2)
        y2 = int(y2)
        r2 = int(r2)

        dx = x1 - x2
        dy = y1 - y2
        d2 = dx * dx + dy * dy
        r_sum = r1 + r2
        r_diff = abs(r1 - r2)
        if d2 <= r_sum * r_sum and d2 >= r_diff * r_diff:
            print("YES")
        else:
            print("NO")
    except EOFError:
        break