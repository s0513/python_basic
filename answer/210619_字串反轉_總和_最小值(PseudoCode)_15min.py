""" Lidemy [ALG101] 先別急著寫leetcode proj1 """
""" https://lidemy.com/courses/ """

'''
1. 字串反轉
給一個字串 str，請輸出 str 反過來的結果
範例輸入：hello
範例輸出：olleh
PS. 可以用 str[i] 取得第 i 個字，例如說 str="abc"，str[0] 就是 'a'

想法:
怎麼把一個字一個字印出來 -> 用for迴圈取最後一個

虛擬碼:
let output = ''
for (i from n-1 to 0) do
    output += str[i]
end for
print output
'''

#1.1
print('hello'[::-1])

#1.2
input_ = 'hello'
output = ''
for i in range(len(input_)-1, -1, -1):
    output += input_[i]
print(output)

##1.3 一開始忘了陣列可以取值，先轉成list處理的寫法
#input_ = 'hello'
#output = []
#for i in range(len(list(input_))-1, -1, -1):
#    output.append(str(list(input_)[i]))
#output_ = ''.join(output)
#print(output_)

###############################################################

'''
2. 陣列總和
給一個陣列 arr，裡面全都包含了數字（整數），請輸出陣列加總的結果（總和保證不超過 int 範圍）
範例輸入：[1, 2, 3]
範例輸出：6

虛擬碼:
let sum = 0
for (i from 0 to n-1) do
    sum += arr[i]
end for
print sum
'''

#2
arr = [1, 2, 3]
result = 0
for i in range(len(arr)):
    result += arr[i]
print(result)

###############################################################

'''
3. 找最大值
給一個陣列 arr，裡面全都包含了數字（整數），請輸出陣列中的最大值
範例輸入：[1, 2, 3]
範例輸出：3

想法:跟第一張比對

虛擬碼:
let max = arr[0]
for (i from 0 to n-1) do
    if (arr[i] > max) do
        max = arr[i]
    end if
end for
print max
'''

#3
arr = [1, 2, 3]
max_ = arr[0]
for i in range(len(arr)):
    if arr[i] > max_:
        max_ = arr[i]
print(max_)












