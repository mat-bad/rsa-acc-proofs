import secrets
from typing import Tuple

MODULUS_SIZE = 2048
MILLER_RABIN_ROUNDS = 10

def generate_rsa_mudulus() -> Tuple[int, int]:

    while True:
        p = _generate_prime(MODULUS_SIZE//2)
        q = _generate_prime(MODULUS_SIZE//2)

        if p == q:
            continue

        n = p * q
        if n.bit_length() == MODULUS_SIZE:
            return p, q
        
def _generate_prime(n: int) -> int:
    """Returns a random `n` bit prime number."""
    while True:
        candidate = _random_odd_integer(n)
        if _is_prime(candidate):
            return candidate
        
def _random_odd_integer(n: int) -> int:
    """Returns a random `n` bit odd number."""
    res = (1<<(n-1)) + secrets.randbits(n-1)
    res |= 1
    return res

def _is_prime(x: int, rounds = MILLER_RABIN_ROUNDS) -> bool:
    """Returns `True` iff x is prime. Uses Miller-Rabin so small chance of false positives."""
    if x==1:
        return False
    if x==2 or x==3:
        return True
    
    for _ in range(rounds):    
        a = secrets.randbelow(x-3)+2
        p = x-1
        z = pow(a, p, x)
        if z != 1:
            return False
        while not p&1:
            p >>= 1
            z = pow(a, p, x)
            if z == x-1:
                break
            if z != 1:
                return False
    return True



# def pow(x: int, p: int, m: int) -> int:
#     """Returns `x` to the power of `p` mod `m`."""
#     res = 1
#     while p:
#         res = res * x % m if p&1 else res
#         p >>= 1
#         x = x * x % m

#     return res


if __name__ == '__main__':
    print(_is_prime(5))
    num = 0
    for i in range(2, 100):
        num += _is_prime(i)
    print(num)

    print(_generate_prime(10))
    a, b = generate_rsa_mudulus()
    print(_is_prime(a))
    print(_is_prime(b))
    print(_is_prime(a*b))