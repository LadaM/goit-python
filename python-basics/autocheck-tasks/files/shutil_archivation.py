import shutil

def create_backup(path, file_name, employee_residence):    
    file_path = path + "/" + file_name
    with open(file_path, 'wb') as file:
        # it is expected that each line is written to the file separately
        for employee, residence in employee_residence.items():
            file.write((f"{employee} {residence}" + '\n').encode("utf-8"))

    archive_name = shutil.make_archive('backup_folder', 'zip', path)
    # print(archive_name)
    return archive_name