# *표준 출력 함수 print()
# ()안에 출력하고 싶은 변수, 리터럴 상수, 수식 등을 적으면
# 터미널에 텍스트 출력을 실행합니다.


'''
- 출력 할 데이터가 여러개라면 괄호 안에 출력할 데이터들을
콤마로 나열해서 작성합니다.
- 여러개의 값들을 공백과 함께 가로로 나란히 출력합니다.
'''

dog='멍멍이'
cat='야옹이'
print(dog, cat, '좋아요~')

'''
-print 함수 내부에는 sep이라는 속성이 존재합니다.
-sep은 separator의 약자로 구분자라고도 부릅니다.
- sep속성은 기본값이 ''(공백 문자열)로 지정되어 있으며
만약 변경을 원한다면 sep속성을 직접 작성하여 변경합니다.
'''

print('------------------------------------')
# print(dog, cat, '좋아요~', sep='') -> 기본값
print(dog, cat, '좋아요~', sep='')
print(dog, cat, '좋아요~', sep='＃')

'''
-end 속성은 데이터 출력 이후 맨 끝에 포함할 문자를
지정하는 용도입니다.

-기본 값은 '\n'이 지정되어 있기 때문에
print함수를 쓸 때마다 자동으로 줄 개행이 되는것처럼 보입니다.
'''

# print(dog, cat, '좋아요~', end='\n') -> 기본값
print(dog, cat, '좋아요~', end=' ')
print('이 문장은 줄 개행이 됐을까요?')

print(dog, cat, '좋아요~', sep='~', end=' ')
# print(sep='~',  end=' ', dog, cat, '좋아요~' ) (x) sep과 end는 뒤로 가야함, 둘 순서는 바뀌어도 괜춘