# 공학용 계산기 함수

import math
from typing import Union, Literal
from .basic import Calculator
from . utils import Utils




class EngineeringCalculator(Calculator):
    def __init__(self):
        self.utils = Utils()

    def square_root(self, x: float, **kwargs: dict) -> Union[float, str]:

        # 제곱근 계산
        result: float = math.sqrt(x) 

        # 결과 포맷팅
        result = self.utils.round_result(result, **kwargs)

        return result
    
    def power(self, x: float, y: float, **kwargs: dict) -> Union[float, str]:

        # 거듭제곱 계산
        result: float = math.pow(x, y)   # x**y
        
        # 결과 포맷팅
        result = self.utils.round_result(result, **kwargs)

        return result
    
    def log(self, x: float, **kwargs: dict) -> Union[float, str]:

        # base = 10인 로그 계산
        result: float = math.log10(x)   # base = 10인 로그

        # 결과 포맷팅
        result = self.utils.round_result(result, **kwargs)

        return result
    
    def ln(self, x: float, **kwargs: dict) -> Union[float, str]:
    
        # 자연로그 계산
        result: float = math.log(x)   # 자연로그

        # 결과 포맷팅
        result = self.utils.round_result(result, **kwargs)

        return result

    def sin(self, x: float, **kwargs: dict) -> Union[float, str]:

        # 각도 변환
        x = self.utils.angle_unit(x, **kwargs)
        
        # sin 계산
        result = math.sin(x)

        # 결과 포맷팅
        result = self.utils.round_result(result, **kwargs)

        return result
    
    def cos(self, x: float, **kwargs: dict) -> Union[float, str]:

        # 각도 변환
        x = self.utils.angle_unit(x, **kwargs)
        
        # cos 계산
        result = math.cos(x)

        # 결과 포맷팅
        result = self.utils.round_result(result, **kwargs)

        return result
    
    def tan(self, x: float, **kwargs: dict) -> Union[float, str]: 
        
        # 각도 변환
        x = self.utils.angle_unit(x, **kwargs)
        
        # tan 계산
        result = math.tan(x)

        # 결과 포맷팅
        result = self.utils.round_result(result, **kwargs)

        return result

# EngineeringCalculator 인스턴스 생성
eng_calc = EngineeringCalculator()

__all__ = ['EnginneringCalculator']

# 모듈 실행될 때 __name__ 의 값은 __main__ 이 된다.
# 모듈이 다른 파일에서 import될 때 __name__ 값은
# 해당모듈의 이름이 된다.

if __name__ == '__main__' :

    # 간단한 데모 코드 작성
    calc = Calculator()
    eng_calc = EngineeringCalculator()

    print("Basic Calculator Demo:")
    print(calc.add(1,2,3))
    print(calc.multiply(2,4,6))

    print("\nEngineering Calculator Demo:")
    print(eng_calc.square_root(16))
    print(eng_calc.sin(30,angle_unit = 'degree'))

# 데모 코드 작성 이유
# 각 클래스의 주요 기능을 보여주기 위해

