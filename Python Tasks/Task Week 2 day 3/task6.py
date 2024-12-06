class InvalidAgeError(Exception): 
    pass  
try:
    age = int(input("Please enter your age: "))     
    if age < 0 or age > 120: 
        raise InvalidAgeError("Age must be between 0 and 120.") 
except InvalidAgeError as e:     
    print(f"Error: {e}") 
except ValueError: 
    print("Error: Please enter a valid number.") 
else:     
    print(f"Your age is {age}.") 