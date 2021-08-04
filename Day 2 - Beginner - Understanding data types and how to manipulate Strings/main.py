#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪
#HINT 1: https://www.google.com/search?q=how+to+round+number+to+2+decimal+places+python&oq=how+to+round+number+to+2+decimal
#HINT 2: https://www.kite.com/python/answers/how-to-limit-a-float-to-two-decimal-places-in-python
print("Welcome to the tip calculator.")
bill = float(input("What was the total of the bill?\n"))
tip_percentage = float(input("What percentage tip would you like to give? 10, 12 or 15%?\n"))
number_people = int(input("How many people to split the bill?\n"))

total_bill_with_tip = bill + bill / 100 * tip_percentage

#Alternative rounding method to always show 2 number (e.g $33.60 instead of $33.6)
bill_per_people = format(total_bill_with_tip / number_people, '.2f')
print(f"Each people should pay: ${bill_per_people}")

#Alternative rounding method but not showing 2 number (e.g $33.6 instead of $33.60)
#bill_per_people = round(total_bill_with_tip / number_people,2 )
#print(f"Each people should pay: ${bill_per_people}")

"""Solution from Angela:
print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill?"))

tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people
final_amount = round(bill_per_person, 2)

#FAQ: How to round to 2 decimal places?
#https://www.udemy.com/course/100-days-of-code/learn/lecture/17965132#questions/13315048

print(f"Each person should pay: ${final_amount}")
"""