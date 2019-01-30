def get_network_mask(test_input_data=None):
    # run ps  command 'cat /etc/sysconfig/network-scripts/ifcfg-eth0'
    # and save output to string variable
    # parse the output string
    import subprocess

    if test_input_data:
        output = test_input_data  # type: str
    else:
        # get output using subprocess
        output = subprocess.check_output("cat /etc/sysconfig/network-scripts/ifcfg-eth0", shell=True, universal_newlines=True)

    # first break the string into a list of lines
    # each line should be a list
    # look for the list starting with NETMASK and extract the net mask
    lines = output.split('\n')
    for l in lines:
        if l.startswith('NETMASK='):
            return {'network_mask': l[8:]}

    return {'network_mask': None}
