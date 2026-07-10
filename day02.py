total = int(input("Enter the total bill amount: "))
number_of_people = int(input("Enter the number of people: "))
def split_the_bill(total, number_of_people, tip_rate=0.1):
    total_with_tip = total + (total * tip_rate) 
    return total_with_tip / number_of_people
print(split_the_bill(total, number_of_people))

