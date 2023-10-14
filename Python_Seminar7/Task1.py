import os


def rename_files(new_name, digits, source_ext, destin_ext, range_name, path='.'):
    counter = 1
    for filename in os.listdir(path):
        if filename.endswith(source_ext):
            old_name = os.path.splitext(filename)[0]
            old_name_substring = old_name[range_name[0]:range_name[1]] if range_name else ""
            new_filename = f"{old_name_substring}{new_name}{str(counter).zfill(digits)}{destin_ext}"
            os.rename(os.path.join(path, filename), os.path.join(path, new_filename))
            counter += 1


rename_files('new_file', 3, '.txt', '.md', [1, 3], './my_folder')
