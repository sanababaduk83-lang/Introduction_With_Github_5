#дз номер 6
result = []

def divider(a, b):
    if a < b:
        raise ValueError
    if b > 100:
        raise IndexError
    return a / b

data = {10: 2, 2: 5, "1234234772834": 4, 18: 0, (): 15, 8: 4}

for key in data:
    try:
        res = divider(key, data[key])
        result.append(res)
    except Exception as e:
        print(f"Виняток для пари ({key}:{data[key]}): {type(e).__name__} - {e}")

print(result)
           #kem kem? може key? a так все гуд
