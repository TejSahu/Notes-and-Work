import os
import subprocess

# run a shell command
# sub = subprocess.run(["less", "reply.json"])

subprocess.run(["less", "reply.json"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)


# print pwd
# print(os.getcwd())
