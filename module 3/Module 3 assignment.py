
#Defining list

Personel_Details = list()

#Getting the inputs

Name = str(input("Please enter your name:"))
Reg_No = int(input("Please enter your registration number:"))
Gender = str(input("Please enter your gender:"))
Age = int(input("Please enter your age:"))
Percentage = float(input("Please enter your percentage:"))

#Adding the inputs into the list

Personel_Details.append(Name)
Personel_Details.append(Reg_No)
Personel_Details.append(Gender)
Personel_Details.append(Age)
Personel_Details.append(Percentage)

#Printing the list

print(Personel_Details)

#Printing list with 'f' string

print("Please verify the details you have provided")

print(f'Your Name is {Name} \nYour Registration number is {Reg_No} \nYour Gender is {Gender} \nYour Age is {Age}years \nYour Percentage is {Percentage}%')


