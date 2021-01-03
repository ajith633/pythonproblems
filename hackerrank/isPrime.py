import math


def isprime(p):
    if (p < 4):
        return p > 1
    if p % 2 == 0 or p % 3 == 0:
        return False
    for i in range(3, int(math.sqrt(p))+1,2):
        if p % i == 0:
            print(i)
            return False
    return True

#3
#1000000007
#100000003
#1000003

T = int(input())
items = []
for _ in range(T):
    items.append(int(input()))

for p in items:
    if (isprime(p)):
        print("{} is Prime".format(p))
    else:
        print("{} is Not Prime".format(p))



