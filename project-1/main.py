from ext import extract_data
dict=extract_data() #it extracts all the data from products and stores in dictionary
from invoice import spacing
from ext import present
present(dict) #it displays all the products that the shop offers
more=True #to check if the customer wants to buy more
success=False #for try and except
item_1=[] #all the items that customer wants to buy
amount_1=[] #the number of items that the customer wants to buy
while success==False: #loop repeats if there is an error
	try:
		nam=input('What is your name? ')
		while more==True:
			#collects all the information from the customer
			print('Please be careful with the syntax of item name!')
			item_1.append(input('What would you like to buy? '))
			amount_1.append(int(input('How many would you like to buy? ')))
			y_n=input('Would you like to buy more?(y/n) ')
			if y_n.upper()=='N':
				more=False			
		print('\n')
		from updates import data_update
		data_update(dict,item_1,amount_1) #it updates the data stored in products file
		from invoice import invoice_1
		invoice_1(dict,item_1,amount_1,nam) #it creates an invoice for the customer
		from invoice import store_invoice
		store_invoice(nam,item_1,amount_1) #it stores invoice in invoicedata file

		lol=input()
		success=True #this exits the loop if the code executes correctly
	except:
		print('You might have entered item name in the wrong syntax! Try again.')
		print('For example : TV should be entered as "TV" and not "tv"')