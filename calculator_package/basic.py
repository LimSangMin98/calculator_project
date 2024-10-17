# 일반 계산기 함수

from . utils import Utils
class Calculator:

    def __init__(self):
        self.utils = Utils()

    # 덧셈
    def add(self, *args, **kwargs):
        result = args[0]  # 첫 번째 인자로 초기값 설정

        for num in args[1:]:
            result += num

         # 결과 포맷팅
        result = self.utils.round_result(result, **kwargs)
        
        return result
    
    # 뺄셈
    def subtract(self, *args, **kwargs):
        result = args[0]  # 첫 번째 인자로 초기값 설정

        for num in args[1:]:
            result -= num

         # 결과 포맷팅
        result = self.utils.round_result(result, **kwargs)
        
        return result

    # 곱셈
    def multiply(self, *args, **kwargs):
        result = args[0]  # 첫 번째 인자로 초기값 설정

        result = args[0]  # 첫 번째 인자로 초기값 설정

        for num in args[1:]:
            result *= num

         # 결과 포맷팅
        result = self.utils.round_result(result, **kwargs)
        
        return result
 
    # 나눗셈
    def divide(self, *args, **kwargs):
        result = args[0]  # 첫 번째 인자로 초기값 설정

        try:
            for num in args[1:]:  # 나머지 인자에 대해 반복
                result /= num
                
            # 결과 포맷팅
            result = self.utils.round_result(result, **kwargs)
            return result   # 결과를 직접 출력
        
        except ZeroDivisionError:
            print("오류: 0으로 나눌 수 없습니다.")
            return ""   # None 대신 빈 문자열로 반환

# Calculator 인스턴스 생성
calc = Calculator()


# 모듈 실행될 때 __name__ 의 값은 __main__ 이 된다.
# 모듈이 다른 파일에서 import될 때 __name__ 값은
# 해당모듈의 이름이 된다.
if __name__ == '__main__' :

    # 간단한 데모 코드 작성
    calc = Calculator()
    

    print("Basic Calculator Demo:")
    print(calc.add(1,2,3))
    print(calc.multiply(2,4,6))

# 데모 코드 작성 이유
# 각 클래스의 주요 기능을 보여주기 위해