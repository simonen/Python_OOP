class Profile:

    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password

    @property
    def username(self):
        return self.__username

    @property
    def password(self):
        return self.__password

    @username.setter
    def username(self, value):
        if len(value) not in range(5, 16):
            raise ValueError("The username must be between 5 and 15 characters.")
        else:
            self.__username = value

    @password.setter
    def password(self, value):
        if len(value) >= 8 and len(list(filter(lambda x: x.isdigit() or x.isupper(), value))) >= 2:
            self.__password = value
        else:
            raise ValueError('The password must be 8 or more characters with at least 1 digit and 1 uppercase letter.')

    def __str__(self):
        return f'You have a profile with username: "{self.username}" and password: {"*" * len(self.password)}'


profile_with_invalid_password = Profile('My_username', 'My-p2assword')
print(profile_with_invalid_password)
# profile_with_invalid_username = Profile('Too_long_username', 'Any')
# correct_profile = Profile("Username", "Passw0rd")
# print(correct_profile)