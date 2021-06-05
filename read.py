data = []
count = 0 
with open ('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		# 每1000行 顯示一次
		if count % 1000 == 0:
			print(len(data))

print(len(data))
print(data[0])