data = []
count = 0 
data_len = 0
with open ('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		# 每1000行 顯示一次
		if count % 1000 == 0:
			print(len(data))
		data_len = data_len + len(line)
print('檔案讀取完畢,總共', len(data), '筆data')

avg_len = data_len/len(data)
print('留言平均長度', avg_len)

# 官方解法
# 留言平均長度
sum_len = 0
for d in data:
	sum_len = sum_len + len(d)

avg_len_2 = sum_len/len(data)

print('留言平均長度', avg_len_2)

#篩選
new = []
for d in data:
	if len(d) < 100:
		new.append(d)

print('總共', len(new), '筆資料長度小於100')
print(new[0])
print(new[1])

good = []
for d in data:
	if 'good' in d:
		good.append(d)
print('一共有',len(good) , '筆留言提到good')
print(good[0])

#清單快寫法
#list comprehension
#第一個d ==> good.append(d)
good = [d for d in data if 'good' in d]
# output =[ (number-1) for number in reference if number %2 = 0 ]
#             運算          變數        清單         篩選條件
print ('一共有',len(good) , '筆留言提到good')

#裝1進入清單
good = []
good = [1 for d in data if 'good' in d]
print(len(good))

#運算結果 'bad' in d
#檢查100萬筆留言
#是否含有bad 字串
#結果會是100萬筆 True/False
bad = ['bad' in d for d in data]
print(len(bad))
print(bad)