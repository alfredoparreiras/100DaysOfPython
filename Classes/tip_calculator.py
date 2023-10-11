print("Welcome to the tip calculator.")
total_bill = input("What was the total bill? $")
percentage_tip = input("What percentage tip would you like to give? 10, 12, or 15?")
number_of_people = input("How many people to slipt the bill?")
percentage = float(percentage_tip) / 100
total = float(total_bill)
people = int(number_of_people)
each_person = (total + (total * percentage)) / people

print(f"Each person should pay ${round(each_person,2)}")