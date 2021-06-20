'''
題目:給一個數字n，印出 1~n
但如果碰到3的倍數，改印Fizz
碰到5的倍數，改印Buzz
若同時是3跟5的倍數，印FizzBuzz

備註:
1.複習 try & except
2.import time 模組測執行時間
'''

        
#fizzbuzz
#while True:
#    try:
#        n = int(input('輸入數字:'))
#        break
#    except ValueError:
#        print('請輸入數字')
import time
start = time.time()

n=100

##1
#for i in range(1,n+1):
#    if i % 3 == 0:
#        if i % 5 == 0:
#            print('FizzBuzz')
#        print('Fizz')
#    elif i % 5 == 0:
#        print('Buzz')
#    else:
#        print(i)

#2
for i in range(1, n+1):
    result = ""
    if i % 3 == 0:
        result += "Fizz"
    if i % 5 == 0:
        result += "Buzz"
    if len(result) > 0:
        print(result)
    else:
        print(i)
        

end = time.time()
print('執行時間: %f 秒' % (end - start) )

'''
其他:虛擬碼練習
for (i from 1 to n) do
    if (i % 15 === 0) print "FizzBuzz"
    else if (i % 3 === 0) print "Fizz"
    else if (i % 5 === 0) print "Buzz"
end for
'''

#for i in range(1,n+1):
#    if i % 15 == 0:
#        print('FizzBuzz')
#    elif i % 3 == 0:
#        print('Fizz')
#    elif i % 5 == 0:
#        print('Buzz')
#    else:
#        print(i)


