import yaml
def get_collector_name(salt_data):
    for key, value in salt_data.items():
        return key


def get_ip_address(salt_data):
    for key, value in salt_data.items():
        return value['ip4_interfaces']['eth0'][0]


def get_collector_dicts(input_data):
    result_list = []
    for key, value in input_data.items():
        """
        Discard input_data dict entry if role is not = Collector
        """

        this_dict = {}
        this_dict['hostname'] = key

        try:
            this_dict['host_ip_address'] = value['ip4_interfaces']['eth0'][0]
        except KeyError:
            continue
        try:
            this_dict['host_default_gateway'] = value['default_gateway']
        except KeyError:
            continue

        try:
            this_dict['host_subnet_mask'] = value['network_mask']
        except KeyError:
            continue

        result_list.append(this_dict)

    return result_list


def get_data_from_yaml_file(input_file):
    import yaml
    with open(input_file) as f:
        yaml_data = yaml.load(f)
    return yaml_data


def create_yaml_file(input_data, output_file):
    with open(output_file, 'w') as yaml_file:
        yaml.dump(input_data, yaml_file, default_flow_style=False)

