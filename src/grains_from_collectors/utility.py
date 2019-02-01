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
        if value['roles'][0] != 'z4Collector':
            continue

        this_dict = {}
        this_dict['a_hostname'] = key

        try:
            this_dict['host_ip_address'] = value['ip4_interfaces']['eth0'][0]
        except KeyError:
            continue

        try:
            this_dict['nameservers'] = value['dns']['ip4_nameservers'][0]
        except KeyError:
            continue

        this_dict['default_gateway'] = value['default_gateway']
        this_dict['network_mask'] = value['network_mask']


        result_list.append(this_dict)

    return result_list


def get_data_from_yaml_file(input_file):
    import yaml
    with open(input_file) as f:
        yaml_data = yaml.load(f)
    return yaml_data

def create_yaml_file(output_dir):
    data_from_grains = get_data_from_yaml_file('resources/two_item_sample.yml')
    with open('/'.join([output_dir, 'final_output_file.yml']), 'w') as yaml_file:
        yaml.dump(get_collector_dicts(data_from_grains), yaml_file, default_flow_style=False)


