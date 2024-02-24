from typing import List
from project.clients.base_client import BaseClient
from project.clients.student import Student
from project.clients.adult import Adult
from project.loans.base_loan import BaseLoan
from project.loans.student_loan import StudentLoan
from project.loans.mortgage_loan import MortgageLoan


class BankApp:
    VALID_LOANS = ["StudentLoan", "MortgageLoan"]
    VALID_CLIENTS = ["Student", "Adult"]

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.loans: List[BaseLoan] = []
        self.clients: List[BaseClient] = []

    def add_loan(self, loan_type: str):
        if loan_type not in self.VALID_LOANS:
            raise Exception("Invalid loan type!")

        new_loan = globals()[loan_type]()
        self.loans.append(new_loan)

        return f"{loan_type} was successfully added."

    def add_client(self, client_type: str, client_name: str, client_id: str, income: float):
        if client_type not in self.VALID_CLIENTS:
            raise Exception("Invalid client type!")

        if len(self.clients) == self.capacity:
            return "Not enough bank capacity."

        new_client = globals()[client_type](client_name, client_id, income)
        self.clients.append(new_client)

        return f"{client_type} was successfully added."

    def grant_loan(self, loan_type: str, client_id: str):
        loan = next(l for l in self.loans if l.__class__.__name__ == loan_type)
        client = next(c for c in self.clients if c.client_id == client_id)
        loan_types = {"StudentLoan": "Student", "MortgageLoan": "Adult"}
        if loan_types[loan_type] != client.__class__.__name__:
            raise Exception("Inappropriate loan type!")

        client.loans.append(loan)
        self.loans.remove(loan)

        return f"Successfully granted {loan_type} to {client.name} with ID {client_id}."

    def remove_client(self, client_id: str):
        client = next((c for c in self.clients if c.client_id == client_id), None)
        if not client:
            raise Exception("No such client!")

        if client.loans:
            raise Exception("The client has loans! Removal is impossible!")

        self.clients.remove(client)

        return f"Successfully removed {client.name} with ID {client_id}."

    def increase_loan_interest(self, loan_type: str):
        loan_list = list(filter(lambda x: x.__class__.__name__ == loan_type, self.loans))
        [loan.increase_interest_rate() for loan in loan_list]

        return f"Successfully changed {len(loan_list)} loans."

    def increase_clients_interest(self, min_rate: float):
        clients_list = list(filter(lambda x: x.interest < min_rate, self.clients))
        [client.increase_clients_interest() for client in clients_list]

        return f"Number of clients affected: {len(clients_list)}."

    def get_statistics(self):
        total_income2 = sum(c.income for c in self.clients)
        total_income = 0
        granted_loans = 0
        total_sum = 0
        all_rates = []
        for c in self.clients:
            total_income += c.income
            granted_loans += len(c.loans)
            all_rates.append(c.interest)
            for l in c.loans:
                total_sum += l.amount

        not_granted = 0
        for l in self.loans:
            not_granted += l.amount

        avg_rate = sum(all_rates) / len(all_rates) if self.clients else 0

        res = f"Active Clients: {len(self.clients)}" \
              f"\nTotal Income: {total_income:.2f}" \
              f"\nGranted Loans: {granted_loans}, Total Sum: {total_sum:.2f}" \
              f"\nAvailable Loans: {len(self.loans)}, Total Sum: {not_granted:.2f}" \
              f"\nAverage Client Interest Rate: {avg_rate:.2f}"

        return res