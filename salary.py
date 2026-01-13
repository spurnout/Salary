def prompt_float(prompt: str) -> float:
	while True:
		try:
			return float(input(prompt))
		except ValueError:
			print("Please enter a number.")


def prompt_int(prompt: str) -> int:
	while True:
		try:
			return int(input(prompt))
		except ValueError:
			print("Please enter a whole number.")


def forecast_salary(current_salary: float, years: int, raise_rate: float) -> None:
	for year in range(1, years + 1):
		current_salary += current_salary * raise_rate
		print(f"Looks like you will be making {current_salary:,.2f} in {year} years.")


def main() -> None:
	current_salary = prompt_float("What is your current salary? ")
	years = prompt_int("How many years would you like to look ahead? ")
	raise_rate = prompt_float(
		"What is the average percentage raise you think you will get? "
	) * 0.01
	forecast_salary(current_salary, years, raise_rate)


if __name__ == "__main__":
	main()
