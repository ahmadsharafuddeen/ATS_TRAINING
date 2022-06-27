def erat_prime(number):
    prime_nums = [True for i in range(number + 1)]
    
    p = 2
    while p * p <= number:
        if prime_nums[p] == True:
            # update all multiples of p
            for i in range(p * p, number + 1, p):
                prime_nums[i] = False
                
        p += 1
        
        all_primes = []
        # print all the prime numbers
        for p in range(2, number + 1):
            if prime_nums[p]:
                all_primes.append(p)
                
        return all_primes
    
print(erat_prime(999))