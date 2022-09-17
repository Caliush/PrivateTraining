import os
print("What do you want to do?\n")
print("1) Create a new file\n")
print("2) Delete a file\n")
print("3) Overwrite an existing file\n")
print("4) Write something to a file\n")
print("5) Exit the program \n")

x = int(input("Write the corresponding number: "))
print("\n")

if(x==1):
    name = input("Write the name of your file (including extension): ")
    print("\nWrite a new line in your file: \n")
    f = open(name, "w")
    f.write(input() + "\n")
    f.close()
elif(x==2):
    name = input("What is the name of the file you want to delete? (including extension)\n")
    os.remove(name)
elif(x==3):
    name = input("What is the name of the file you want to overwrite? (including extension)\n")
    f = open(name, "w")
    print("\nWrite a new line in your file: \n")
    f.write(input() + "\n")
    f.close()
elif(x==4):
    name = input("What is the name of the file you want to edit? (including extension) \n")
    f= open(name, "a")
    print("\nWrite a new line in your file: \n")
    f.write(input() + "\n")
    f.close()
elif(x==5):
    input("Press Enter to exit...")