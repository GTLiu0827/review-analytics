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


