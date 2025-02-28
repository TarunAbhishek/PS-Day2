#print 1-100 numbers
for i in range(1, 101):
    print(i)

#natural numbers
n = int(input("Enter a number: "))
sum_n = 0
for i in range(1, n + 1):
    sum_n += i
print("Sum of first", n, "natural numbers:", sum_n)

#even numbers in 1-50
num=2
while num <= 50:
    print(num)
    num += 2

#multiplication table
num = int(input("Enter a number: "))
print("Multiplication table for", num)
for i in range(1, 21):
    print(num, "x", i, "=", num * i)

#factorial
num = int(input("Enter a number: "))
factorial = 1
i = num
while i > 0:
    factorial *= i
    i -= 1  
print("Factorial of", num, "is", factorial)

#divisible by 3 and 5
for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0: 
        print(i)