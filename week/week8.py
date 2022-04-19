def initialize():
	data = []
	try:
		f = open("records.txt", "r")	
		money = int(f.readline())
		read_data = f.readlines()
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
	
	try:
		money = int(money)
	except:
		money = 0
		print("Invalid value for money. Set to 0 by default.")
	return data, money
def add():
	x = input("add an expense or income record with description and amount: ").split()
	if len(x) == 2:
		try:
			record = [x[0], int(x[1])]
			return record
		except:
			print("invalid value for money\nfail to add a record ")
	else:
		print("the format of a record should be like this: breakfase -50 ")

def view():
	print("here is your expense and income records:")
	print("description".ljust(20) + "amount")
	print("=" * 30)
	bal = money
	for x in data:
		print(x[0].ljust(20) + str(x[1]))
		bal += x[1]
	print("=" * 30)
	print("now you havae " + str(bal) + " dollars")

def delete():
	x = input("which record do you want to delete").split()
	print(x)
	try:
		record = [x[0], int(x[1])]
		if record in data:
			return record
		else:
			print("theres no record with" + x[0] + " " + x[1] + ". fail to delete a record ")
	except:
		print("invalid format, fail to delete a record ")

def exit():
	f = open("records.txt", "w")
	data_write = str(money) + "\n"
	for x in data:
		data_write += (x[0] + " " + str(x[1]) + "\n")
	f.write(data_write)
	print("program end")

data, money = initialize()
while True:
	action = input("What do you wan to do (add / view / delete / exit)? ")
	if action == "add":
		record = add()
		if record:
			data.append(record)
	elif action == "view":
		view()
	elif action == "delete":
		record = delete()
		if record:
			data.remove(record)
			
	elif action == "exit":
		exit()
		break
	else:
		print("invalid command. try again")












