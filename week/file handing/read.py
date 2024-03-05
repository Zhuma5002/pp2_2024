f=open("demofile.txt","r")
print(f.read())

#"r" - Read - Default value. Opens a file for reading, error if the file does not exist
#"a" - Append - Opens a file for appending, creates the file if it does not exist
#"w" - Write - Opens a file for writing, creates the file if it does not exist
#"x" - Create - Creates the specified file, returns an error if the file exists
f=open("demofile.txt","r")
print(f.read(6))


f=open("demofile.txt","r")
print(f.readline())
print(f.readline())
