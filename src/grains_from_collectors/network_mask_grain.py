def get_network_mask(test_input_data=None):

    import subprocess

    if test_input_data:
        output = test_input_data  # type: str
    else:
        # get output using subprocess
        output = subprocess.check_output("ifconfig eth0", shell=True, universal_newlines=True)

    for this_line in output.split('\n'):
        if this_line.split()[0] == 'inet':
            mask = this_line.split()[-1].replace('Mask:', '')
            return {'network_mask': mask}
    return {'network_mask': None}
