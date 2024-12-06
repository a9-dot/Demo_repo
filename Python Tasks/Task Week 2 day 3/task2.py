
try:
    age = int(input("Please enter your age: ")) 
except ValueError: 
    print("Invalid input. Please enter a valid number.") 
else:     
    print(f"Your age is {age}.") 
