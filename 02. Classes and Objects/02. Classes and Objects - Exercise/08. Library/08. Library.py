from project.library import Library
from project.user import User
from project.registration import Registration


user = User(12, 'Peter')
user2 = User(13, 'Gertge')
library = Library()
registration = Registration()

library.books_available.update({'J.K.Rowling': ['The Chamber of Secrets',
 'The Prisoner of Azkaban',
 'The Goblet of Fire',
'The Order of the Phoenix',
'The Half-Blood Prince',
 'The Deathly Hallows']})

print(library.books_available)
print(library.rented_books)
print(library.get_book('J.K.Rowling', 'The Deathly Hallows', 12, user))
print(library.get_book('J.K.Rowling', 'The Chamber of Secrets', 12, user))
print(library.get_book('J.K.Rowling', 'The Prisoner of Azkaban', 12, user))
print(library.get_book('J.K.Rowling', 'The Goblet of Fire', 12, user))
print(library.get_book('J.K.Rowling', 'The Order of the Phoenix', 12, user))
print(library.get_book('J.K.Rowling', 'The Half-Blood Prince', 22, user))
print(library.rented_books)
print(library.books_available)
print(user.username, user.books)
print("-000000000000")
print(library.get_book('J.K.Rowling', 'The Half-Blood Prince', 111, user2))
library.return_book('J.K.Rowling', 'The Half-Blood Prince', user)
print(user.username, user.books)
print(library.get_book('J.K.Rowling', 'The Half-Blood Prince', 111, user2))
print(library.rented_books)
registration.add_user(user, library)
print(registration.change_username(12, 'Pedro', library))
print(registration.change_username(12, 'Pedro', library))
print(registration.remove_user(user2, library))
print(library.rented_books)
# print(registration.remove_user(user, library))
# registration.add_user(user, library)
# print(registration.change_username(2, 'Igor', library))
# print(registration.change_username(12, 'Pedro', library))
# print(registration.change_username(12, 'George', library))
# print(registration.change_username(12, 'George', library))

# print(registration.remove_user(user, library))
# print(registration.remove_user(user, library))
#
# [print(f'{user_record.user_id}, {user_record.username}, {user_record.books}') for user_record in library.user_records]

# library.get_book('J.K.Rowling', 'The Deathly 22121Hallows', 17, user)
# print(library.books_available)
# print(library.rented_books)
# print(user.books)
# print(library.get_book('J.K.Rowling', 'The De22athly Hallows', 10, user))
# print(library.get_book('J.K.Rowling', 'The Deathly Hallows', 10, user))
# print(library.return_book('J.K.Rowling', 'The Cursed Child', user))
# print(library.return_book('J.K.Rowling', 'The Cursed Child', user))
# library.return_book('J.K.Rowling', 'The Deathly Hallows', user)
# library.return_book('J.K.Rowling', 'The Deathl1y Hallows', user)
# library.return_book('J.K.Rowling', 'The Deathly Hallows', user)
# print(registration.remove_user(user2, library))
# print(library.books_available)
# print(library.rented_books)
# print(user.books)


