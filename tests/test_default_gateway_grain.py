from grains_from_collectors.default_gateway_grain import get_default_gateway


def test_get_default_gateway():
    input_string = '''
205.153.31.0/24 dev eth0  proto kernel  scope link  src 205.153.31.132
10.18.0.0/16 via 205.153.31.1 dev eth0
169.254.0.0/16 dev eth0  scope link
default via 205.153.31.1 dev eth0'''

    assert '205.153.31.1' == get_default_gateway(test_input_data=input_string)['default_gateway']
