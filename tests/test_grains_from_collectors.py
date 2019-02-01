
from click.testing import CliRunner

from grains_from_collectors.cli import main


def test_main():
    runner = CliRunner()
    result = runner.invoke(main, ['tests/resources'])

    assert result.output == '()\n'
#    assert result.output == 'DONE !!!'

    assert result.exit_code == 0
