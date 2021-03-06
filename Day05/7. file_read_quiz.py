
'''
* points.txt 파일의 숫자값을 모두 읽어서
총합과 평균을 구한 뒤
총점, 평균값을 result.txt라는 파일에
쓰는 프로그램을 작성해 보세요.
'''
import traceback as trace

try:
    f = open('C:/Users/minho/Desktop/test/points.txt', 'r')
    numlist = f.read().split()
    print(numlist)
except:
    print('파일 로드 실패!')
    print(trace.format_exc())
finally:
    f.close()

sum = 0
for num in numlist:
    score = int(num)
    sum += score
    print(score)
    
avg = sum / len(numlist)

try:
    f = open('C:/Users/minho/Desktop/test/result.txt', 'w')
    data = f'총점:{sum}, 평균:{avg}점'
    f.write(data)
    print('파일저장 완료!')
except:
    print('저장 실패!')
    print(trace.format_exc)
finally:
    f.close()



