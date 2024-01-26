#Calculate the product and sum of two numbers
#Using if else statement
#Show the product if it is equal or greater than 1000, else show the sum

def calculate(x, y):

    product = x * y
    if product <= 1000:
        return product
    else: 
        return x + y
    
#Print the result
num1 = 10
num2 = 60
result = calculate(num1, num2)
print(f"The result is: {result}")