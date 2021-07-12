# Elliptic_Curve_Cryptography

공개키암호의 종류로

줄여서 ECC라고 하기도 합니다. 한국어로는 타원 곡선 암호입니다.

## ECC의 기본 연산
1. Addtion
2. Doubling
3. Scalar Multiplication(left-to-right binary)

를 Python으로 구현했습니다.

## ECC를 이용한 암호 시스템
ECC의 기본 연산을 이용한 암호 시스템들입니다.

1. Key Exchange : ECDH(Elliptic Curve Cryptography) : ECDH.py
2. Encryption / Decryption : EC ELGamal
3. Digital Signature : ECDSA
