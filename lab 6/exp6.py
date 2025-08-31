i = 1
while i <= 100:
    if i % 2 != 0:
        print(i, end=" ")
    i += 1
n = int(input("Enter a number: "))
total = 0
i = 1

while i <= n:
    total += i
    i += 1

print("Sum =", total)
def count_digits(num):
    count = 0
    if num == 0:
        return 1
    while num != 0:
        num //= 10
        count += 1
    return count

number = int(input("Enter a number: "))
print("Number of digits:", count_digits(number))
num = int(input("Enter a number: "))
last_digit = num % 10

first_digit = num
while first_digit >= 10:
    first_digit //= 10

print("First digit:", first_digit)
print("Last digit:", last_digit)
def swap_first_last(num):
    num_str = str(num)
    if len(num_str) == 1:
        return num  # No swap needed
    swapped = num_str[-1] + num_str[1:-1] + num_str[0]
    return int(swapped)

# Example usage
number = int(input("Enter a number: "))
print("After swapping first and last digits:", swap_first_last(number))
num = int(input("Enter a number: "))
product = 1

while num > 0:
    digit = num % 10
    product *= digit
    num //= 10

print("Product of digits:", product)
num = int(input("Enter a number: "))
reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num //= 10

print("Reversed number:", reverse)
