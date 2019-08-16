def initialize(string):
	words = string.split()
	initials = ''
	if len(words)>2:
		list_ = [words[0]]
		for i in range(1,len(words)-1):
			initials += ''.join([words[i][0],'.'])
		list_.append(initials)
		list_.append(words[-1])
		print(" ".join(list_))	
	else:
		print(string)


str_list = ['Jack Ryan','Lois Mary Lane','Dimitri','Alice Betty Catherine Davis']
for i in str_list:
	initialize(i)
