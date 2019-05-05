import click


@click.command()
@click.option('--name', '-n', help='The person to greet.')
def cli(name):
    click.echo(f'Hello {name}!')


if __name__ == '__main__':
    cli()
