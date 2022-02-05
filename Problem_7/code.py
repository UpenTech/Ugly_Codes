from pickle import TRUE

store = int(input("Which Prime?\n>"))

list_prime = [2,3,5,7,11,13,17,19]
num = 22
odd = False

while len(list_prime) < store:
    for i in list_prime:
        if num % i == 0:
            odd = TRUE
            break
    if not odd:
        list_prime.append(num)
    odd = False
    num += 1

print(list_prime[store - 1])
