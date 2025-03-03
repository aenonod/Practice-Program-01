# Create a program that print all the numbers starting from 0 to 100 except numbers ending in zero.

non_zero = []
for i in range (0, 101):
    if i % 10 != 0:
        non_zero.append(i)

print(non_zero)