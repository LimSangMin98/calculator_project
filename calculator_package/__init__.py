# 버전정보
__version__ = "3.11.4"

# 필요한 모듈 호출
from calculator_package.basic import Calculator
from calculator_package.engineering import EngineeringCalculator

__all__ = ['Calculator', 'EngineeringCalculator']


# 패키지 레벨에서 사용할 상수 정의
PI = 3.14159265359
E = 2.71828182846

# 패키지 초기화 함수

# 패키지가 import 될 때 실행되는 코드


# 사용 예시 출력
print("사용 예시:")
print("from calculator_package.basic import Calculator")
print("from calculator_package.engineering import EngineeringCalculator")
print("calc = Calculator()")
print("eng_calc = EngineeringCalculator()")
print("print(calc.add(1, 2, 3, precision=2))")
print("print(eng_calc.sin(30, angle_unit='degree', precision=4))")
