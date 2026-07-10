ethiopian_cities = ["Addis Ababa", "Adama"]
kenyan_cities = ["Nairobi", "Mombasa"]
all_cities = ethiopian_cities + kenyan_cities
# Result: ["Addis Ababa", "Adama", "Nairobi", "Mombasa"]
print ( all_cities )
print("Adama" in all_cities)  
print("Harar" in all_cities)  
coordinates = (9.03, 38.74)
print(coordinates[0])  
totals = [] 
for price in [100, 250, 400]: 
    totals.append(price * 1.15)   # add 15% tax 
# totals -> [115.0, 287.5, 460.0]
print(totals)
coordinates = (9.03, 38.74)
print(coordinates[0])  # 9.03
location = (9.0192, 38.7525)    # Addis Ababa coordinates
lat, lon = location             # unpacking into two variables
print(lat)  # 9.0192
print(lon)  # 38.7525
# location[0] = .0               # TypeError — tuples can't change
customer = { 
    "name": "Almaz Bekele", 
    "balance": 1500,        # ETB 
    "city": "Addis Ababa", 
} 
  
print(customer["name"])              # "Almaz Bekele" 
print(customer["balance"])           # 1500
customer["balance"] = 2000   # update a value 
print(customer["balance"])           # 2000
customer.get("phone", "N/A") # safe access, no KeyError
print(customer.get("phone", "N/A"))  # "N/A"

prices = {"Bread": 50, "Milk": 80, "Eggs": 120}   # ETB 
  
for item, price in prices.items(): 
    print(f"{item}: {price} ETB") 
  
print(prices.keys())      # the item names 
print(prices.values())    # the prices 
print("Milk" in prices)   # True — membership test on keys
print ( 1200.8 + 300)
a=10
b=46
float(a)
print(float(a+b))
print ( 1%10)
balance = 10 
#while balance >= 0:
  #  balance - 1
   # print (f" i have {balance} remaning")
for i in range (10):
    print (i)

def add_tax(price, rate=0.15): 
    return price + price * rate 
total = add_tax(1000)    
total = 100
number_of_people = 5 
def split_the_bill(total, number_of_people, tip_rate=0.01):
    total_with_tip = total + (total * tip_rate) 
    return total_with_tip / number_of_people
for i in range(5):
    print(split_the_bill(total, number_of_people))