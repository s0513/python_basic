'''
心得:
1.複習 try & except
2.import time 模組測執行時間

'''

        
#fizzbuzz
#while True:
#    try:
#        n = int(input('輸入數字:'))
#        break
#    except:
#        print('請輸入數字')
import time
start = time.time()

n=100

for i in range(1,n+1):
    if i % 3 == 0:
        if i % 5 == 0:
            print('FizzBuzz')
        print('Fizz')
    elif i % 5 == 0:
        print('Buzz')
    else:
        print(i)
        
#for i in range(1,n+1):
#    if i % 15 == 0:
#        print('FizzBuzz')
#    elif i % 3 == 0:
#        print('Fizz')
#    elif i % 5 == 0:
#        print('Buzz')
#    else:
#        print(i)

end = time.time()
print('執行時間: %f 秒' % (end - start) )
