first = 0
second = 1
n = int(input("Enter the number of terms: "))
for i in range(n):
    print(first)
    next_term = first + second
    first = second
    second = next_term