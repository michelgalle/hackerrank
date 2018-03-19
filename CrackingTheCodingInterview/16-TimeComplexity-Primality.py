def is_prime(a):
    if a < 2: return False
    if a == 2 or a == 3: return True  # manually test 2 and 3
    if n & 1 == 0 or a % 3 == 0: return False  # exclude multiples of 2 and 3

    maxDivisor = a ** 0.5
    d, i = 5, 2
    while d <= maxDivisor:
        if a % d == 0: return False
        d += i
        i = 6 - i  # this modifies 2 into 4 and viceversa

    return True


p = int(input().strip())
for a0 in range(p):
    n = int(input().strip())
    print("Prime" if is_prime(n) else "Not prime")
