
'''
* for ~ else문을 이용한 범위 안의 모든 소수 출력하기
for문 내부에서 중간에 반복문의 종료없이 지정된 범위까지
모두 반복이 된 후에 else문이 실행되는구조입니다.
존재 유무 등 논리값을 통해서 확인하던 문제를
for ~ else문을 통해 확인하는것이 가능합니다. (flag)
'''

n1,n2 = map(int, input('정수 2개를 입력하세요: ').split())

if n1 > n2: # n1이 클 경우, 숫자를 바꿔치기한다.
    n1,n2 = n2,n1

cnt = 0 # 소수의 개수를 저장할 변수.

for i in range(n1,n2+1):  
    for j in range(2, i): 
        if i % j == 0:
            break
    else: # for문에서 break가 한번도 동작하지 않으면 else문이 발동한다.
        print(i, end=' ')
        cnt += 1


print('\n소수의 개수: ',cnt,'개')




