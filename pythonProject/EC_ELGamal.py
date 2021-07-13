import random

from ecc import mul, valid, add, neg


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
    # S
    __S = -1, -1
    # C
    __C = -1, -1

    # 이름과 공유 점 초기화/ public_key 생성
    def __init__(self, name, P):
        self.__name = name
        self.__P = P
        self.__A = public_key_gnt(self.__a, self.__P)

    # pulick_key 반환
    def get_public_key(self):
        return self.__A

    # S 받기
    def set_S(self, K):
        self.__S = public_key_gnt(self.__a, K)

    # C 받기
    def set_C(self, C):
        self.__C = C

    # M(메세지) 생성 및 반환
    def get_M(self):
        M_ = add(self.__C, neg(self.__S))
        return M_


# EC ELGamal(Elliptic Curve ELGamal) main 함수
if __name__ == "__main__":
    S = random.sample(valid_points, 1)
    P = S[0]

    # 점P가 타원 곡선에 있는 지 확인(당연하지만)
    if not valid(P):
        print("이 점은 타원 곡선에 없는 점입니다.")

    # 메세지를 타원 곡선 위에 있게 하는 것을 모르겠어서 일단 valid_points에서 뽑았습니다.
    m = random.sample(valid_points, 1)
    M = m[0]

    # M(메세지)이 타원 곡선에 있는 지 확인(당연하지만)
    if not valid(M):
        print("메세지에 해당하는 점은 타원 곡선에 없는 점입니다.")

    # Alice, public_key 생성
    alice = Person("Alice", P)
    A = alice.get_public_key()

    # Bob's random value k, K, C 생성
    k = private_key_gnt()
    K = public_key_gnt(k, P)
    C = add(mul(k, A), M)

    # Alice가 Bob의 K, C 받음
    alice.set_S(K)
    alice.set_C(C)

    # Alice가 계산한 M_(메세지)
    M_ = alice.get_M()

    # Alice의 M_과 Bob의 M이 같으면 성공
    if M_ == M:
        print("EC_ELGamal Perfect!")
    else:
        print("EC_ELGamal failure..")












