


'''
- 서로 다른 정수가 담긴 두 개의 리스트를 비교하여
li 안에 있는 정수가 li2에도 담겨있다면 그 정수를 배제하세요.
서로 겹치지 않는 정수만 담긴 새로운 리스트를 생성해보세요.
'''

li = [1,2,3,4,5,6,7]
li2 = [1,3,8,4,5,7,101]
li3 = []

result = set(li) ^ set(li2)
print(list(result))
result.sort()
print(result)

''''
for n in li:
    if n not in li2:
        li3.append(n)
'''




sum = (set(li) | set(li2)) - (set(li) & set(li2))
print('sum', sum)

'''
common = set(li) & set(li2)
print('common',common)

a = sum - common
print(a)

li3.append(a)
print(li3)
'''

































