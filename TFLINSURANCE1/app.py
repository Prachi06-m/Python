# import json

# # Read JSON file
# with open("policies.json", "r") as file:
#     policies = json.load(file)

# # Display policies
# print(policies)



# import json 
# with  open("policies.json","r")as f:
#     policies=json.load(f)
# print(policies)



import pandas as pd

df = pd.read_csv("policies.csv")

print(df.head())






# high_coverage = df[
#     df["Coverage"].apply(
#         lambda coverage: coverage > 1000000
#     )
# ]

# print(high_coverage)



           
