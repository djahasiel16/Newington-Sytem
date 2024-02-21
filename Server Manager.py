

import os
import glob

def environmentActivate():
    dirs = [item for item in os.listdir() if os.path.isdir(item)]
    path = ""
    for i in dirs:
        if i[0] == ".":
            if i != ".git":
                path = i
                activate = glob.glob(f"./{path}/**/activate", recursive=True)
                os.system(str(activate[0].replace("/", "\\")))
                os.system("pause")
                return True
            
    return False
    


if environmentActivate():
    from rich import print
    from rich.table import Table
    from rich.console import Console
    

    options = {'1':('Runserver privately', 'py manage.py runserver'), '2': ('Runserver publicly', 'py manage.py runserver 0.0.0.0:8000'), '3':('Exit', False)}
    headers = ['Key', 'Command Description']



    def display_options(options, headers):
        options_table = Table()
        options_table.show_lines = True
        for header in headers:
            options_table.add_column(header, style="green", justify="center")

        for k,v in options.items():
            options_table.add_row(k,v[0])
        
        while True: 
            console = Console()
            console.clear()
            console.print(options_table)
            user_input = console.input("[blue]Select option: [/blue]")
            if user_input in options.keys():
                try:
                    if options[user_input][1]:
                        os.system(options[user_input][1])
                    else:
                        console.log("Server Terminated")
                        break
                    
                except KeyboardInterrupt:
                    console.log('Command Execution Successful')
            else:
                console.print("[red]Invalid Choice[/red]")

    display_options(headers=headers, options=options)

else:
    print("Environment failed to activate")
