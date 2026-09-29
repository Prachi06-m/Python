import pandas as pd

# df = pd.read_csv("policies.csv")

# print(df.head())





# df = pd.read_csv("policies.csv")

# high_coverage = df[
#     df["Coverage"].apply(
#         lambda coverage: coverage > 1000000
#     )
# ]

# print(high_coverage)




# df = pd.read_csv("policies.csv")
# df["DiscountedPremium"] = df["Premium"].apply(
#     lambda premium: premium * 0.90
# )

# print(df)





df = pd.read_csv("policies.csv")
# df["PremiumCategory"] = df["Premium"].apply(
#     lambda premium: "High"
#     if premium >= 50000
#     else "Normal"
# )

# print(df)






# df = pd.read_csv("policies.csv")
# sorted_policies = df.sort_values(
#     by="Premium",
#     ascending=False
# )

# print(sorted_policies)




# avg_premium = (
#     df.groupby("Product")["Premium"]
#       .apply(lambda x: x.mean())
# )

# print(avg_premium)







# active_policies = df[
#     df["Status"].apply(
#         lambda status: status == "Active"
#     )
# ]

# print(active_policies)