'''
題目:
小明和小華生完第一個孩子後非常高興，他們的兒子喜歡玩具，
所以小明想買一些玩具。他面前擺著許多不同的玩具，
上面標有它們的價格，他想用手上的錢最大程度地購買玩具。
給定玩具的價格清單和能夠花費金額，
確定他可以購買的最大禮物數量。
#註: 注意每個玩具只能購買一次。

Example:
玩具價格清單 = [ 1, 2, 3, 4 ]
手上的錢k = 7
所以預算為7個貨幣單位，他可以購買組合為[1、2、3]或[3、4]，因此最多3個玩具。

限制:
1. 玩具清單n最長為10個項目
2. 玩具價格i最高100
3. 手上有的錢k最高150
'''


import random

#i = random.randint(1,100)    #玩具價格最高100
#n = [random.randint(1,101) for i in range(random.randint(1,11))]    #玩具清單最長為10個項目，價格最高100
n = random.sample(range(1,101), random.randint(1,11))    #玩具清單最長為10個項目(不重複)，價格最高100
n.sort()    #玩具清單價格排序
print('玩具的價格清單=', n)    #print玩具清單價格

k = random.randint(1,151)  #手上的錢k最高150元
print('能夠花費金額=', k)     #print手上能夠花費金額

#確定他可以購買的最大禮物數量
for num in range(1, len(n)+1):  
    price = sum(n[0:num])   #禮物加起來的價格
    if price >= k:  #終止條件:禮物加起來的價格 > 手上能夠花費金額
        print('max_gift_num=', num - 1)
        break
    else:        
        if num == len(n):   #如果可以買所有禮物
            print('max_gift_num=', num)
            
    