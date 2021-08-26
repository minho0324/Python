
'''
* 함수 (function)

- 함수는 지속적으로 사용되는 코드블록에 이름을 붙여놓은 형태입니다.

- 함수는 한 번 정의해 두면 지정된 함수 이름을 통해
 언제든지 해당 코드 블록을 실행할 수 있습니다.

- 함수를 정의할 때는 def라는 키워드를 사용합니다.

- 정의해 놓은 함수를 사용하는것을 호출(call) 이라고 부릅니다.

- 파이썬에서는 함수를 호출하려면 반드시 호출문보다 상단부에
 함수를 먼저 정의해야 합니다.
'''

# 함수의 정의 (1-x까지의 누적합을 구하는 로직)
def calc_sum(x):
    sum = 0
    for n in range(1,x+1):
        sum += n
    return sum

# 함수의 호출
print('1~100까지의 누적합: ', calc_sum(100))

'''
* 인수, 매개변수 (arguments)

-인수는 함수를 호출할 때 함수 실행에 필요한 값들을 전달하는
매개체 역할을 하며, 그렇기 때문에 매개변수(parameter) 라고도 부른다.

-인수의 개수는 제한이 없어 많은 값을 함수에 전달할 수도 있고
하나도 전달하지 않을수도 있다.

- 파이썬의 경우에는 데이터 타입을 작성하지 않기 때문에
이 함수를 처음 사용하는 사람도 인수 이름만 보고 무슨값을
전달해야 할지 의미를 알기 쉽게 지정하는것이 좋다.
'''



def calc_rangesum(start, end):
    sum = 0
    for n in range(start, end+1):
        sum += n
    return sum

print('-' * 40)

start = int(input('시작값 입력하세요: '))
end = int(input('끝값 입력하세요: '))
print('x~y까지의 누적합: ', calc_rangesum(3,7))

'''
* 반환값 (return value)

- 반환값이란 함수를 호출한 곳으로 함수의 최종실행 결과를 전달하는 값이다.

- 인수는 여러 개 존재할수있지만, 반환값은 언제나 하나만 존재해야한다.

- 모든 함수가 반환값이 있는것은 아닙니다,
함수 실행 후에 딱히 반환할 값이 없다면 return을 생략할수 있다.
'''

def add(n1,n2):
    return n1+n2
result = add(10,5) # result=15
print(add(add(5,7),add(9,8))) # add(12,17)

# n = int(input('정수:3')) -> n = int('3')

# 만약 여러 개의 값을 한번에 return해야 할때는
# 컬렉션 자료형을 사용합니다. (list, tuple, set ...)

def operate_all(n1,n2):
    return n1 + n2, n1 - n2, n1 * n2, n1 / n2
    #return n1 - n2
    #return n1 * n2


print(type(operate_all(10,5)))

def multi(n1,n2):
    result = n1*n2
    print(f'{n1} X {n2} = {n1*n2}')

#abc = multi(9,6) --> None
#print(abc)



