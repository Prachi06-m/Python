# policies = [
#     {"policy_id": "POL1001","customer": "Ravi","premium": 25000,"coverage": 1000000},
#     { "policy_id": "POL1002","customer": "Amit","premium": 40000,"coverage": 2000000},
#     { "policy_id": "POL1003","customer": "Sneha","premium": 15000,"coverage": 500000},
#     { "policy_id": "POL1004","customer": "Priya","premium": 60000,"coverage": 3000000}
# ]


# (map)
# discounted = list(
#     map(
#         lambda p: {
#             **p,
#             "discounted_premium": p["premium"] * 0.90
#         },
#         policies
#     )
# )

# print(discounted)


# (Filter)

# high_coverage = list(
#     filter(
#         lambda p: p["coverage"] > 1000000,
#         policies
#     )
# )

# print(high_coverage)









# import pandas as pd

# data = {
#     "PolicyID": ["POL1001","POL1002","POL1003","POL1004","POL1005" ],
#     "Customer": ["Ravi","Amit","Sneha","Priya","Rahul"],
#     "Product": ["Life Protection", "Child Future", "Life Protection", "Retirement","Child Future"],
#     "Premium": [25000,40000,15000,60000,30000],
#     "Coverage": [1000000,2000000,500000,3000000,1500000],
#     "Status": ["Active", "Active", "Inactive", "Active", "Active"]
# }

# df = pd.DataFrame(data)
# print(df)







# # (sorted)


# sorted_policies = sorted(
#     policies,
#     key=lambda p: p["premium"],
#     reverse=True
# )

# print(sorted_policies)


