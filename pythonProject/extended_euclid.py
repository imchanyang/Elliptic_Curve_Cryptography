"""
Extended Euclidean Algorithm (Iterative version) ( a >= b )

return (x, y, r) such that a * x + b * y = r = gcd(a, b)
loop invariant :
a * x_1 + b * y_1 = r_1
a * x_2 + b * y_2 = r_2

"""


def extended_euclid(a, b):

    if a == b:
        return 1, 0, a
    elif b == 0:
        return 1, 0, a
    else:
        x_1 = 1
        y_1 = 0
        r_1 = a

        x_2 = 0
        y_2 = 1
        r_2 = b

        while r_2 != 0:
            q = r_1 // r_2

            r_t = r_1 - q * r_2
            x_t = x_1 - q * x_2
            y_t = y_1 - q * y_2

            x_1, y_1, r_1 = x_2, y_2, r_2
            x_2, y_2, r_2 = x_t, y_t, r_t

        return x_1, y_1, r_1


"""
Multiplicative Inverse

x = a^-1 mod n 
a * x mod n = 1

"""


def m_inv(a, n):
    x, y, r = extended_euclid(n, a % n)
    if r != 1:
        print("No multiplicative inverse")
        return
    else:
        return y % n


if __name__ == "__main__":
    print(extended_euclid(710, 310))
    print(extended_euclid(8, 0))
    print(extended_euclid(300, 10))
    print(extended_euclid(2000000000000000000000000000000, 43217))
    print(extended_euclid(1759, 550))
    # print(extended_euclid(1160718174, 316258250))
    print()
    # print(m_inv(710, 310))
    print(m_inv(550, 1759))  # x = 550^-1 mod 1759
