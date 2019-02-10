import random

a = [random.randint(1, 100) for _ in range(15)]
b = [random.randint(1, 100) for _ in range(15)]

result = set(a).intersection(set(b))

print(a)
print(b)
print(result)
