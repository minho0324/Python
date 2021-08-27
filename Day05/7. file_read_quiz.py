


try:
    f = open(r'C:\Users\minho\Desktop\test\points.txt', 'r')
    numlist = f.read().split()

except:
    print('파일 로드 실패!')
finally:
    f.close()

sum = 0
for num in numlist:
    score = int(num)
    sum += score

avg = sum / len(numlist)

try:
    f = open(r'C:\Users\minho\Desktop\test\result.txt', 'w')
    data = f'총점은: {sum}점, 평균:{avg:0.2f}점'
    f.write(data)
    print('파일 저장이 완료되었습니다.')
except:
    print('파일 저장 실패!')
finally:
    f.close()