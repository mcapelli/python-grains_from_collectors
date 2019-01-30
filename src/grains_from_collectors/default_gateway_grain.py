def get_default_gateway(test_input_data=None):
    #  run ps  command 'ip route ls' and save output to string variable
    # parse the output string
    import subprocess

    if test_input_data:
        output = test_input_data  # type: str
    else:
        # get output using subprocess
        output = subprocess.check_output("ip route ls", shell=True, universal_newlines=True)

    # first break the string into a list of lines
    # each line should be a list
    # look for the last line/list and extract the third [2] occurence ...
    lines = output.split('\n')
    for l in lines:
        if l.startswith('default '):
            return {'default_gateway': l.split()[2]}
    return {'default_gateway': None}
