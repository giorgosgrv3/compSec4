from getpass import getpass
from fabric import Connection

password = getpass("Enter your WSL password: ")

c = Connection(
    "giosthspanagias@localhost",
    connect_kwargs={"password": password},
)

result = c.run("echo Running on local")
print(result)
