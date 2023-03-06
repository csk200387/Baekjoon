from math import gcd

def solution(numer1, denom1, numer2, denom2):
    up = (numer1 * denom2) + (numer2 * denom1)
    down = denom1 * denom2
    g = gcd(up, down)
    return [int(up/g), int(down/g)]