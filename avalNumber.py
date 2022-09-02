def is_prime(number):
 if number < 2:
    return False

 if number == 2:
    return True

 if number % 2 == 0:
    return False

 for i in range(3, int(number**0.5), 2):
    if number % i == 0:
        return False
 
 return True

def calculate_prime_divisors(number):
 primes = []

 for i in range(2, number+1):
    if ((is_prime(i)) and (number % i == 0)):
        primes.append(i)
 
 return primes

numbers = {}
for i in range(10):
 n = int(input())
 numbers[n] = len(calculate_prime_divisors(n))

# find maximum number of prime divisors
max_value = max(numbers.values())
# find numbers with max_value number of prime divisors
max_keys = [k for k, v in numbers.items() if v == max_value]

print( sorted(max_keys)[-1], max_value)