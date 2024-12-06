n= int(input("Enter the number of elemnts that u want to enter in the list:"))
ls=[]
for i in range(n):
    x= int(input("Enter the number {} :".format(i)))
    ls.append(x)

print("Traversing through the list using the for loop as mentioned in the problm -----")
for i in range(len(ls)):
    print(ls[i])