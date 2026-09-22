
# (properties /methods same as parent class)
class Employee:

    def __init__(self, employee_id, name):
        self.employee_id = employee_id
        self.name = name

    def display(self):
        print("Employee ID:", self.employee_id)
        print("Name:", self.name)


class Agent(Employee):

    def sell_policy(self):
        print("Selling insurance policy")


class ClaimsOfficer(Employee):

    def process_claim(self):
        print("Processing claim")


# Agent object
agent = Agent(101, "Rahul")

agent.display()
agent.sell_policy()


print()


# Claims Officer object
officer = ClaimsOfficer(102, "Prachi")

officer.display()
officer.process_claim()