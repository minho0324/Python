

import random as r

answer = r.randint(1,100)
print(answer)

x = int(input('1~100사이 숫자를 입력하세요: '))

'''
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
'''

secret = r.randint(1,100)
count = 0 # 몇번만에 정답을 맞췄는지를 파악할 변수
count_down = 6

print('[UP & DOWN 게임 - 1~100 사이의 숫자 중 어떤 숫자가 들어있을까요?]')

while True:
    print('-' * 40)
    num = int(input('숫자를 입력하세요: '))
    count += 1
    count_down -= 1

    if num == secret:
        print(f'정답입니다!! {count}번 만에 맞추셨네요!')
        if count_down > 0:
            print('이겼습니다.')
        else:
            print('졌어요 ㅠㅠ')
        break
    elif num < secret:
        print('UP!!')
    else:
        print('DOWN')

    if count_down > 0:
        print(f'정답 기회가 {count_down}번 남았습니다!')
    else:
        print('정답 기회 모두 소진! 계속 문제를 풀어주세요.')
