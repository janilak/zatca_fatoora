import subprocess
foo1 = subprocess.run(["/bin/sh", "/home/dell/odoo-14.0/custom_addons/zatca_fatoora/models/outgen.sh"])
f=open("test.txt")
w=f.read()
print(w)
f.close()

