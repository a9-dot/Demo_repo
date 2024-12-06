try:     
    with open("source.txt", "r") as src_file: 
        data = src_file.read() 
    with open("destination.txt", "w") as dest_file: 
        dest_file.write(data) 
except FileNotFoundError: 
    print("Error: The source file does not exist.")
except IOError: 
    print("Error: There was an issue with file writing.") 
finally: 
    print("File operations completed.") 
