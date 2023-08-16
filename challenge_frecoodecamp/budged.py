class Category:

    def __init__(self, category):
        self.category = category
        self.ledger = []

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        return False

    def get_balance(self):
        return sum(item["amount"] for item in self.ledger)

    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {category.category}")
            category.deposit(amount, f"Transfer from {self.category}")
            return True
        return False

    def check_funds(self, amount):
        return self.get_balance() >= amount

    def __str__(self):
        output = self.category.center(30, "*") + "\n"
        for item in self.ledger:
            desc = item["description"][:23]
            amt = f"{item['amount']:.2f}".rjust(30 - len(desc))
            output += f"{desc}{amt}\n"
        output += f"Total: {self.get_balance():.2f}"
        return output


def create_spend_chart(categories):
    spent_percentages = [(sum(item["amount"] for item in category.ledger if item["amount"] < 0) / category.get_balance()) * 100 for category in categories]

    graph = "Percentage spent by category\n"
    for i in range(100, -1, -10):
        graph += str(i).rjust(3) + "| "
        for percent in spent_percentages:
            if percent >= i:
                graph += "o  "
            else:
                graph += "   "
        graph += "\n"

    graph += "    -" + "---" * len(categories) + "\n"

    max_len = max(len(category.category) for category in categories)
    for i in range(max_len):
        graph += "     "
        for category in categories:
            if i < len(category.category):
                graph += category.category[i] + "  "
            else:
                graph += "   "
        graph += "\n"

    return graph
