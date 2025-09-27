nums = list(map(int, input().split()))

N = nums[0]
M = nums[1]
L = nums[2:]

L.sort(reverse=True)

total = 0
count = 0
for length in L:
    total += length
    count += 1
    if total >= N:
        print(count)
        break
else:
    print(0)
