def filter_prime(numbers):
    primes = []
    for num in numbers:
        if num > 1:
            is_prime = True
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    is_prime = False
                    break
            if is_prime:
                primes.append(num)
    return primes

input_numbers = input( "number: ")
numbers = input_numbers.split() 
numbers = [int(num) for num in numbers]
prime_numbers = filter_prime(numbers)
print("prime numbers: ", prime_numbers)