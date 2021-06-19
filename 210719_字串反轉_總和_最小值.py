"""
一疊撲克牌找最小值
想法:跟第一張比對
"""

"""
proj1
1. 字串反轉
給一個字串 str，請輸出 str 反過來的結果
範例輸入：hello
範例輸出：olleh
PS. 可以用 str[i] 取得第 i 個字，例如說 str="abc"，str[0] 就是 'a'

2. 陣列總和
給一個陣列 arr，裡面全都包含了數字（整數），請輸出陣列加總的結果（總和保證不超過 int 範圍）
範例輸入：[1, 2, 3]
範例輸出：6
##2
#arr = [1, 2, 3]
#result = 0
#for i in range(len(arr)):
#    result += arr[i]
#print(result)


3. 找最大值
給一個陣列 arr，裡面全都包含了數字（整數），請輸出陣列中的最大值
範例輸入：[1, 2, 3]
範例輸出：3
##3
#arr = [1, 2, 3]
#max_ = arr[0]
#for i in range(len(arr)):
#    if max_ < arr[i]:
#        max_ = arr[i]
#print(max_)
"""

'''
1. 字串反轉
給一個字串 str，請輸出 str 反過來的結果
範例輸入：hello
範例輸出：olleh
PS. 可以用 str[i] 取得第 i 個字，例如說 str="abc"，str[0] 就是 'a'
怎麼把一個字一個字印出來
1.for迴圈取最後一個
2.放到output.append
'''
#input_ = 'hello'
#output = []
#for i in range(len(list(input_))-1, -1, -1):
#    output.append(str(list(input_)[i]))
#output_ = ''.join(output)
#print(output_)
#
#print('hello'[::-1])

input_ = 'hello'
output = ''
for i in range(len(input_)-1, -1, -1):
    output += input_[i]
print(output)









