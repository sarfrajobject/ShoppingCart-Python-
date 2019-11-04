class soping:
	def __init__(self):
		self.d={}
		self.c={}
		self.a=[]
	def displayList(self):
		for item in self.d:
			print(item,": price:",self.d[item],"qty",self.c[item])	
		chooise = self.chooseAction()
		self.acceptInput(chooise)	
	def BuydisplayList(self):
	   for x in self.a:
	   	print(x,": price:",self.d[x],"qty",self.c[x])
	   chooise = self.chooseAction()
	   self.acceptInput(chooise)	   	
	def Additem(self):
		item=input("Enter the item :")
		qty=int(input("Enter the item qty :"))
		price=int(input("Enter the item price :"))
		self.d[item] = price
		self.c[item] = qty
		chooise = self.chooseAction()
		self.acceptInput(chooise)
	def BuyItem(self):
		Buyitem2=input("Enter the Buy item :")
		qty=int(input("Enter the item qty !You want :"))
		if qty<=self.c[Buyitem2]:
			print("\n")
		else:
			print("Sorry!No avalible qty")	
		self.c[Buyitem2] = qty
		if(Buyitem2 in self.d):
			self.a.append(Buyitem2)

		else:
			print ("Item not exist")

		chooise = self.chooseAction()
		self.acceptInput(chooise)
	def totalcost(self): 
		mytotalcost=0
		for name in self.a:
			mytotalcost = mytotalcost + self.d[name]*self.c[name]		
	    
		return mytotalcost	


	def chooseAction(self):

		print("1.Add item ")
		print("2.Display cart ")
		print("3.Delete cart ")
		print("4.update cart ")
		print("5.shoping cart ")
		print("6.Display BuydisplayList: ")
		print("7.genrate cart ")
		chooise = input("Enter the opretion !1,2,3,4,5,6,7:")
		return chooise
	def acceptInput(self,chooise):
		if chooise=='1':
			self.Additem()
		elif chooise=='2':
			self.displayList()
		elif chooise=='3':
			item=input("Enter the Delete item :")
			del self.d[item]
			self.displayList()
		elif chooise=='4':	
			self.Additem()	
		elif chooise=='5':
			self.BuyItem()
		elif chooise=='6':
			self.BuydisplayList()
		elif chooise=='7':
			print (self.totalcost())
		else:
			print("2.Please correct opretion ")


y = soping()
chooise = y.chooseAction()
y.acceptInput(chooise)



























	# def priceCalc():
# 	return totalCost
# def displayList(list):
#    for x in list:
#    	print(x,": Quantity:",list[x])

# displayList(d)

# item = input("Enter the item for buy:")
# if item in d:
#   qty= int(input("Enter the item Quantity:"))
#   d[item] = d[item]-qty
#   totalCost = qty*price[item]
#   print("Your total cost of item:",totalCost)
 

#   print("Reamining List of item ")
#   displayList(d)

# else:
# 	print("Please enter the item from below list")
# 	displayList(d)

# for x i:
# 	if item in d:
# 		print("Buy item:",item)
# 		Quantity = input("Enter the Quantity !you want:")
# 	else:
# 		print("No item! try again")
	  


# 	print ("Item \t\t Quantity\n",item,"\t\t",Quantity)

# 	d["mango"] = d["mango"] - 1

# 	print(d)