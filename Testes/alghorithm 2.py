from math import sqrt

count = 131
step = int(sqrt(count))
arr = [list() for _ in range(step)]
c1 = 0
c2 = step
for i in range(step):
    arr[i] = [j + 1 for j in range(c1, c2)]
    c1 += step
    c2 += step

rest = count - step ** 2

count_add = rest // step
if count_add == 0:
    arr.append([i for i in range(count - step + 2, count + 1)])
else:
    c1 = step ** 2 + 1
    c2 = c1 + step
    for i in range(count_add):
        arr.append([j for j in range(c1, c2)])

    arr.append([k for k in range(arr[-1][-1] + 1, count + 1)])

for i in range(len(arr)):
    for j in range(len(arr[i])):
        arr[i][j] = (len(str(count)) - len(str(arr[i][j]))) * " " + str(arr[i][j])

for i in arr:
    print(*i)
