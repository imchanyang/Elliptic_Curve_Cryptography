# Elliptic_Curve_Cryptography

줄여서 ECC라고 하기도 합니다. 한국어로는 타원 곡선 암호입니다.

Python을 이용해서 구현했습니다.
## ECC의 기본 연산
1. Addtion
2. Doubling
3. Scalar Multiplication(left-to-right binary)
ECC의 기본연산을 Python으로 구현했습니다.

## ECC를 이용한 암호 시스템
ECC의 기본 연산을 이용한 암호 시스템들입니다.
각 시스템들 옆에는 해당 시스템을 구현한 파일이름입니다.
ex) ECDH.py 

1. Key Exchange : ECDH(Elliptic Curve Diffe-Hellman) : ECDH.py
2. Encryption / Decryption : EC(Elliptic Curve) ELGamal : EC_ELGamal.py
3. Digital Signature : ECDSA(Elliptic Curve Digital Signature Algorithm) : ECDSA.py
