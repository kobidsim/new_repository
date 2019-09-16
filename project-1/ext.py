def extract_data():
	new_list=[]
	new_dict={}
	f=open("products.txt",'r')
	#collects the data in new_list:
	for i in f:
		new_list.append(i.replace('\n','').split(','))
	f.close()
	n_list=[]
	#collects the data in a dictionary new_dict:
	for i in range(len(new_list)):
		new_list[i][1]=int(new_list[i][1])#converts the price into integers
		new_list[i][2]=int(new_list[i][2])#converts the amount into integers
		n_list.append(new_list[i][1])#saves the price in n_list
		n_list.append(new_list[i][2])#saves the amount in n_list
		new_dict[new_list[i][0]]=n_list#saves the name of item as key and n_list as value
		n_list=[]#empties n_list for the next loop
	return new_dict #returns the dictionary that contains all the data from products

def present(d):
	from invoice import spacing
	print('Here are our products:')
	print('S.N.','|','Item Name  ','|','Price of Item ','|','No. of Items','|')
	a=0 #for symbol number(S.N)
	for i,j in d.items():#dictionary bata sab bhako item, price, amount print garcha
		a=a+1
		print('  ',a,'|',i,spacing(10,len(i)),'|','    ',j[0],spacing(8,len(str(j[0]))),'|','     ',j[1],spacing(5,len(str(j[1]))),'|')
	print('\n')

