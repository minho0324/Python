

import random as r

answer = r.randint(1,100)
print(answer)

x = int(input('1~100사이 숫자를 입력하세요: '))

while True:
    if x > answer:
        print('DOWN!')
        print(input('> '))
        continue
    elif x < answer:
        print('UP!')
        print(input('> '))
        continue
    elif x == answer:
        print('CORRECT!')
        break