# Create a program that ask user to input 10 numbers. Print how many are odd numbers.

odd = []
for i in range (10):
    num = int(input("Input a number: "))
    if num % 2 != 0:
        odd.append(num)

print(odd)