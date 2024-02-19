from rich import print
from rich.table import Table

options = {'1':'Runserver', 'Ctrl + C': 'Terminate Server'}

def display_options(options):
    options_table = Table()
    options_table.add_column("Key", style="green", justify="center")
    for k,v in options.items():
        print(f"[green][{k}][/green] > {v}")
        
