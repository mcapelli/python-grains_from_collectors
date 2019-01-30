def get_collector_name(salt_data):
    for key, value in salt_data.items():
        return key


def get_ip_address(salt_data):
    for key, value in salt_data.items():
        return value['ip4_interfaces']['eth0'][0]


def get_collector_dicts(input_data):
    result_list = []
    for key, value in input_data.items():
        this_dict = {}
        this_dict['hostname'] = key
        try:
            this_dict['host_ip_address'] = value['ip4_interfaces']['eth0'][0]
        except KeyError:
            continue
        this_dict['nameservers'] = value['dns']['ip4_nameservers'][0]
        """
        Discard dict entry if role is Hub
        """
        for key in value:
            if key == 'roles' and value['roles'][0] == 'z4Collector':
                result_list.append(this_dict)


    return result_list


def get_data_from_yaml_file(input_file):
    import yaml
    with open(input_file) as f:
        yaml_data = yaml.load(f)
    return yaml_data
