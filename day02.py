# 1)write a python small python program that splits a Restaurant  bill with in a group of people 
total = int(input("Enter the bill amount: "))
number_of_people = int(input("Enter the number of people: "))
def split_the_bill(total, number_of_people, tip_rate=0.1):
    total_with_tip = total + (total * tip_rate) 
    return total_with_tip / number_of_people
print(split_the_bill(total, number_of_people))
#2) write a small python program that splits a restaurant bill with a tip rate=0.1 across friends 
#using variables, operators, a function and  a loop.
total = int(input("Enter the bill amount: "))
number_of_people = int(input("Enter the number of people: "))
def split_the_bill(total, number_of_people, tip_rate=0.1):
    total_with_tip = total + (total * tip_rate) 
    return total_with_tip / number_of_people
for i in range(number_of_people):
    print(f"the total bill is {split_the_bill(total, number_of_people)}")


