height = 5
for i in range(height):
    print(" " * (height - i - 1) + "*" * (2 * i + 1))

for _ in range(2):
    print(" " * (height - 1) + "*")