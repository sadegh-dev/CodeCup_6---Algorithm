t = int(input())

arr = []

for x in range(t):
    d = input()
    b = d.split()
    arr.append(b)
    y = int(x)
    if x != y :
        print("-1")
    else:
        qq = (n*x)
        tt = s+(a*(n-1))
        if qq != tt :
            print("-1")
        else:
            result = x-a
            if result == 0 :
                print("-1")
            else:
                print(int(result))
