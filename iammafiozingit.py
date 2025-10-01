data = list(map(int, input().split()))

n = data[0]
weights = data[1:]

max_w = max(weights)
min_w = min(weights)
total = sum(weights)

print(max_w, min_w, total)
