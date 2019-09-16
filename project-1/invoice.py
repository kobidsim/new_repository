def spacing(y,x): #name, price, amount haru print garda format milauna banako
	space=''
	for i in range(y-x):
		space=space+' '
	return space
	


def invoice_1(dict,item_1,amount_1,nam):
	total=0 #totl price customer has to pay
	print('Customer name: ',nam)#prints the customer's name
	print('S.N.','|','Item Name  ','|','No. of Items','|','Price of item','|')
	for i in range(len(item_1)):
		print('  ',i+1,'|',item_1[i],spacing(10,len(item_1[i])),'|','    ',amount_1[i],spacing(6,len(str(amount_1[i]))),'|','    ',dict[item_1[i]][0],spacing(7,len(str(dict[item_1[i]][0]))),'|')
		total=total+(amount_1[i]*dict[item_1[i]][0])
	print('Your total cost is : ',total)

def store_invoice(nam,item_1,amount_1):
	file=open('invoicedata.txt','a+')#appends the file invoicedata
	#appends invoicedata file with customer name,item ordered and no, of items
	for i in range(len(item_1)):
		file.write(nam+','+item_1[i]+','+str(amount_1[i])+'\n')
	file.close()

