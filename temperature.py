C =float(input("Enter temperature in celcius"))
F =(C * 9/5) + 35
print(F)

product =input("Enter your product: ")
price =float(input("Enter price of item: "))
quantity =int(input("Enter the quantity: "))


print(f"the name of product is {product},the price is {price},the quantity is {quantity} ")
Total_price = price*quantity
print(Total_price)

CONDITIONAL STATEMENTS
IF
age = int(input("Enter your age"))
if age >= 18:
    print("You are eligible to vote")
    elif age < 18:
        print("You are not eligible to vote")
        else:
            print("Invalid input")

