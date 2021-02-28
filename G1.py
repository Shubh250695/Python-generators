# range(start, stop, step)

# printing sequence of numbers
for i in range(10):
    print(i, end =" ")
print()

# performing mathematical operation
# here sum of natural number 
sum = 0
for i in range(1, 11):
    sum = sum + i
print("Sum of first 10 natural number :", sum)

# sequence of numbers, but increment by some number instead of 1
x = range(3, 20, 2)
for n in x:
    print(n, end=" ")