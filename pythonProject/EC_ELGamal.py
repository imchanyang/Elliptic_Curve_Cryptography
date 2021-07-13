import random

from ecc import mul, valid

# 파이썬 코딩에 익숙하지 않아서 ecc.py에 있는 점들 복사해옴
valid_points = [(2, 6), (4, 19), (8, 10), (13, 23), (16, 2), (19, 16), (27, 2),
                (0, 7), (2, 23), (5, 7), (8, 19), (14, 6), (16, 27), (20, 3), (27, 27),
                (0, 22), (3, 1), (5, 22), (10, 4), (14, 23), (17, 10), (20, 26),
                (1, 5), (3, 28), (6, 12), (10, 25), (15, 2), (17, 19), (24, 7),
                (1, 24), (4, 10), (6, 17), (13, 6), (15, 27), (19, 13), (24, 22)]

n = 37
# 키 생성
def private_key_gnt():
    k = random.randint(0, 32)
    return k


# 공개키 생성
def public_key_gnt(k, s):
    q = mul(k, s)
    return q

class Person:
    # 이름
    __name = ""
    # private key
    __a = private_key_gnt()
    # public key
    __A = -1, -1
    # base point
    __P = -1, -1

    def __init__(self, name, P):
        self.__name = name
        self.__P = P
        self.__A = public_key_gnt(self.__a, self.__P)

    def get_public_key(self):
        return self.__A


# EC ELGamal(Elliptic Curve ELGamal) main 함수
if __name__ == "__main__":
    S = random.sample(valid_points, 1)
    P = S[0]

    if not valid(P):
        print("이 점은 타원 곡선에 없는 점입니다.")

    M = input("메세지를 입력하세요 : ")

    alice = Person("Alice", P)
    A = alice.get_public_key()

    k = private_key_gnt()
    K = public_key_gnt(k, P)


