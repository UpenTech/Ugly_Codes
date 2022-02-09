from glob import glob


prime_list = [2,3,5,7,11,13,17,19,23]
detective = 1

def calcSum(start, end):
    global detective
    for num in range(start,end):
        for prime in prime_list:
            if num % prime == 0:
                detective = 0
                break

        if detective == 1:
            prime_list.append(num)

        detective = 1






