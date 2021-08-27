print('저장할 내용을 입력(\'그만\'이라고 입력시 종료됩니다.')

user_input = ''
while True:
    temp = input('> ')
    if temp == '그만':
        break
    user_input += temp + '\n'

f_name = input('파일명을 입력: ')
f_path =  f'C:/Users/minho/Desktop/test/{f_name}.txt'

try:
    f = open(f_path, 'a')
    f.write(user_input)
    print('파일 저장 성공')
except:
    print('파일저장 실패!')
finally:
    f.close



