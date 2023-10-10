import argparse
import json
from mock import get_mocked_user

parser = argparse.ArgumentParser(description=)

arguments = vars(parser.parse_args())
filename = arguments.get("filename")
num = arguments.get("num")

# db access
with open(filename, mode='w') as file:
    users = list()
    for i in range(int(num)):
        