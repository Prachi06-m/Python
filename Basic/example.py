#TAKE INPUT FROM USER(REGISTRATION PAGE)
 
 
# name = input("Enter customer name: ")
# age = int(input("Enter age: "))
# premium = float(input("Enter premium: "))

# print("Customer:", name)
# print("Age:", age)
# print("Premium:", premium)







#(INDENTATION)
premium = 25000

if premium > 20000:
    print("High premium policy")

print("Policy processing completed")






#(Logic)
# sum_assured = 1000000
# rate = 0.025

# premium = sum_assured * rate

# print("Premium:", premium))







# (CONTROL STRUCTURE)
# age = int(input("Enter your age: "))

# if age >= 18:
#     print("You are eligible to vote.")






# marks = int(input("Enter Marks: "))

# if marks >= 40:
#     print("Congratulations! You Passed.")
# else:
#     print("Better Luck Next Time.")










# marks = int(input("Enter Marks: "))

# if marks >= 75:
#     print("Distinction")
# elif marks >= 60:
#     print("First Class")
# elif marks >= 40:
#     print("Pass")
# else:
#     print("Fail")





#(Loops)
# for i in range(5):
#     print("Welcome to Transflower")



# (multiplication table)
# number = int(input("Enter Number: "))

# for i in range(1,11):
#     print(number,"x",i,"=",number*i)





# count = 1

# while count <= 5:
#     print(count)
#     count += 3





# for i in range(1,6):
#     if i % 2 == 0:
#         print(i,"is Even")
#     else:
#         print(i,"is Odd")






# for number in range(2,21,2):
#     print(number)










# count = 10

# while count > 0:
#     print(count)
#     count -= 1

# print("Launch!")














# import random

# secret_number = random.randint(1, 100)
# attempts = 0

# print("=== Number Guessing Game ===")
# print("I have selected a number between 1 and 100.")

# while True:
#     guess = int(input("Enter your guess: "))
#     attempts += 1

#     if guess < secret_number:
#         print("Too Low! Try Again.")
#     elif guess > secret_number:
#         print("Too High! Try Again.")
#     else:
#         print("🎉 Congratulations!")
#         print("You guessed the correct number.")
#         print("Attempts:", attempts)
#         break



    #print("Secret number:", secret_number)



















# choice = 2

# match choice:
#     case 1:
#         print("Add Customer")

#     case 2:
#         print("Update Customer")

#     case 3:
#         print("Delete Customer")

#     case 4:
#         print("Exit")

#     case _:
#         print("Invalid choice")





# day = 4

# match day:
#     case 1 | 2 | 3 | 4 | 5:
#         print("Weekday")

#     case 6 | 7:
#         print("Weekend")

#     case _:
#         print("Invalid day")









# role = "admin"

# match role:
#     case "admin":
#         print("Full access")

#     case "manager":
#         print("Management access")

#     case "developer":
#         print("Development access")

#     case "tester":
#         print("Testing access")

#     case _:
#         print("Unknown role")





















# def add():
#     print("Adding customer")


# def update():
#     print("Updating customer")


# def delete():
#     print("Deleting customer")

# #dictionary data type
# actions = {
#     1: add,
#     2: update,
#     3: delete
# }

# choice = 1

# action = actions.get(choice)

# if action:
#     action()
# else:
#     print("Invalid choice")












# command = ["add", "Ravi"]#List

# match command:
#     case ["add", name]:
#         print(f"Adding customer: {name}")

#     case ["delete", name]:
#         print(f"Deleting customer: {name}")

#     case ["update", name]:
#         print(f"Updating customer: {name}")

#     case _:
#         print("Unknown command")





