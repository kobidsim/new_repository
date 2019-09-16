def data_update(dict,item_1,amount_1):
	#edits the amount of items available in the data stored in dictionary
	for i in range(len(item_1)):
		dict[item_1[i]][1]=dict[item_1[i]][1]-amount_1[i]
	f=open('products.txt','w')
	#writes the the edited data in products file
	for i,j in dict.items():
		f.write(i)
		for k in j:
			f.write(','+str(k))
		f.write('\n')
	f.close()
	return dict

