# 유틸리티 함수
# 정적 메서드로 구성되어 있어 인스턴스 생성X
import math
from typing import Union, Literal

class Utils :
    
    # round_result : 주어진 숫자를 지정된 소수점 자릿수로 반올림하는 기능

      #인자:
         # result: 반올림할 숫자
         # **kwargs: 키워드 인자로 precision과 return_float 옵션을 받습니다.

      #동작:
         # precision이 지정된 경우: 결과를 지정된 소수점 자릿수까지 반올림합니다.
         # return_float가 True인 경우: 결과를 float 타입으로 반환합니다.
         # 그 외의 경우: 기본적으로 정수로 반올림합니다.

      # 반환 값:
         # precision이 지정된 경우: 지정된 소수점 자릿수까지 반올림된 문자열
         # return_float가 True인 경우: 반올림된 float 값

         # 그 외의 경우: 정수로 반올림된 값 


    def round_result(self,result,**kwargs) : 
        precision: Union[int, None] = kwargs.get('precision', None)
        return_float: bool = kwargs.get('return_float', False)

        if return_float:
            return float(result)
        
        if precision is not None:
            return f'{result:.{precision}f}'
        
        return round(result)
    
    # convert_to_radians
    # 각도가 degree일 때 결과를 radian으로 변환

    def angle_unit(self, x, **kwargs) : 

        # angle_unit 매개변수 추가 및 radian을 기본값으로 지정
        angle_unit: Literal['radian', 'degree'] = kwargs.get('angle_unit', 'radian')

        if angle_unit == 'degree':
            x: float = math.radians(x)
        
        return x

__all__ = [Utils]


