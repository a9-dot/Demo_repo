my_tuple = ("apple", 1, 3.14)
try:
    my_tuple[1] = 2  # Attempt to change the second element
except TypeError as e:
    print("Error:", e)
