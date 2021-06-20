'''
題目:
給定一個整數串列，找到其中任意兩個元素之間的差距小於或等於 1 的最長子集。

Example:
a = [ 1, 1, 2, 2, 4, 4, 5, 5, 5 ]
有兩個子集滿足該標準：[1, 1, 2, 2] 和 [4, 4, 5, 5, 5]。 最大長度子集有 5 個元素。

限制:
1. 2 ≦ n ≦ 100( 給定一串列的長度)
2. 0 < a[i] < 100( 串列中每個元素的大小 )
3. 答案自少要 ≧ 2.


sample input
6 -----------------------n
1 2 2 3 1 2 --------------a[i]

Sample Output
5-------------------------answer

解釋
我們從串列中選擇以下最長子集：[1, 2, 2, 1, 2] 。 多重集中的每一對都有一個絕對差 ≦ 1
（即，| 1 - 2 | = 1 ，| 1 - 1 | = 0 ，和 | 2 - 2 | = 0），
所以我們印出所選整數的數量「5」，作為我們的答案。
'''


def check_n():
    global n
    while 2 > n or n > 100:
        print('你輸入的串列長度不對哦，請重新輸入~')
        n = int(input('請給定一串列的長度(2 ≦ n ≦ 100):'))

def check_a():
    global a
    a.sort()
    for i in range(len(a)):
        while 0 >= a[i] or a[i] >= 100:
            print('你輸入的串列元素大小不在1到99的數字，請重新輸入~')
            a = [int(i) for i in input('請輸入長度為n，每個元素大小為1到99的數字(按空白鍵分隔):').split(' ')]



n = int(input('請給定一串列的長度(2 ≦ n ≦ 100):'))
check_n()

#a = input('請輸入長度為n，每個元素大小為1到99的數字(按空白鍵分隔):').split(' ')
#for i in range(len(a)): #字串轉整數
#    a[i] = int(a[i])
a = [int(i) for i in input('請輸入長度為n，每個元素大小為1到99的數字(按空白鍵分隔):').split(' ')]
check_a()

while n != len(a):
    print('你輸入的串列不符合串列長度哦，請重新輸入~')
    n = int(input('請給定一串列的長度(2 ≦ n ≦ 100):'))
    check_n()
    a = [int(i) for i in input('請輸入長度為n，每個元素大小為1到99的數字(按空白鍵分隔):').split(' ')]
    check_a()
    
subset_len = 0
subset_list_len =[]
subset_list=[]
subset = []
for i in range(n):
    for j in range(n):
        if a[j] >= a[i]:
            if a[j] - a[i] <= 1:
                subset.append(a[j]) 
    subset_len = len(subset) 
    subset_list_len.append(subset_len)
    subset_list.append(subset)
    subset = []
print('子集=', subset_list)
print('最大長度子集=', max(subset_list_len), '個元素')


