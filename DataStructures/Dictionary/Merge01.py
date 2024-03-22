D1 = {"name": "Bob", "age": 25, "job": "Dev"}
print(D1)

D2 = {"age": 30, "city": "New York", "email": "bob@web.com"}
print(D2)

D1.update(D2)
print(D1)
# Prints {'name': 'Bob', 'age': 30, 'job': 'Dev',
#         'city': 'New York', 'email': 'bob@web.com'}
