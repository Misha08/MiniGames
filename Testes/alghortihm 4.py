from math import sqrt
from random import randint

count = 31
step = int(sqrt(count))

arr = [list() for _ in range(step)]
find_count = set(map(str, [4, 15, 19, 25, 1]))
generate_count = set()
counter = 0
while counter < len(find_count):
    num = str(randint(1, count))
    if (0 < int(num) <= count) and (num not in generate_count):
        generate_count.add(num)
        counter += 1

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

ready_arr = list()
print(generate_count, find_count)
ready_set = generate_count.intersection(find_count)
copied_arr = list()
for i in arr:
    copied_arr.append([j.replace(" ", "") for j in i])

for k in ready_set:
    for i in range(len(copied_arr)):
        for j in range(len(copied_arr[i])):
            if str(k) == copied_arr[i][j]:
                copied_arr[i][j] = "x" * len(copied_arr[i][j])
                print("Yes")

for i in range(len(copied_arr)):
    for j in range(len(copied_arr[i])):
        copied_arr[i][j] = (len(str(count)) - len(str(copied_arr[i][j]))) * " " + str(copied_arr[i][j])

