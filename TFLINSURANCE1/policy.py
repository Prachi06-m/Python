

import json

with open("policies.json", "r") as file:
    policies = json.load(file)

new_policy = {
    "policy_number": "POL1005",
    "customer_name": "sakshiii",
    "premium": 18000,
    "status": "Active"
}

policies.append(new_policy)



with open("policies.json", "w") as file:
    json.dump(policies, file, indent=4)






import json
def find_policy(policy_number):

    with open("policies.json", "r") as file:
        policies = json.load(file)

    for policy in policies:

        if policy["policy_number"] == policy_number:
            return policy

    return None


policy = find_policy("POL1001")

print(policy)















import json

try:
    with open("policies.json", "r") as file:
        policies = json.load(file)

    print("Policies loaded successfully.")
    print(policies)

except FileNotFoundError:
    print("Policy file does not exist.")
    policies = []

print("Policies:", policies)


















import json

try:
    with open("policies.json", "r") as file:
        policies = json.load(file)

    print("Policies loaded successfully.")
    print(policies)

except FileNotFoundError:

    print("Policy file not found.")
    policies = []

except json.JSONDecodeError:

    print("Policy file contains invalid JSON.")
    policies = []

print("Policies:", policies)

































