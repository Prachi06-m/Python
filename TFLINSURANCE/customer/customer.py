class Customer:

    def __init__(self, customer_id, name):
        self.customer_id = customer_id
        self.name = name

    def display(self):
        print("Customer ID:", self.customer_id)
        print("Customer Name:", self.name)
        































































#     from customer.customer import Customer
# from policy.models import Policy
# from policy.service import PolicyService
# from policy.repository import PolicyRepository
# from premium.calculator import calculate_total
# from premium.service import PremiumService


# # Customer
# customer = Customer("CUS101", "Prachi")

# customer.display()


# # Policy
# policy = Policy(
#     "POL1001",
#     "CUS101",
#     "Life Insurance",
#     25000
# )

# policy.display()


# # Policy Service
# policy_service = PolicyService()

# premium = policy_service.calculate_premium(policy)

# print("Policy Premium:", premium)


# # Check policy active
# print("Policy Active:", policy_service.is_active(policy))


# # Repository
# repository = PolicyRepository()

# repository.get_policy("POL1001")


# # Premium Service
# premium_service = PremiumService()

# due = premium_service.calculate_due(25000)

# print("Premium Due:", due)


# # Calculator
# total = calculate_total(25000)

# print("Total Premium:", total)