## 계산기 패키지

간단한 수학 연산을 수행하는 일반 계산기와
공학용 계산기 까지 추가된 Python 계산기 패키지입니다.

## 기능

이 패키지는 다음과 같은 기본적인 수학 연산을 제공합니다:

- 덧셈 , 뺄셈, 곱셈, 나눗셈
- 제곱근 , 거듭제곱, base = 10인 로그, 자연로그, 삼각함수

## 설치 방법

pip를 사용하여 패키지를 설치할 수 있습니다:

pip install calculator_package

## 사용방법

```python
from calculator_package.basic import Calculator
from calculator_package.engineering import EngineeringCalculator

calc = Calculator()
eng_calc = EngineeringCalculator()


print(calc.add(1, 2, 3, precision=2))  # 출력: 6.00
print(calc.subtract(10, 2, 3, return_float=True))  # 출력: 5.0
print(calc.multiply(2, 3, 4))  # 출력: 24
print(calc.divide(100, 2, precision=3))  # 출력: 50.000
print(calc.divide(100, 0, precision=3))  # 출력  "오류: 0으로 나눌 수 없습니다."

print(eng_calc.square_root(16, precision=3))  # 출력: 4.000
print(eng_calc.log(100, precision=4))  # 출력: 2.0000
print(eng_calc.sin(30, angle_unit='degree', precision=4))  # 출력: 0.5000

```

## 주의 사항
나눗셈에서 0으로 나눌시 ZeroDivisionError 가 발생하며
"오류: 0으로 나눌 수 없습니다." 로 출력이 됩니다.
