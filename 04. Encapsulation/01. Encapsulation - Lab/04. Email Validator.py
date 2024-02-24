class EmailValidator:

    def __init__(self, min_length: int, mails: list, domains: list):
        self.min_length = min_length
        self.mails = mails
        self.domains = domains

    def __is_name_valid(self, name) -> bool:
        if len(name) >= self.min_length:
            return True

        return False

    def __is_mail_valid(self, mail) -> bool:
        if mail in self.mails:
            return True

        return False

    def __is_domain_valid(self, domain) -> bool:
        if domain in self.domains:
            return True

        return False

    def validate(self, email: str) -> bool:
        name = email.split("@")[0]
        mail = email.split("@")[1].split(".")[0]
        domain = email.split("@")[1].split(".")[1]
        if self.__is_name_valid(name) and self.__is_mail_valid(mail) and self.__is_domain_valid(domain):
            return True

        return False


a = EmailValidator(5, ['gmail', 'yahoo'], ['com', 'cc'])

print(a.validate('pesha@gmail.com'))
print(a.is_mail_valid('gmai'))