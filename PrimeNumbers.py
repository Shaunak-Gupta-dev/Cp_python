import math
# check if a number is prime or not,    TC -> O(root(n)) SC -> O(1) 
def is_prime(n):
    if n == 1:
        return False
    i = 2
    while(i*i<=n):
        if n % i == 0:
            return False
        i += 1
    return True

print(is_prime(25))
print(is_prime(13))



# print all the prime factors of a number with their count

# Optimized    TC -> O(nlogn)
def get_prime_factors(n):
    prime_factors = []
    for i in range(2, n + 1):
        if n % i == 0:
            cnt = 0
            while n % i == 0:
                n = n // i
                cnt += 1
            prime_factors.append([i, cnt])
    return prime_factors

print(get_prime_factors(84))

#best          TC -> O((n^1/2)logn)
def get_prime_factors(n):
    prime_factors = []
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            cnt = 0
            while n % i == 0:
                n = n // i
                cnt += 1
            prime_factors.append([i, cnt])
    if n > 1:
        prime_factors.append([n, 1])
    return prime_factors

print(get_prime_factors(84))


# Generate prime numbers in a range
# SieveOfEratosthenes TC -> O(nloglogn)
def SieveOfEratosthenes(num):
    prime = [True for i in range(num+1)]
    p = 2
    while (p <= num):
        if (prime[p] == True):
            for i in range(p * p, num+1, p):
                prime[i] = False
        p += 1
    for i in range(2, num+1):
        if prime[i]:
            print(i)

SieveOfEratosthenes(20)

# optimized seive