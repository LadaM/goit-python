# file -> any file .txt .py .exe .json
# scipt -> any file executable in the terminal: bash, shell, .py (can be setup)
# module -> python files that are made to be imported and used by the others files
# package -> all modules, static files (including setup.py, README.md, images), executable files

import utils
from hello import say_hello

print(utils.minutes_to_milliseconds(10))
say_hello("Main")