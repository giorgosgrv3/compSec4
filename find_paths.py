import os
import fabric
import paramiko

print("Fabric location:", os.path.dirname(fabric.__file__))
print("Paramiko location:", os.path.dirname(paramiko.__file__))