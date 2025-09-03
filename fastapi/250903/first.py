# 타입힌트
# 타입이 불일치 한다고 해서 실행이 안되는 것은 아님.
# 타입힌트는 개발시 서로간의 규칙을 정하기 위한 것.
# dict, tuple, set, int, str, bool 등


def typeHint(a: str, b: int) -> str:

    print(a)

    return b  # 반환타입 불일치


typeHint(10, 11)  # 첫 번째 파라미터 타입힌트 오류
typeHint("good", "good")  # 두 번째 파라미터 타입힌트 오류

# 퀴즈
# 1. 두가지 변수(첫번째 변수 int, 두번째 변수 str) 반환값 정수형
# 2. 두가지 변수를 곱하여 반환한다.


def twoTypeHint(a: int, b: str) -> int:

    return a * int(b)

print(twoTypeHint(10,"109"))
