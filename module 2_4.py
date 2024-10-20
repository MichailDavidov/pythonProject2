numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
prime = []
not_prime = []
is_prime = True
for i in range (len(numbers)):
    for k in range (2, numbers[i]+1):
        if numbers[i] % k ==0 and k != numbers[i]:
            not_prime.append (numbers[i])
            break
        if numbers[i] % k ==0 and k == numbers[i]:
            prime.append(numbers[i])
print (prime)
print (not_prime)