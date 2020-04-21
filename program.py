db = [

{"id": 1, 
"first_name": "Kelvin", 
"last_name": "De Guzman", 
"birthday": "August 05, 1989"
}, 

{"id": 2, "first_name": "Adriana", 
"last_name": "Boston Terrier", 
"birthday": "August 17, 2017"
}, 

{"id": 3, "first_name": "Anastasia", 
"last_name": "Boston Terrier", 
"birthday": "August 03, 2017"
}, 

{"id": 4, 
"first_name": "Juan", 
"last_name": "Dela Cruz", 
"birthday": "August 30, 2000"
}

]

def main_menu():
	print("------------------------")
	print("1. Show all\n2. Birthdays today\n3. Add\n4. Delete\n5. Exit")
	print("------------------------")
	menu_input = int(input("Enter menu item: "))

	if menu_input == 1:
		show_all()
	elif menu_input == 2:
		pass
	elif menu_input == 3:
		pass
	elif menu_input == 4:
		pass
	elif menu_input == 5:
		pass
	else:
		print('Invalid input')

def show_all():
	for item in db:
		print(f'''

		ID: {item['id']}
		Full name: {item['first_name'] + ' ' + item['last_name']}
		Birthday: {item['birthday']}
		Age:
			
			''')


main_menu()






