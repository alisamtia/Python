# Custom Expection error in Python
#   Q - WHY CUSTOM EXPECTIONS
#   A - to incraese the readability of code


# example
class NameTooShort(ValueError):
    pass

def vaildate(name):
    if len(name) < 8:
        raise NameTooShort('Name is too short')

user_name=input('Enter your name: ')
print(vaildate(user_name))
print(f'hello {user_name}')
# NameTooShort