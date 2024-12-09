def first_n_primes(n):
    is_prime = lambda x: all([x % i != 0 for i in range(2, x // 2 + 1)])
    primes = []
    counter = 2
    while len(primes) < n:
        if is_prime(counter):
            primes.append(counter)
        counter += 1
    return primes



print(first_n_primes(5))

