


'''
* 사용자의 입력을 파일(xxx.txt)에 저장하는 프로그램을 작성하세요.
(단, 프로그램을 다시 실행하더라도 파일명이 동일하다면
기존 작성한 내용을 그대로 유지하고
새로 입력된 내용이 추가되어야 합니다.
파일명도 마지막에 입력받아서 생성하세요.)
'''



print('저장할 내용을 입력(\'그만\'이라고 입력시 종료됩니다.')

user_input = '' # 입력받은 텍스트를 저장해 둘 변수 선언
while True:
    temp = input('> ')
    if temp == '그만':
        break
    user_input += temp + '\n'

f_name = input('파일명을 입력')
f_path = r'C:\Users\minho\Desktop\test\{f_name}.txt'

try:
    f = open(f_path, 'a')
    f.write(user_input)
except:
    print('파일 저장 실패!')
finally:
    f.close()




