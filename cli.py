import click
from colorama import Fore, Back, Style

@click.command()
@click.option('--name', prompt='Your name', help='The person to greet.')
def hello(name):
    print(Back.BLUE + Fore.WHITE + Style.BRIGHT + """
 __     __   __     ______     ______     __   __     ______     __  __    
/\ \  _ \ \ /\ \   /\  ___\   /\  ___\   /\ "-.\ \   /\  ___\   /\_\_\_\   
\ \ \/ ".\ \\ \ \  \ \  __\   \ \___  \  \ \ \-.  \  \ \  __\   \/_/\_\/_  
 \ \__/".~\_\\ \_\  \ \_____\  \/\_____\  \ \_\\"\_\  \ \_____\   /\_\/\_\ 
  \/_/   \/_/ \/_/   \/_____/   \/_____/   \/_/ \/_/   \/_____/   \/_/\/_/ 

""" + Style.RESET_ALL)

    click.echo(f"Hello, {name}!")

if __name__ == '__main__':
    hello()
