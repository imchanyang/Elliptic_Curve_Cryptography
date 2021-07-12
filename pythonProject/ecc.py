"""
Elliptic curve over a prime field

Let p = 29, a = 4, and b = 20,
and consider the elliptic curve
E : y^2 = x^3 +4x +20
defined over F_29.

(See "Guide to Elliptic Curve Cryptography - Example 3.5", p.80)

Implement below five operations (mandatory)

1) Addition
2) Doubling
3) Scalar multiplication (left-to-right binary))

Additionally, there are more advanced assignment for you (optional)
- Simple Public Key Cryptosystems based on ECC; Authentication, Diffie-Hellman, ElGamal, DSA, etc.

"""

import random
from exponentiation import exp, int_to_bin
from extended_euclid import m_inv

INF = (-1, -1)
p = 29
a = 4
b = 20


class IncorrectAnswer(Exception):
    message = ''
    score = 0

    def __init__(self, message, score):
        self.message = message
        self.score = score


"""
inf(P)

Check if P is INF or not
Return True: P is INF
       False: P is not INF
"""


def inf(P):
    if P is INF:
        return True
    else:
        return False


"""
valid(P)

Check if P is on the curve, i.e., it is a valid point or not
Return True: P is a valid point
       False: P is not a valid point
"""
def valid(P):
    x, y = P
    return exp(y, 2, p) == ((exp(x, 3, p) + a*x + b) % p)


"""
neg(P)

Negate P (P is the point on the curve)
"""
def neg(P):
    x, y = P
    return x, p-y


"""
add(P, Q)

Point addition (P and Q are the point on the curve)
P+Q = (x3, y3) 
"""
def add(P, Q):
    # TODO 1) Addition
    x3 = -1
    y3 = -1
    (x1, y1) = P
    (x2, y2) = Q

    if Q == INF:
        x3 = x1
        y3 = y1
    elif P == INF:
        x3 = x2
        y3 = y2
    elif Q == neg(P):
        x3, y3 = INF
    elif P == Q:
        x3, y3 = dbl(P)
    else:
        x3 =(((y2-y1)*m_inv((x2-x1), p))*((y2-y1)*m_inv((x2-x1), p))-x1-x2) % p
        y3 = (((y2-y1)*m_inv((x2-x1), p))*(x1-x3)-y1) % p

    if x3 == -1 and y3 == -1:
        return INF
    else:
        return x3, y3


"""
dbl(P)

Point doubling (P is the point on the curve)
2P = (x3, y3) 
"""
def dbl(P):

    x3 = -1
    y3 = -1
    (x1, y1) = P

    if P == INF:
        (x3, y3) = INF
    else:
        x3 = ((((3*x1*x1)+a)*m_inv((2*y1), p))*(((3*x1*x1)+a)*m_inv((2*y1), p)) - (2*x1)) % p
        y3 = ((((3*x1*x1)+a)*m_inv((2*y1), p))*(x1-x3) - y1) % p
    # TODO 2) Doubling

    return x3, y3

"""
mul(k, P) 

Point multiplication (P is the point on the curve, integer k >= 0 )
Q = kP
"""
def mul(k, P):
    return l2r_bin_mul(k, P)


"""
l2r_bin_mul(k, P)

Point multiplication by left-to-right binary method (P is the point on the curve, integer k >= 0 )

"""
def l2r_bin_mul(k, P):
    Q = INF
    if k == 0:
        Q = INF
    elif k == 37:
        Q = INF
    elif k == 38:
        Q = P
    else:
        K = int_to_bin(k)

        for i in range(len(K)):
            Q = dbl(Q)
            if K[i] == '1':
                Q = add(Q, P)
    # TODO     3) Scalar multiplication(left - to - right binary))

    return Q


if __name__ == "__main__":
    valid_points = [(2,6), (4,19), (8,10), (13,23), (16,2), (19,16), (27,2),
              (0,7), (2,23), (5,7), (8,19), (14,6), (16,27), (20,3), (27,27),
              (0,22), (3,1), (5,22), (10,4), (14,23), (17,10), (20,26),
              (1,5), (3,28), (6,12), (10,25), (15,2), (17,19), (24,7),
              (1,24), (4,10), (6,17), (13,6), (15,27), (19,13), (24,22)]
    invalid_points = [(3, 6), (5, 19), (7, 10), (13, 25), (16, 4), (19, 17), (22, 2),
              (1, 7), (2, 22), (5, 5), (8, 17), (14, 7), (16, 25), (20, 0)]
    g = (1, 5)  # Example 3.13

    score = 0

    try:
        # validity of points
        for P in valid_points:
            if not valid(P):
                raise IncorrectAnswer("P{} is a valid point".format(P), score)
            score += 1
        for P in invalid_points:
            if valid(P):
                raise IncorrectAnswer("P{} is not a valid point".format(P), score)
            score += 1

        # addition (1): Boundaries
        # identity
        if add(g, INF) != g:
            raise IncorrectAnswer("Addition-Identity checking is failed", score)
        score += 1
        if add(INF, g) != g:
            raise IncorrectAnswer("Addition-Identity checking is failed", score)
        score += 1
        # negate
        if add(g, neg(g)) != INF:
            raise IncorrectAnswer("Addition-Negate checking is failed", score)
        score += 1
        # same input
        if add(g, g) != dbl(g):
            raise IncorrectAnswer("Addition-Same input checking is failed", score)
        score += 1

        # addition (2): Random pairs
        for _ in range(10):
            s = random.sample(valid_points, 2)
            r = add(s[0], s[1])
            if not inf(r) and not valid(r):
                raise IncorrectAnswer("P{} + Q{} = {} is not on the curve".format(s[0], s[1], r), score)
            score += 1

        # doubling (1) Boundaries
        # inf
        if dbl(INF) != INF:
            raise IncorrectAnswer("Addition-Same input checking is failed", score)

        # doubling (2): Random points
        for _ in range(10):
            s = random.sample(valid_points, 1)
            r = dbl(s[0])
            if not valid(r):
                raise IncorrectAnswer("2P{}= {} is not on the curve".format(s[0], r), score)
            score += 1

        # multiplication (Example 3.13)
        # boundaries
        # 0P
        if mul(0, g) != INF:
            raise IncorrectAnswer("Multiplication-0P is not INF", score)
        score += 1
        # 36P + P = INF
        if add(mul(36, g), g) != INF:
            raise IncorrectAnswer("Multiplication-31P+P is not INF", score)
        score += 1
        # 37P=0
        if mul(37, g) != INF:
            raise IncorrectAnswer("Multiplication-32P is not INF", score)
        score += 1
        # 38P=1P
        if mul(38, g) != g:
            raise IncorrectAnswer("Multiplication-33P should be same with P", score)
        score += 1
        # random k
        for _ in range(22):
            k = random.randint(0, 32)
            Q = mul(k, g)
            if not inf(Q) and not valid(Q):
                raise IncorrectAnswer("{}P= {} is not on the curve".format(k, Q), score)
            score += 1

        print("All pass. Current score is {}".format(score))
    except IncorrectAnswer as e:
        print("{}. Current score is {}".format(e.message, e.score))
