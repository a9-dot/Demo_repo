try: 
    file = open("output.txt", "w")     
    file.write("Hello, world!") 
except IOError:
    print("Error: Unable to write to file.") 
finally: 
    file.close()     
    print("File closed.") 