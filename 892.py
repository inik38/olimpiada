import sys

sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')

while True:
    try:
        a = int(input())

        if 0<a<13:
            if a==1 or a==2 or a==12:
                print("Winter")

            elif a==3 or a==4 or a==5:
                print("Spring")

            elif a==6 or a==7 or a==8:
                print("Summer")

            elif a==9 or a==10 or a==11:
                print("Autumn")

        else:
            print("Error")
    except EOFError:
        break