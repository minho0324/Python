



ssn = input('주민등록번호 입력하세요: ')
#990909-1234567

print('주민등록번호 앞자리: ', ssn[:6])
print('주민등록번호 뒷자리: ', ssn[7:])

year = int(ssn[:2])
month = ssn[2:4]
day = ssn[4:6]
gender_num = ssn[7]

if gender_num == '1' or gender_num == '3':
    gender = '남자'
else:
    gender = '여자'

birth_year = 0

if gender_num == '1' or gender_num == '2':
    birth_year = 1900 + year
else: 
    birth_year = 2000 + year

age = 2021-birth_year

print(f'{birth_year}년 {month}월 {day}일 {age}세 {gender}')




'''
x = ssn[:6] #주민번호 앞자리 수 자른거
y = ssn[7:] #주민번호 뒷자리 수 자른거
x1 = ssn[:3] #주민번호 연도 자른거
y1 = ssn[3:] #주민번호 성별 자른거

print(x,y)

if x[0] > 0:
    if y[0] == 1 or 3:
        #m = '남자'
        print(f'19{x1}')
    elif y[0] == 2 or 4:
        #f = '여자'
        print(f'')
elif 

'''






