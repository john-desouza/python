print("Welcome to the tip calculator.")
initialBill = float(input("What's the total bill? "))
numberOfPeople = float(input("How many people are splitting the bill? "))
tipPercentage = float(input("What percentage tip would you like to give? "))

# Calculate the impact the percentage given will have on the bill
maximumTip = 100
tipAmmount = (tipPercentage / maximumTip) * 100

#Calculate the final ammount considering all previous values provided
finalBill = (tipAmmount + initialBill) / numberOfPeople

print(f"Each person should pay {finalBill}")
