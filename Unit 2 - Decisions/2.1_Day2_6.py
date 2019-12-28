#Name: Yash Raja
#Date: September 22nd, 2017
#File Name: 2.1Day2_6.py
#Descrpition: Asks user for item, for its price, and if overnight shipping is
#wanted, adds 5 to shipping if overnight shipping. If product is more than
#$10 then $3.00 regular shipping and if under $10 then $2.00 shipping
#Test Cases: Tuna Salad and 4.50 and 1

print("Enter the item: ")
item = input("")
print("Enter the price: ")
price = float(input(""))
print("Overnight delivery (0==no, 1==yes)")
delivery = int(input(""))

if delivery == 0:
    if price < 10:
        shipping = 2.00
    elif price >= 10:
        shipping = 3.00
if delivery == 1:
    if price < 10:
        shipping = 7.00
    elif price >= 10:
        shipping = 8.00
total = price + shipping

print("Invoice")
print("          ", item, "=", price)
print("           Shipping", "=", shipping)
print("           Total", "=", total)
