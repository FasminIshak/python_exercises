def Remove(duplicate): 
	final_list = [] 
	for num in duplicate: 
		if num not in final_list: 
			final_list.append(num) 
	return final_list 
	
duplicate = [1,11,21,31,41,51,1,42,3,57,42]
print(Remove(duplicate))