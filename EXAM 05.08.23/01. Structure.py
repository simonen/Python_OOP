from project.loans.base_loan import BaseLoan
from project.loans.student_loan import StudentLoan
from project.loans.mortgage_loan import MortgageLoan
from project.clients.student import Student
from project.clients.adult import Adult
from project.bank_app import BankApp


student = StudentLoan()

print(student.interest_rate)
print(student.amount)
print(student.increase_interest_rate())
print(student.interest_rate)

mort = MortgageLoan()

print(mort.interest_rate)
print(mort.amount)
mort.increase_interest_rate()
print(mort.interest_rate)

print("______________")
bank = BankApp(3)

print(bank.add_loan('StudentLoan'))
print(bank.add_loan('MortgageLoan'))
print(bank.add_loan('StudentLoan'))
print(bank.add_loan('MortgageLoan'))

print("____________")
print(bank.add_client('Student', 'Peter Simmons', '1234567891', 500))
print(bank.add_client('Adult', 'Samantha Peters', '1234567000', 1000))
print(bank.add_client('Student', 'Simon Mann', '1234567999', 700))
print(bank.add_client('Student', 'Tammy Smith', '1234567555', 700))

print(bank.grant_loan('StudentLoan', '1234567891'))
print(bank.grant_loan('MortgageLoan', '1234567000'))
print(bank.grant_loan('MortgageLoan', '1234567000'))
print("_______________")
print(bank.remove_client('1234567999'))
print("_______________")
print(bank.increase_loan_interest('StudentLoan'))
print(bank.increase_loan_interest('MortgageLoan'))
print("_______________")
print(bank.increase_clients_interest(1.2))
print(bank.increase_clients_interest(3.5))

print("_______________")
print(bank.get_statistics())
