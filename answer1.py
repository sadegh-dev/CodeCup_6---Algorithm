index = int(input())

txt = "codecup6"
arr = list(txt)

if index < 9 :
    index -= 1
    result = arr[index]
else :
    a = divmod(index,8)
    index = a[1]
    index -= 1
    result = arr[index]


print(result)

