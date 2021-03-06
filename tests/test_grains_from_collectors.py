
from click.testing import CliRunner

from grains_from_collectors.cli import main


def test_main(tmp_path):
    from grains_from_collectors.utility import path_to_resource
    runner = CliRunner()
    output_file = str(tmp_path) + '/collector_data.yml'
    input_file = path_to_resource('simple_data.yml')
    result = runner.invoke(main, [input_file, output_file], standalone_mode=False)

    assert result.output == '2\n'
    assert result.exit_code == 0


def test_main_usage(tmp_path):
    runner = CliRunner()
    result = runner.invoke(main, [])

    assert result.output == """Usage: main [OPTIONS] INPUT_FILE OUTPUT_FILE
Try "main --help" for help.

Error: Missing argument "INPUT_FILE".
"""
    assert result.exit_code == 2
