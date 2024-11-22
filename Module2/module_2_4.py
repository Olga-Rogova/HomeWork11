numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for i in numbers:
    is_primes = True
    for delitel in range(2, i):
        if i % delitel == 0:
            is_primes = False
            not_primes.append(i)
            break
    if is_primes == True and i != 1:
        primes.append(i)
print(primes)
print(not_primes)