'''
題目是這樣的，會先給你一堆用空行分隔的字串，你要把幾個字串拼起來變成一個大的字串
接下來會給你一些數字 a1...an，你要求出這個字串裡面第 ai 個字拼起來的結果。
舉例來說，一開始會給一個數字 n，後面跟著 n 行字串：

3
hello
world
yo

把這些字串拼起來，就會變成一個更長的字串 S，以上面的範例來說，S 就是 helloworldyo。
接著會給一個數字 m，代表接下來有 m 個用空行分隔的數字 ，例如說：

2
9
1

就代表要把第 9 個字還有第 1 個字合起來（字串的第一個字就是第一個字，不是第零個字）

helloworldyo 的第九個字元是：l
helloworldyo 的第一個字元是：h

因此答案就是：lh
完全不會寫程式的小明跑來找你求助，你必須趕快完成這道程式，才能幫助小明順利取得前往聯誼的門票！
'''

'''
Input
第一行為一個數字 n，1 <= n <= 100
接著會有 n 行字串，分別是 S1 到 Sn，每一行的長度皆不超過 100，而且內容保證為小寫英文字母
再來會有一個數字 m，1 <= m <= length(S)
接著會有 m 行數字，分別是 A1 到 Am

Output
請輸出拼接起來的字串 S 裡面第 Ai 個字加總起來的結果 
'''

#input第一行為數字
while True:
    try:
        n = int(input('數字:'))   #input數字
        if 1 <= n and n <= 100:     #數字不在 1 <= n <= 100 的範圍
            break
        else:
            print('輸入數字的範圍不是1 <= n <= 100哦，請重新輸入')
    except:     #不是數字，ValueError
        print('不是數字哦，請重新輸入')

input_list = []     
output_list = []

for i in range(n):
    input_str = input('字串:').lower()    #內容保證為小寫英文字母
    while len(input_str) > 100:     #每一行的長度皆不超過 100
        print('字串太長請重新輸入')     
    input_list.append(input_str)

combine_input = list(''.join(input_list))

#input為數字
while True:
    try:
        m = int(input('數字:'))   #input數字
        if 1 <= m and m <= n:     #數字不在 1 <= n <= 100 的範圍
            break
        else:
            print('輸入數字的範圍不是1 <= m <= length(S)哦，請重新輸入')
    except:     #不是數字，ValueError
        print('不是數字哦，請重新輸入')
   
for i in range(m):
    index = int(input('數字:'))
    pick_index = combine_input[index-1]
    output_list.append(pick_index)

output_list_str = ''.join(output_list)

print('答案=', output_list_str)





