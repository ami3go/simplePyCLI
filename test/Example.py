import src.simplePyCLI as cli_class

cli = cli_class.simplePyCLI(">")

#
# template for adding command into CLI
#

def hello(txt):
    print(f"Hello {txt}")

cmd_str = "hello" #  input string that assosiated with funciton below
cmd_action = hello # should be a callable function
n_params = 1 # number of parameters separated with space
cmd_help = "say hello" # describe action to automatically generate help
cli.add_command(cmd_str, cmd_action, n_params, cmd_help)

#
# template for adding command into CLI
#
def add(a,b):
    a = float(a)
    b = float(b)
    print(f"summ of {a} + {b} = {a+b}")
cmd_str = "add"
cmd_action = add
n_params = 2
cmd_help = "Add a + b and print result "
cli.add_command(cmd_str, cmd_action, n_params, cmd_help)

while True:
    cmd = input("Enter your command:")
    if cmd != "\n":  # Check if there's any data available to read
        cmd_with_params = cmd.strip()  # Read the command with parameters from UART and decode it
        # print(cmd_with_params)
        cli.process_command(cmd_with_params)  # Process the command