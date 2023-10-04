import os

def total_salary(path: str):
    file_reader = open(path, 'r')
    tot_salary = 0
    for line in file_reader.readlines():
        salary_str = line[line.find(',') : ].strip(',\n')
        salary = float(salary_str) if salary_str.isdigit() else 0
        tot_salary += salary
        print(tot_salary)
    file_writer = open(path, 'w')
    file_writer.write()
    file_reader.close()
    return tot_salary

    
absolute_path = os.path.dirname(__file__)
# print("Absolute path = {}".format(absolute_path))
relative_path = 'salaries.txt'
path_to_file = os.path.join(absolute_path, relative_path)

total_salary(path_to_file)    
        
    
