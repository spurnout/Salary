def money():
	current_salary = float(input("What is your current salary? "))
	
	while True:
		try:
			years = int(input("How many years would you like to look ahead? "))
			break
		except ValueError:
			print("That is not a full number.  Please try again.")
	
	amount_of_raise = float(input("What is the average percentage raise you think you will get? ")) * 0.01
	for years in range(1, years + 1):
		current_salary += current_salary * amount_of_raise
		print('Looks like you will be making', current_salary,' in ', years,'years.')

money()