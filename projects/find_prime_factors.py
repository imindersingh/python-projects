def get_prime_factors(number):
    factors = list()
    divisor = 2
    while divisor <= number:
        if number % divisor == 0:
            number = number / divisor
            factors.append(divisor)
        else:
            divisor +=1
    return factors

def main():
    number = input("Enter number to return all prime factors: ")
    factors = get_prime_factors(int(number))
    print(factors)

if __name__ == "__main__":
    main()
    