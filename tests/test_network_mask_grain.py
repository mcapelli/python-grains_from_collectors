from grains_from_collectors.network_mask_grain import get_network_mask


def test_get_network_mask():
    input_string = '''eth0      Link encap:Ethernet  HWaddr 00:50:56:96:24:95
          inet addr:205.153.31.156  Bcast:205.153.31.255  Mask:255.255.255.0
          UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
          RX packets:9898136011 errors:0 dropped:0 overruns:0 frame:0
          TX packets:9318047092 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:1000
          RX bytes:11290021334082 (10.2 TiB)  TX bytes:4463955971560 (4.0 TiB)
'''
    assert '255.255.255.0' == get_network_mask(test_input_data=input_string)['network_mask']
