# SimplePyCLI
 Simple CLI for micropython and python projects when command line interface is required. 
Tested on RP2040 MicroPython 


Supported features:
- fool-prove input (entering wrong input will generate just error message)  
- Help generation on "help" command 
- Check if command existed in list of available commands
- Check if command entered with all parameters
- return status 

Please see Example for quick start 
For MiroPython example check:
- https://github.com/ami3go/Digital_NTC_emulation_board.git

### Installation

Option 1 - install as module:

```
pip3 install git+https://github.com/ami3go/simplePyCLI
```
Option 2 

```
TBD
```

### Uninstall

```
pip3 uninstall simplePyCLI
```

### Usage 

#### Initialization 
```Python
import src.simplePyCLI as cli_class
cli = cli_class.simplePyCLI()
cli.cursor = ">" # setting cursor format
cli.debug = True
```

#### Adding commad 
```Python
def hello(name):
    print(f"Hello {name}")

cmd_str = "hello" #  input string that assosiated with funciton below
cmd_action = hello # should be a callable function
n_params = 1 # number of parameters separated with space
cmd_help = "Replay hello to given name" # describe action to automatically generate help
cli.add_command(cmd_str, cmd_action, n_params, cmd_help)
```

### Usage 
```Python
while True:
    cmd = input("Enter your command:")
    if cmd != "\n":  # Check if there's any data available to read
        cmd_with_params = cmd.strip()  # Read the command with parameters from UART and decode it
        # print(cmd_with_params)
        cli.process_command(cmd_with_params)  # Process the command
```

