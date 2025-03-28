import os

if os.path.exists("index.txt"):
    os.remove("index.txt")
    
    print("File exists")
else:
    print("File does not exist")

    


