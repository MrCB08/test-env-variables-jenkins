from decouple import config

server = config("SERVER1")
user1 = config("SERVER1_USER")
pass1 = config("SERVER1_PASS")

print(server)
print(user1)
print(pass1)