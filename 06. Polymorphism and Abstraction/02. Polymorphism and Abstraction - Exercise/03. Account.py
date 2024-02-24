class Account:

    def __init__(self, owner: str, amount=0) -> None:
        self.owner = owner
        self.amount = amount
        self._transactions = []
        self.start_amount = amount

    def handle_transaction(self, transaction_amount):
        if transaction_amount + self.amount < 0:
            raise ValueError("sorry cannot go in debt!")

        self._transactions.append(transaction_amount)
        self.amount += transaction_amount

        return f"New balance: {self.amount}"

    def add_transaction(self, amount):
        if not isinstance(amount, int):
            raise ValueError("please use int for amount")

        if self.amount + amount < 0:
            raise ValueError("sorry cannot go in debt!")

        self._transactions.append(amount)
        self.amount += amount

        return f"New balance: {self.amount}"

    @property
    def balance(self):
        return self.amount

    def __len__(self) -> int:
        return len(self._transactions)

    def __str__(self) -> str:
        return f"Account of {self.owner} with starting amount: {self.amount}"

    def __repr__(self) -> str:
        return f"Account({self.owner}, {self.amount})"

    def __iter__(self):
        return iter(self._transactions)

    def __reversed__(self):
        return reversed(self._transactions)

    def __getitem__(self, item):
        return self._transactions[item]

    def __gt__(self, other) -> bool:
        return self.amount > other.amount

    def __ge__(self, other) -> bool:
        return self.amount >= other.amount

    def __lt__(self, other) -> bool:
        return self.amount < other.amount

    def __le__(self, other) -> bool:
        return self.amount <= other.amount

    def __eq__(self, other) -> bool:
        return self.amount == other.amount

    def __ne__(self, other) -> bool:
        return self.amount != other.amount

    def __add__(self, other):
        new_owner = f"{self.owner}&{other.owner}"
        new_amount = self.amount + other.amount
        new_acc = Account(new_owner, new_amount)
        new_acc._transactions = self._transactions + other._transactions

        return new_acc


acc = Account('bob', 10)
acc2 = Account('john')
print(acc)
print(repr(acc))
acc.add_transaction(20)
acc.add_transaction(-20)
acc.add_transaction(30)
print(acc.balance)
print(len(acc))
for transaction in acc:
    print(transaction)
print(acc[1])
print(list(reversed(acc)))
acc2.add_transaction(10)
acc2.add_transaction(60)
print(acc > acc2)
print(acc >= acc2)
print(acc < acc2)
print(acc <= acc2)
print(acc == acc2)
print(acc != acc2)
acc3 = acc + acc2
print(acc3)
print(acc3._transactions)
acc1 = Account("Johhny")
acc2 = Account("Anna", 40)
acc2.add_transaction(-20)
print(acc2.balance)
# self.assertEqual(self.acc2.balance, 20)
