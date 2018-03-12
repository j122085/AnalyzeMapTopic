stopwordset=set()
with open(r'stopwords.txt', 'r',encoding="big5") as sw:
		for line in sw:
			stopwordset.add(line.strip('\n'))
print(stopwordset)
