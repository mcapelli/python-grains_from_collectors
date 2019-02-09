
from click.testing import CliRunner

from grains_from_collectors.cli import main


def test_main(tmp_path):
    from real_data import path_to_real_data_file
    runner = CliRunner()
    output_file = str(tmp_path) + '/collector_data.yml'
    input_file = path_to_real_data_file()
    result = runner.invoke(main, [input_file, output_file], standalone_mode=False)

    assert result.output == '106\n'
    assert result.exit_code == 0
