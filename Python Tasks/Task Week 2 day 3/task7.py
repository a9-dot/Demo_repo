try: 
    age = int(input("Enter your age: ")) 
    assert age > 0, "Age must be a positive number." 
except AssertionError as e:     
    print(f"Error: {e}") 
except ValueError: 
    print("Error: Please enter a valid number.") 
else:     
    print(f"Your age is {age}.") 
