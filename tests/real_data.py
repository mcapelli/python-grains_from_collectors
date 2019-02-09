def path_to_real_data_file():
    file_name = 'real_data.yml'
    possible_locations = [
        './resources',
        './tests/resources'
    ]
    import os
    for this_path in possible_locations:
        full_path = os.path.join(this_path, file_name)

        if os.path.isfile(full_path):
            return full_path
        raise RuntimeError("Can't find real_data file: real_data.yml")
