# try:
#     premium = int(input("Enter premium amount: "))
#     print("Premium:", premium)

# except:
#     print("Invalid premium amount.")





try:

    age = int(input("Enter age: "))

except ValueError:
    print("Age must be a number.")

except TypeError:
    print("Invalid data type.")

    