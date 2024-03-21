# Split an email address into a user name and a domain
addr = "bob@python.org"
print(addr)
user, domain = addr.split("@")

print(user)
# Prints bob

print(domain)
# Prints python.org
