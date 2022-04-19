# init read data
data = []
## (7)(8)
try:
	f = open("records.txt", "r")	
	## (9)
	money = int(f.readline())
	read_data = f.readlines()
	## (10)
	for x in read_data:
		data.append([x.split()[0], int(x.split()[1])])
	f.close()
	print("Welcome bak!\n")
except:
	print("Invalid format in records.txt. Deleting the contents. ")
try:
	money
except:
	money = input("How much money do you have?")
	
# 10 exception solving that this question required
## (1)
try:
	money = int(money)
except:
	money = 0
	print("Invalid value for money. Set to 0 by default.")

while True:
	action = input("What do you wan to do (add / view / delete / exit)? ")
	if action == "add":
		x = input("add an expense or income record with description and amount: ").split()
		## (3)
		if len(x) == 2:
			try:
				data.append([x[0], int(x[1])])
			except:
				## (4)
				print("invalid value for money\nfail to add a record ")
		else:
			print("the format of a record should be like this: breakfase -50 ")
	elif action == "view":
		print("here is your expense and income records:")
		print("description".ljust(20) + "amount")
		print("=" * 30)
		bal = money
		for x in data:
			print(x[0].ljust(20) + str(x[1]))
			bal += x[1]
		print("=" * 30)
		print("now you havae " + str(bal) + " dollars")
	elif action == "delete":
		x = input("which record do you want to delete").split()
		print(x)
		try:
			record = [x[0], int(x[1])]
			try:
				data.remove(record)
			except:
				## (6)
				print("theres no record with" + x[0] + " " + x[1] + ". fail to delete a record ")
		except:
			## (5)
			print("invalid format, fail to delete a record ")
			
	elif action == "exit":
		f = open("records.txt", "w")
		data_write = str(money) + "\n"
		for x in data:
			data_write += (x[0] + " " + str(x[1]) + "\n")
		f.write(data_write)
		print("program end")
		break
	else:
		## (2)
		print("invalid command. try again")












