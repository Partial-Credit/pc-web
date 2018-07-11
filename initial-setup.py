#!/usr/bin/env python3
import os, sys
import random


# os.chdir(os.path.dirname(__file__))
current_path = os.getcwd()
print(current_path)

if "/pc-web" not in current_path:
    print("Please CD into the pc-web repository/directory before running this script!")
    sys.exit(1)

if "/pc-web/" in current_path:
    print("Please move up one level to run the script at the root of the repository. (/pc-web)")
    sys.exit(1)

env_path = current_path + "/pcwebsite/settings/env.py"
secret_key = ''.join(random.SystemRandom().choice('abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)') for i in range(50))

print("Please enter the credentials used when setting up the local postgreSQL database.")

db_name = input("\n  DB Name (default: pcwebsite): ")
if db_name is '':
    db_name = 'pcwebsite'

db_user = input("  User (default: admin): ")
if db_user is '':
    db_user = 'admin'

db_pass = input("  Password: ")

env_lines = [
    "# Partial Credit Website Environment Variables\n",
    "# SECURITY WARNING: keep the secret key used in production secret!\n",
    "LOCAL_SECRET_KEY=\"" + secret_key + "\"\n",
    "DB_NAME=\"" + db_name + "\"\n",
    "DB_USER=\"" + db_user + "\"\n",
    "DB_PASS=\"" + db_pass + "\"\n",
]

print("\nWriting /pcwebsite/setttings/env.py file... ", end='')
try:
    with open(env_path, 'w') as env_file:
        env_file.writelines(env_lines)
except IOError:
    print("Failed to write.\n")
    sys.exit(1)
print("SUCCESS\n")
