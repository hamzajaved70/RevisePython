# My understanding of Sieve of Eratosthenes

# 1. Add all numbers below n to a list and mark them as True
# 2. Set p = 2 and loop through p until p squared is less then or equal to n
# 3.  Mark all multiples of p as False
# 4. Remaining True items in list are prime.

# input max number for primes
n = int(input())
# create list of numbers and mark them all as prime initially
numList = []
for i in range(n + 1):
    numList.append(True)
# p is the initial multiple to start with
p = 2
while(p * p <= n):
    if numList[p]:
        # mark all multiples of p as False
        for i in range(p * p, n + 1, p):
            numList[i] = False
    p += 1

for i in range(2, n):
    if numList[i]:
        print(i, end=' ')
