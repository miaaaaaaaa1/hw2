#1

def product_of_numbers(numbers):
    product = 1
    for number in numbers:
        product *= number
    return product

numbers = [1, 2, 3, 4, 5]
result = product_of_numbers(numbers)
print(result)

#2

def minimum(numbers):
    
    minimum = numbers[0]
    for number in numbers:
        if number < minimum:
            minimum = number
    return minimum

numbers = [5, 3, 8, 1, 2, 7]
result = minimum(numbers)
print(result)

#3

def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

def count_primes(numbers):
    prime_count = 0
    for number in numbers:
        if is_prime(number):
            prime_count += 1
    return prime_count

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = count_primes(numbers)
print(result)

#4

def remove_element(numbers, num):
    length = len(numbers)
    numbers = [number for number in numbers if number != num]
    removed_count = length - len(numbers)
    return removed_count

numbers = [1, 2, 3, 4, 3, 5, 3, 6]
num = 3
result = remove_element(numbers, num)
print(result)
print(numbers)

#5

def lists(list1, list2):
    list = list1 + list2
    return list

list1 = [1, 2, 3]
list2 = [4, 5, 6]
result = lists(list1, list2)
print(result)

#6

def elements(numbers, exponent):
    l = [number ** exponent for number in numbers]
    return l

numbers = [1, 2, 3, 4, 5]
exponent = 2
result = elements(numbers, exponent)
print({result})