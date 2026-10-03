def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    if num2 == 0:
        return "Error Division by Zero is not allowed"
    return num1 / num2

firstnumber = float(input("Enter first number: "))
Secondnumber = float(input("Enter second number: "))
print('choose an operation:')
print('1. add')
print('2. subtract')
print('3. multiply')
print('4. divide')
operation = input("Enter your choice (1/2/3/4): ")

if operation == '1':
    result = add(firstnumber, Secondnumber)
    print("Result is: ", result)
elif operation == '2':
    result = subtract(firstnumber, Secondnumber)
    print("Result is: ", result)
elif operation == '3':
    result = multiply(firstnumber, Secondnumber)
    print("Result is: ", result)
elif operation == '4':
    result = divide(firstnumber, Secondnumber)
    print("Result is: ", result)
else:
    print("Invalid operation")
