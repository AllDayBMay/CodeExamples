#This is my solution to the "Multiples of 3 and 5" problem 1 on Project Euler,
#Problem description found here: https://projecteuler.net/problem=1

sum = 0
i = 0
while (i < 1000):
    if (i%3 == 0):
        sum = sum + i
        i = i + 1
    elif (i%5 == 0):
        sum = sum + i
        i = i + 1
    else:
        i = i + 1
print(sum)