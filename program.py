db = [

{"id": 1, 
"first_name": "Kelvin", 
"last_name": "De Guzman", 
"birthday": "August 05, 1989"
}, 

{"id": 2, 
"first_name": "Adriana", 
"last_name": "Boston Terrier", 
"birthday": "August 17, 2017"
}, 

{"id": 3, 
"first_name": "Anastasia", 
"last_name": "Boston Terrier", 
"birthday": "April 22, 2000"
}, 

{"id": 4, 
"first_name": "Juan", 
"last_name": "Dela Cruz", 
"birthday": "April 22, 2000"
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
		birthdays_today()
	elif menu_input == 3:
		pass
	elif menu_input == 4:
		pass
	elif menu_input == 5:
		exit()
	else:
		print('Invalid input')

def show_all():
	from datetime import datetime

	for item in db:
		birtdate = datetime.strptime(item['birthday'], '%B %d, %Y')
		age = calculate_age(birtdate)

		print(f'''

		ID: {item['id']}
		Full name: {item['first_name'] + ' ' + item['last_name']}
		Birthday: {item['birthday']}
		Age: {age}
			
			''')

	input('Press any key to continue...')

	main_menu()

def search_by_id(user_id):
	from datetime import datetime

	for item in db:
		birtdate = datetime.strptime(item['birthday'], '%B %d, %Y')
		age = calculate_age(birtdate)

		if user_id == item['id']:
			print(f'''

		ID: {item['id']}
		Full name: {item['first_name'] + ' ' + item['last_name']}
		Birthday: {item['birthday']}
		Age: {age}
			
			''')


def calculate_age(born):
	from datetime import date

	today = date.today()
	return today.year - born.year - ((today.month, today.day) < (born.month, born.day))


def birthdays_today():
	from datetime import datetime, date
	
	today = date.today()

	with_birthday = False

	for item in db:
		birtdate = datetime.strptime(item['birthday'], '%B %d, %Y')

		if (today.month, today.day) == (birtdate.month, birtdate.day):
			with_birthday = True
			search_by_id(item['id'])

	if with_birthday == False:
		print('No one has a birthday today.')

	input('Press any key to continue...')
	main_menu()

main_menu()






