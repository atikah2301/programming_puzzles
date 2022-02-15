## Maximum number of distinct prime factors for numbers [1,n]

# "Leonardo's Prime Factors" from HackerRank > Mathematics > Fundamentals

def find_next_prime(n):
    # find the smallest prime bigger than n
    if n % 2 == 0:
        k = n + 1
    else:
        k = n + 2
    
    while True:
        is_prime = True
        for i in range(2, int(k**(1/2))+1):
            if k % i == 0:
                #print(f"{i} DOES divide {k}")
                is_prime = False
                break
            #print(f"{i} does not divide {k}")
        if is_prime == True:
            return k
        else:
            k += 2
        
#print(find_next_prime(11))

def prime_count(n):
    primes = [2]
    prod = 2
    while True:
        if n < prod:
            return len(primes) - 1
        
        next_prime = find_next_prime(primes[-1])
        primes.append(next_prime)
        prod *= next_prime
        
#print(prime_count(5000))
        
