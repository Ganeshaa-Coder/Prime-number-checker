def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    # Check for even numbers greater than 2
    elif n > 2 and n % 2 == 0:
        return False
    # Check only odd divisors starting from 3
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


number = int(input("Enter a number: "))
if is_prime(number):
    print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number.")
