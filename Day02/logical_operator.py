'''
* 논리 연산자 (&, |, and, or, not)

# &,and 연산자는 좌항과 우항의 논리값이 모두 True일 경우에만 전체 결과를 True로 도출합니다.
(and를 더 많이 씀)


'''

a = 6

if a > 1 and a < 10:
    print('a는 1보다 크고, 10보다는 작습니다')
else:
    print('a는 1~10 사이의 숫자가 아닙니다.')


# 파이썬은 위의 식을 연결해서도 작성할 수 있습니다.
if 1 < a < 10:
    print('OK!')


'''
|, or 연산자는 좌항과 우항의 논리값이 한 쪽만 True여도
전체 결과를 True로 도출
'''


'''
* 단축 평가 연산 (short circuit: and, or)
- 좌항에서 전체 결과가 판명났을 경우
우항 연산을 진행하지 않는 연산자입니다.
'''

c = 0

if(c == 0) | (10/c == 5):  # 우항에서 100% 에러가 나는 상황
    print('에러없이 통과!')

# not 연산자는 논리값을 반전시킵니다.

'''
- C언어에서는 정수 0을 False로 해석하고, 0이 아닌
모든 정수를 True로 해석합니다. (논리형 타입이 없어서)
파이썬에서도 C의 논리해석을 그대로 적용시킬 수 있습니다.
'''

apple = 5
if not apple:
    print('사과가 하나도 없습니다.')
else:
    print('사과가', apple, '개 있습니다.')








