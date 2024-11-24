numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []    #простые числа
not_primes = []

for elem in numbers:
    if elem < 2:
        continue
    is_prime = True
    for div in range(2,elem):
        if elem % div == 0:
            is_prime = False
            break
        else:
            continue
    if is_prime:
        primes.append(elem)
    else:
        not_primes.append(elem)


print ("Прост. числа: ", primes)
print ("Не прост. числа: ", not_primes)