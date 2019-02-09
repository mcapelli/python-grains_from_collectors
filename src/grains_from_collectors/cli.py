"""
Module that contains the command line app.

Why does this file exist, and why not put this in __main__?

  You might be tempted to import things from __main__ later, but that will cause
  problems: the code will get executed twice:

  - When you run `python -mgrains_from_collectors` python will execute
    ``__main__.py`` as a script. That means there won't be any
    ``grains_from_collectors.__main__`` in ``sys.modules``.
  - When you import __main__ it will get executed again (as a module) because
    there's no ``grains_from_collectors.__main__`` in ``sys.modules``.

  Also see (1) from http://click.pocoo.org/5/setuptools/#setuptools-integration
"""
import click


@click.command()
@click.argument('input_file')
@click.argument('output_file')
def main(input_file, output_file):
    from grains_from_collectors.utility import get_data_from_yaml_file,\
        get_collector_dicts, create_yaml_file
    input_data = get_data_from_yaml_file(input_file)
    result = get_collector_dicts(input_data)
    create_yaml_file(result, output_file)

    click.echo(str(len(result)))

