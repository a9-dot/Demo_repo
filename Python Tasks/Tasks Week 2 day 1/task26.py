#lambda fun
square = lambda x: x**2

#Use Lambda Function with map():


numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(square, numbers))
