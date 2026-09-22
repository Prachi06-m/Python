
from customer.customer import Customer
from policy.models import Policy
from policy.service import PolicyService
from policy.repository import PolicyRepository




# Customer
customer = Customer("CUS101", "Prachi")

customer.display()



# Policy
policy = Policy(
    "POL1001",
    "CUS101",
    "Life Insurance",
    25000
)

policy.display()





# Policy Service
policy_service = PolicyService()

premium = policy_service.calculate_premium(policy)

print("Policy Premium:", premium)



# Repository
repository = PolicyRepository()

repository.get_policy("POL1001")







