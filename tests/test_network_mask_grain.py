from grains_from_collectors.network_mask_grain import get_network_mask


def test_get_network_mask():
    input_string = '''
#Intel Corporation Device 1f41
DEVICE=eth0
BOOTPROTO=static
ONBOOT=yes
IPADDR=10.10.1.252
NETMASK=255.255.255.0
IPV6INIT=no
IPV6_AUTOCONF=no'''

    assert '255.255.255.0' == get_network_mask(test_input_data=input_string)['network_mask']
#    assert '255.255.255.0' == get_network_mask(test_input_data=None)['network_mask']
