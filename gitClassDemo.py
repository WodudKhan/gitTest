# Python program is displayed all the prime numbers within an interval

lower = 900
upper = 1000

print("Prime numbers between"), lower, "and", upper, "are:"

for num in range(lower, upper + 1):
    # All prime numbers are greater than 1
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            print(num)

    print("This is a git test")
    print("This is a git test2")
    print("This is a git test3")