# class Claim:
#     def __init__(self, claimname,amount):
#         self.claimname=claimname
#         self.__amount = amount

# c1=Claim("insurance",1000)

# print(c1.claimname)
# print(c1.__amount)



# (data hide cannot access without method)
class Claim:
     def __init__(self, claimname, amount):
         self.claimname = claimname
         self.__amount = amount

     def get_amount(self):
         return self.__amount


c1 = Claim("insurance", 1000)

print(c1.claimname)
print(c1.get_amount()) #(method access)



class Person:
  def __init__(self, name, age):
    self.name = name
    self.__age = age # Private property

p1 = Person("Emil", 25)
print(p1.name)
print(p1.__age) # This will cause an error






