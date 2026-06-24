from functools import total_ordering

print("Wellcome to the tip calculator!!")
bill = float(input("What was the total bill ? "))
tip = int(input("How much tip would you like to give ?"))
tip_percent = tip/100
people = int(input("How many people to split the bill"))
tip_bill = (bill * tip_percent )
total_bill =  (bill + tip_bill)/people
print(f"Each Person Have to pay : {total_bill}")