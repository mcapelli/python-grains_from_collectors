import yaml
from grains_from_collectors.utility import get_collector_name
from grains_from_collectors.utility import get_ip_address
from grains_from_collectors.utility import get_collector_dicts
from grains_from_collectors.utility import get_data_from_yaml_file

def test_get_collector_name():
    """
    figure out the data format in the salt data and
    make a good test

    :return:
    """

    salt_input_yaml = """
first_collector_name:
  ip4_interfaces:
    eth0:
      - 99.99.99.99
"""
    salt_data = yaml.load(salt_input_yaml)
    assert get_collector_name(salt_data) == 'first_collector_name'


def test_get_ip_address():
    """
    figure out the data format in the salt data and
    make a good test

    :return:
    """

    salt_input_yaml = """
first_collector_name:
  ip4_interfaces:
    eth0:
      - 99.99.99.99
"""
    salt_data = yaml.load(salt_input_yaml)
    assert get_ip_address(salt_data) == '99.99.99.99'


def test_get_collector_dicts():
    expected_yaml = """
- hostname: first_collector_name
  host_ip_address: '99.99.99.99'
- hostname: second_collector_name
  host_ip_address: '88.88.88.88'
    """

    input_yaml = """
    first_collector_name:
      ip4_interfaces:
        eth0:
          - 99.99.99.99
      roles:
        - z4Collector 
    second_collector_name:
      ip4_interfaces:
        eth0:
          - 88.88.88.88
      roles:
        - z4Collector    
    """
    input_data = yaml.load(input_yaml)
    expected_data = yaml.load(expected_yaml)

    assert get_collector_dicts(input_data) == expected_data


def test_real_data():
    real = get_data_from_yaml_file('resources/two_item_sample.yml')
    result = get_collector_dicts(real)
    assert len(result) == 2
