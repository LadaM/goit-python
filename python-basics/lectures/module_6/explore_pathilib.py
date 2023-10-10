from pathlib import Path

# find out the current path 
current_path = Path.cwd()
print(f"Current path is {current_path}")


# print all files
current_dir = Path('.')

for element in current_dir.iterdir():
    print(element.name)

# explore all folders in the parent dir
parent_dir = Path('./.')
