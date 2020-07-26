arr = [10, 22, 9, 33, 21, 50, 41, 60, 80]
lisList = [1, 1, 1, 1, 1, 1, 1, 1, 1]

for i in range(1, len(arr)):
    for j in range(i-1, -1, -1):
        if arr[j] > arr[i]:
            continue

        elif lisList[j] + 1 > lisList[i]:
            lisList[i] = lisList[j] + 1

print(max(lisList))
