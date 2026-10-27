from project.clients.base_client import BaseClient
from project.loans.base_loan import BaseLoan
from project.loans.mortgage_loan import MortgageLoan
from project.loans.student_loan import StudentLoan
from project.clients.student import Student
from project.clients.adult import Adult


class BankApp:
    _LOAN_TYPES = {"StudentLoan": StudentLoan, "MortgageLoan": MortgageLoan}
    _LOAN_CLIENT = {"StudentLoan": "Student", "MortgageLoan": "Adult"}
    _CLIENT_TYPES = {"Adult": Adult, "Student": Student}

    def __init__(self, capacity: int) -> None:
        self.capacity = capacity
        self.loans: list[BaseLoan] = []
        self.clients: list[BaseClient] = []

    def _find_client(self, client_id: str) -> BaseClient | None:
        return next((c for c in self.clients if c.client_id == client_id), None)

    def add_loan(self, loan_type: str) -> str:
        if loan_type not in self._LOAN_TYPES:
            raise Exception("Invalid loan type!")

        self.loans.append(self._LOAN_TYPES[loan_type]())
        return f"{loan_type} was successfully added."

    def add_client(self, client_type: str, client_name: str, client_id: str, income: float) -> str:
        if client_type not in self._CLIENT_TYPES:
            raise Exception("Invalid client type!")

        if len(self.clients) == self.capacity:
            return "Not enough bank capacity."

        self.clients.append(self._CLIENT_TYPES[client_type](client_name, client_id, income))
        return f"{client_type} was successfully added."

    def grant_loan(self, loan_type: str, client_id: str) -> str | None:
        client = self._find_client(client_id)
        if client is None:
            return None

        if self._LOAN_CLIENT[loan_type] != type(client).__name__:
            raise Exception("Inappropriate loan type!")

        loan = next((l for l in self.loans if type(l).__name__ == loan_type), None)
        if loan is None:
            return None

        client.loans.append(loan)
        self.loans.remove(loan)

        return f"Successfully granted {loan_type} to {client.name} with ID {client_id}."

    def remove_client(self, client_id: str) -> str:
        client = self._find_client(client_id)
        if client is None:
            raise Exception("No such client!")

        if client.loans:
            raise Exception("The client has loans! Removal is impossible!")

        self.clients.remove(client)
        return f"Successfully removed {client.name} with ID {client_id}."

    def increase_loan_interest(self, loan_type: str) -> str:
        affected_loans = 0
        for loan in self.loans:
            if type(loan).__name__ == loan_type:
                loan.increase_interest_rate()
                affected_loans += 1

        return f"Successfully changed {affected_loans} loans."

    def increase_clients_interest(self, min_rate: float) -> str:
        affected_clients = 0
        for client in self.clients:
            if client.interest < min_rate:
                client.increase_clients_interest()
                affected_clients += 1

        return f"Number of clients affected: {affected_clients}."

    def get_statistics(self) -> str:
        granted_loans = sum(len(c.loans) for c in self.clients)
        total_income = sum(c.income for c in self.clients)
        granted_sum = sum(l.amount for c in self.clients for l in c.loans)
        avg_client_rate = sum(c.interest for c in self.clients) / len(self.clients) if self.clients else 0
        available_sum = sum(l.amount for l in self.loans)
        res = [f"Active Clients: {len(self.clients)}",
               f"Total Income: {total_income:.2f}",
               f"Granted Loans: {granted_loans}, Total Sum: {granted_sum:.2f}",
               f"Available Loans: {len(self.loans)}, Total Sum: {available_sum:.2f}",
               f"Average Client Interest Rate: {avg_client_rate:.2f}"]

        return "\n".join(res)