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
	try:
		menu_input = int(input("Enter menu item: "))
	except ValueError:
		main_menu()

	if menu_input == 1:
		show_all()
	elif menu_input == 2:
		birthdays_today()
	elif menu_input == 3:
		add_item()
	elif menu_input == 4:
		delete_item()
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
			return f'''

		ID: {item['id']}
		Full name: {item['first_name'] + ' ' + item['last_name']}
		Birthday: {item['birthday']}
		Age: {age}
			
			'''
			

	return None


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
			print(search_by_id(item['id']))

	if with_birthday == False:
		print('No one has a birthday today.')

	input('Press any key to continue...')
	main_menu()

def add_item():
	confirm_input = ''
	while confirm_input.upper() != 'Y':
		valid_id = False
		while valid_id == False:
			try:
				input_id = int(input('Enter valid id (whole number(s) only): '))
				valid_id = True
			except ValueError:
				continue

		is_taken = check_id(input_id)
		while is_taken:
			try:
				input_id = int(input('The ID is already taken. Please try again: '))
			except ValueError:
				continue
			is_taken = check_id(input_id)

		input_first_name = input('Enter first name: ').strip()
		input_last_name = input('Enter last name: ').strip()
		input_birthday = input('Enter birthday: ')
		is_invalid_birthday = check_birthday(input_birthday.capitalize())
		while is_invalid_birthday:
			input_birthday = input('Enter valid Birthday (e.g. August 10, 1999): ')
			is_invalid_birthday = check_birthday(input_birthday.capitalize())

		confirm_input = input(f''' 

    		Check if your inputs are correct:
    		ID: {input_id}
    		Full name: {input_first_name.capitalize()} {input_last_name.capitalize()}
    		Birthday: {input_birthday.capitalize()}

    		(Y/N): ''')

		if confirm_input.upper() == 'Y':
			db.insert(len(db), 
					{
					'id': input_id, 
					'first_name': input_first_name.capitalize(), 
					'last_name': input_last_name.capitalize(),
					'birthday': input_birthday
					 })
			input('Record added. Press any key to continue...')
			main_menu()

def check_id(id):
	for item in db:
		if item['id'] == id:
			return True
	return False 

def check_birthday(birthday):
	from datetime import datetime
	try:
		if birthday != datetime.strptime(birthday, '%B %d, %Y').strftime('%B %d, %Y'):
			raise ValueError
		return False
	except ValueError:
		return True

def delete_item():
	input_id = int(input('Enter ID of the record you want to delete: '))
	
	record = search_by_id(input_id)
	if record is None:
		print('Record doesn\'t exist.')
	else:
		input_response = input(f'Continue deleting {record} (Y/N) ')
		if input_response.upper() == 'Y':
			i = 0
			for item in db:
				if item['id'] == input_id:
					del db[i]
					print('Record deleted.\n')
				i += 1
		else:
			print('Nothing deleted.')

	input('Press any key to continue...')
	main_menu()

main_menu()






