f=open("demofile.txt","a")
f.write("yeah baby!")
f.close()

f=open("demofile.txt","r")
print(f.read())

f = open("demofile.txt", "w")
f.write("Woops! I have deleted the content!")
f.close()

f = open("demofile.txt", "r")
print(f.read())
