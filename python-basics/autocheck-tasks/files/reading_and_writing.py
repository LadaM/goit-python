def file_operations(path, additional_info, start_pos, count_chars):
    with open(path,'+a') as file:
        file.write(additional_info)
        file.flush()

        file.seek(start_pos)
        content = file.read()
        end_pos = count_chars
        return content if end_pos >= len(content) else content[:end_pos]

# print(file_operations('read-write.txt', 'Nothing is forever', 100, 10))

def get_employees_by_profession(path, profession):
    names = []
    
    with open(path, 'r') as file:
        lines = file.readlines()
        print(lines)
        for line in lines:
            if profession in line:
                names.append(line.replace(profession, '').replace('\n', '').strip())
    
    return ' '.join(names)

print(get_employees_by_profession('employees.txt', 'courier'))