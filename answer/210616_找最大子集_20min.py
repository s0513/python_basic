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

1111111112223

Sample Output
5-------------------------answer

解釋
我們從串列中選擇以下最長子集：[1, 2, 2, 1, 2] 。
多重集中的每一對都有一個絕對差 ≦ 1（即，| 1 - 2 | = 1 ，| 1 - 1 | = 0 ，
和 | 2 - 2 | = 0），所以我們印出所選整數的數量「5」，作為我們的答案。
'''


def subset(input_list):
#    input_list.sort()   #排序input_list
    dic = {}    #存num:count
    max_num = 0     #最長子集的元素數量，最後return用
    
    for i in range(len(input_list)):    
        num = input_list[i]
        if num not in dic:  #建立字典
            num_count = input_list.count(num)
            dic[num] = num_count
    
            if num-1 not in input_list and num+1 not in input_list: #如果大於或小於自己的元素都不存在，只有自己
                if max_num <= num_count:
                    max_num = num_count
        
            else:   #如果只有大於或是小於自己的元素
                if num-1 in input_list:
                    num_count += input_list.count(num-1)
                elif num+1 in input_list:
                    num_count += input_list.count(num+1)
                
                if max_num <= num_count:
                    max_num = num_count
    
    return max_num


input_list = [1, 2, 2, 3, 1, 2]

max_num = subset(input_list)
print("最長子集的元素數量:", max_num)





