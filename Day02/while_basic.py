'''
* 반복문 (loop)

- 반복문은 유사한 명령을 반복해서 실행하는 제어문입니다,
- 파이썬의 반복문 키워드는 while, for ~in 이 있습니다.
'''

# while문에 필요한 3요소: 제어변수(begin), 조건식(end), 증감식(step)

i = 1
total = 0

while i <= 10:
    total += i
    i += i # 파이썬은 증감연산자가 없습니다. (++,--)

# print('1부터 10까지의 누적합: ', total)



x = int(input('첫번쨰 정수를 입력하세요: '))
y = int(input('두번쨰 정수를 입력하세요: '))

'''
if x > y:
    temp = x
    x = y
    y = temp
'''

if x > y:
    x,y = y,x

total = 0
n = x

while n <= y:
    total += n
    n += 1

print(x, '~' , y, '까지의 누적 합계: ' , total)