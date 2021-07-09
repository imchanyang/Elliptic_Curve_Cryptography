"""
int_to_bin

convert an integer to a binary representation
(the most significant bit becomes the 0-th bit)
"""


def int_to_bin(num):
    return list(bin(num))[2:]


"""
Modular exponentiation

a ^ b mod n
"""


def exp(a, b, n):
    c = 0
    f = 1
    bin_b = int_to_bin(b)
    k = len(bin_b)
    for i in range(k):
        c = 2 * c
        f = (f * f) % n
        if bin_b[i] == '1':
            c = c + 1
            f = (f * a) % n
    return f


if __name__ == "__main__":
    # print(int_to_bin(560))

    # print(exp(7, 560, 561))
    print(exp(7, 43214321443214412341234321, 65537))
    # print(exp(7, 0, 561))
    # print(exp(7, 1, 561))
