import click
import platform

print(platform.python_version())


@click.group()
def cli():
   """ Welcome to Skynet """ 

@cli.command()
@click.option('--temp',type = int, help="This is the temp you want to convert")
@click.option('--units', help="The units of your temperature and what you want to convert to")
def convert(temp,units):
	if units == 'f2c':
		new_temp = (temp-32)*5/9
		print(f'{temp} F degrees is equal to {new_temp} degrees C')

@cli.command()
def initiate():
        click.echo("skynet is not initiating")
