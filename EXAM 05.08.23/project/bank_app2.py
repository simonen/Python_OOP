from typing import List
from project.clients.base_client import BaseClient
from project.clients.student import Student
from project.clients.adult import Adult
from project.loans.base_loan import BaseLoan
from project.loans.student_loan import StudentLoan
from project.loans.mortgage_loan import MortgageLoan


class BankApp:

    VALID_LOANS_CLIENTS = {"StudentLoan": "Student", "MortgageLoan": "Adult"}

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.loans: List[BaseLoan] = []
        self.clients: List[BaseClient] = []
        self.granted_loans: List[BaseLoan] = []

    def add_loan(self, loan_type: str) -> str or None:
        if loan_type not in self.VALID_LOANS_CLIENTS:
            raise Exception("Invalid loan type!")

        new_loan = globals()[loan_type]()
        self.loans.append(new_loan)

        return f"{loan_type} was successfully added."

    def add_client(self, client_type: str, client_name: str, client_id: str, income: float) -> str or None:
        if client_type not in self.VALID_LOANS_CLIENTS.values():
            raise Exception("Invalid client type!")

        if len(self.clients) == self.capacity:
            return "Not enough bank capacity."

        new_client = globals()[client_type](client_name, client_id, income)
        self.clients.append(new_client)

        return f"{client_type} was successfully added."

    def grant_loan(self, loan_type: str, client_id: str) -> str or None:
        loan = next(l for l in self.loans if l.__class__.__name__ == loan_type)
        client = next(c for c in self.clients if c.client_id == client_id)

        if self.VALID_LOANS_CLIENTS[loan_type] != client.__class__.__name__:
            raise Exception("Inappropriate loan type!")

        client.loans.append(loan)
        self.granted_loans.append(loan)
        self.loans.remove(loan)

        return f"Successfully granted {loan_type} to {client.name} with ID {client_id}."

    def remove_client(self, client_id: str) -> str or None:
        client = next((c for c in self.clients if c.client_id == client_id), None)
        if not client:
            raise Exception("No such client!")

        if client.loans:
            raise Exception("The client has loans! Removal is impossible!")

        self.clients.remove(client)

        return f"Successfully removed {client.name} with ID {client_id}."

    def increase_loan_interest(self, loan_type: str) -> str:
        loan_list = list(filter(lambda x: x.__class__.__name__ == loan_type, self.loans))
        [loan.increase_interest_rate() for loan in loan_list]

        return f"Successfully changed {len(loan_list)} loans."

    def increase_clients_interest(self, min_rate: float) -> str:
        clients_list = list(filter(lambda x: x.interest < min_rate, self.clients))
        [client.increase_clients_interest() for client in clients_list]

        return f"Number of clients affected: {len(clients_list)}."

    def get_statistics(self) -> str:
        total_income = sum(c.income for c in self.clients)
        total_sum = sum([l.amount for l in self.granted_loans])
        all_rates = [c.interest for c in self.clients]
        not_granted = sum([l.amount for l in self.loans])
        avg_rate = sum(all_rates) / len(all_rates) if self.clients else 0

        res = f"Active Clients: {len(self.clients)}" \
              f"\nTotal Income: {total_income:.2f}" \
              f"\nGranted Loans: {len(self.granted_loans)}, Total Sum: {total_sum:.2f}" \
              f"\nAvailable Loans: {len(self.loans)}, Total Sum: {not_granted:.2f}" \
              f"\nAverage Client Interest Rate: {avg_rate:.2f}"

        return res
