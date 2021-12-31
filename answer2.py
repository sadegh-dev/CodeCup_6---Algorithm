t = int(input())

arr = []

for x in range(t):
    d = input()
    b = d.split()
    arr.append(b)



for x in range(t):
    n = int(arr[x][0])
    s = int(arr[x][1])
    a = int(arr[x][2])

    x = (s-(a*(1-n))) / n
    result = x-a
    tt = int(result)
    if result > 0 and tt == result :
        print(int(result))
    else :
        print("-1")

