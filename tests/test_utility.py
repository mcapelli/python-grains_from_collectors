import yaml


from grains_from_collectors.utility import get_collector_name
from grains_from_collectors.utility import get_ip_address
from grains_from_collectors.utility import get_collector_dicts
from grains_from_collectors.utility import get_data_from_yaml_file


def find_subdir(input_dir):
    """Return the relative path of a directory

    Used by test fixtures to find resource files regardless of where pytests is from from (project_root,
    project_root/tests, etc). This didn't matter when i was just running pytests directly, but tox runs form teh
    project dir so this fixes that problem
    """
    import os
    for root, dirs, files in os.walk("."):
        for d in dirs:
            if d == input_dir:
                return os.path.relpath(os.path.join(root, d), ".")


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
  host_default_gateway: '29.29.29.29'
  host_subnet_mask: '255.255.255.0'
- hostname: second_collector_name
  host_ip_address: '88.88.88.88'
  host_default_gateway: '28.28.28.28'
  host_subnet_mask: '255.255.255.0'
    """

    input_yaml = """
    first_collector_name:
      ip4_interfaces:
        eth0:
          - 99.99.99.99
      dns:
        ip4_nameservers:
          - 19.19.19.19    
      roles:
        - z4Collector
      default_gateway:
        29.29.29.29
      network_mask:
        255.255.255.0
    second_collector_name:
      ip4_interfaces:
        eth0:
          - 88.88.88.88
      dns:
        ip4_nameservers:
          - 18.18.18.18    
      roles:
        - z4Collector
      default_gateway:
        28.28.28.28
      network_mask:
        255.255.255.0      
    """
    input_data = yaml.load(input_yaml)
    expected_data = yaml.load(expected_yaml)
    result = get_collector_dicts(input_data)
    assert expected_data[0] in result
    assert expected_data[1] in result
    assert len(result) == 2
    assert result[0] in expected_data
    assert result[1] in expected_data



"""
def test_real_data():
    arq = '/resources/two_item_sample.yml'
    real = get_data_from_yaml_file(arq)
    result = get_collector_dicts(real)
    assert len(result) == 2
"""

