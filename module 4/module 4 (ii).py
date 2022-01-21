Mydict = {}

elements = int(input("Enter the number of elements to store:"))

for i in range(elements):
    name = str(input("Enter the name:"))
    rollno = int(input("Enter the Roll No:"))
    Mydict.update({name: rollno})

print(Mydict)
