import random
from ecc import mul, valid

# 파이썬 코딩에 익숙하지 않아서 ecc.py에 있는 점들 복사해옴
valid_points = [(2, 6), (4, 19), (8, 10), (13, 23), (16, 2), (19, 16), (27, 2),
                (0, 7), (2, 23), (5, 7), (8, 19), (14, 6), (16, 27), (20, 3), (27, 27),
                (0, 22), (3, 1), (5, 22), (10, 4), (14, 23), (17, 10), (20, 26),
                (1, 5), (3, 28), (6, 12), (10, 25), (15, 2), (17, 19), (24, 7),
                (1, 24), (4, 10), (6, 17), (13, 6), (15, 27), (19, 13), (24, 22)]


# 키 생성
def private_key_gnt():
    k = random.randint(0, 32)
    return k


# 공개키 생성
def public_key_gnt(k, s):
    q = mul(k, s)
    return q


# 공개키를 가지고 최종 key 생성
def make_key(k, q):
    K = mul(k, q)
    return K


class Person:
    # 이름
    __name = ''
    # private key
    __X = private_key_gnt()
    # 상대방과 공유하는 점
    __S = -1, -1
    # 자신의 public key
    __Q_self = -1, -1
    # 상대방의 public key
    __Q_another = -1, -1
    # 상대방의 public key와 자신의 private key로 만든 KEY
    __K = -1, -1

    # 이름과 공유하는 점 초기화 / 자신의 public key 생성
    def __init__(self, name, S):
        self.__name = name
        self.__S = S
        self.__Q_self = public_key_gnt(self.__X, S)

    # 자신의 public key 공유
    def give_key(self):
        return self.__Q_self

    # 상대방의 public key 받기
    def recieve_key(self, Q):
        self.__Q_another = Q

    # 만든 KEY를 공유
    def make(self):
        self.__K = make_key(self.__X, self.__Q_another)
        return self.__K


# ECDH(Elliptic Curve Diffie-Hellman) main 함수
if __name__ == "__main__":

    # 공유할 점P 생성
    S1 = random.sample(valid_points, 1)
    P = S1[0]

    # 점P가 정의한 타원 곡선 상에 있는지 확인
    if not valid(P):
        print("타원 곡선에 존재하지 않는 점입니다.")
    else:
        print("타원 곡선에 존재하는 점입니다.")
        alice = Person("Alice", P)
        bob = Person("Bob", P)

        # Bob이 public key를 Alice에게 준다
        alice.recieve_key(bob.give_key())

        # Alice이 public key를 Bob에게 준다
        bob.recieve_key(alice.give_key())

        # 각자 받은 상대방의 public key로 KEY를 만든다
        K1 = alice.make()
        K2 = bob.make()

        # 상대방의 키와 나의 키가 잘 공유 했다면 Key Exchange 성공
        if K1 == K2:
            print("ECDH(Elliptic Curve Diffie-Hellman)을 이용한 Key Exchange 성공!")
        else:
            print("ECDH(Elliptic Curve Diffie-Hellman)을 이용한 Key Exchange 실패!")
