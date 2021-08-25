# 리스트는 인덱싱을 사용하여 변수처럼 내부의 값을 변경할 수 있다.
print('-' * 40)
print(nums)

nums[2] = 34
print(nums)

nums[7] = 88
print(nums)

nums[3] = nums[6]
print(nums)


'''
- 문자열은 상수 형태로 저장되는 고정형 리스트입니다.
- 따라서 인덱싱이나, 슬라이싱을 통해 값의 복사본을 활용하는 것은 가능하지만,
영역에 직접 접근하여 내부의 값을 편집할 수는 없습니다.
- 문자열은 변경이 불가능한 자료형입니다. (immutable)
'''


s = 'python'
# s[2] = 'x' (x)

#unpackaging : 리스트 내부 요소를 다시 변수에 저장

# pokemon = ['피카츄','라이츄', '파이리', '꼬부기', '버터풀']

'''
p = pokemon[0]
r = pokemon[1]
c = pokemon[2]
s = pokemon[3]
b = pokemon[4]
'''
#좌항의 변수의 개수와 우항의 리스트의 요소의 개수가 일치한다면
#자동으로 변수에 리스트 내부 요소의 값이 저장되게 됩니다.
p, r, c, s, b = pokemon
print(p,r,c,s,b)

# 빈 리스트 만들기
list1 = []
list2 = list()
print(list2)