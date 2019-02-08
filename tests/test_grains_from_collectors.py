
from click.testing import CliRunner

from grains_from_collectors.cli import main


def test_main(tmp_path):
    from real_data import path_to_real_data_file
    runner = CliRunner()
    result = runner.invoke(main, [str(tmp_path) + '/collector_data.yml',
                                  path_to_real_data_file()])

    assert result.output == '97\n'
    assert result.exit_code == 0
