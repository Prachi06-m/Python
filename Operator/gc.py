# import gc


# class Customer:
#     pass


# class InsurancePolicy:
#     pass


# customer = Customer()
# policy = InsurancePolicy()

# customer.policy = policy
# policy.customer = customer

# print("Objects created")

# del customer
# del policy

# print("References deleted")

# collected = gc.collect()

# print("Garbage collected:", collected)






# import gc

# print(gc.get_threshold())

# print(gc.get_count())




import gc

# Enable automatic cyclic garbage collection
gc.enable()

print("Garbage Collector enabled:", gc.isenabled())
