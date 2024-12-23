print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, or 15?"))
people = int(input("How many people will wplit the bill?"))
bill_paid = (tip/100 * bill + bill) / people
final_amount = round(bill_paid, 2)
print(f"Each person should pay: ${final_amount}")