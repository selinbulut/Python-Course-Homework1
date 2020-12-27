
user = []

first_name = input("Please enter a first name: ")
user.append(first_name)
last_name =  input("Please enter a last name: ")
user.append(last_name)
age = int( input("Please enter a age: "))
user.append(age)
date_of_birth =int( input("Please enter a date of birth(just year): "))
user.append(date_of_birth)
print(user) 
if age <18 :
  print("You can't go out because its too dangerous")
else:
    print("You can go out to the street")