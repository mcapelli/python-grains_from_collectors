def get_collector_name(salt_data):
    for key, value in salt_data.items():
        return key


def get_ip_address(salt_data):
    for key, value in salt_data.items():
        return value['ip_interfaces']['eth0'][0]


def get_collector_dicts(input_data):
    result_list = []
    for key, value in input_data.items():
        this_dict = {}
        this_dict['hostname'] = key
        try:
            this_dict['host_ip_address'] = value['ip_interfaces']['eth0'][0]
        except KeyError:
            continue
        result_list.append(this_dict)
        # result_list.append(key)
        # result_list.append(value['ip_interfaces']['eth0'][0])

    return result_list


def get_data_from_yaml_file(input_file):
    import yaml
    with open(input_file) as f:
        yaml_data = yaml.load(f)
    return yaml_data
