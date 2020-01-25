import sys
from os import getcwd

print(f"Running from {getcwd()}")
if "--port" in sys.argv:
    try:
        port = int(sys.argv[sys.argv.index("--port") + 1])
    except ValueError:
        print("An invalid port number was given.")
        exit()
else:
    print("No port aregument was given")
    exit()

file = open("Server_Santi/default_htaccess", "r")
default = file.read()
file.close()
replace = default.replace("0000", str(port))

file = open("public_html/.htaccess", "w")
file.write(replace)
file.close()
