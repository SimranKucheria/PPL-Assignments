try:
    file = open("Assignment.txt","r")
    for line in file:
        print(line)
except:
    print("File Doesn't exist")
