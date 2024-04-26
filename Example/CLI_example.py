import src.simplePyCLI as cli_class
import datetime
cli = cli_class.simplePyCLI()
cli.cursor = ">" # setting cursor format
cli.error_msg = "Wrong Input"
cli.ok_msg = "OK-OK"
cli.debug = True
#
# template for adding command into CLI
#
def hello(name):
    print(f"Hello {name}")

cmd_str = "hello" #  input string that assosiated with funciton below
cmd_action = hello # should be a callable function
n_params = 1 # number of parameters separated with space
cmd_help = "Replay hello to given name" # describe action to automatically generate help
cli.add_command(cmd_str, cmd_action, n_params, cmd_help)

#
# template for adding command into CLI
def add(a,b):
    a = float(a)
    b = float(b)
    print(f"summ of {a} + {b} = {a+b}")
cmd_str = "add"
cmd_action = add
n_params = 2
cmd_help = "Add a + b and print result "
cli.add_command(cmd_str, cmd_action, n_params, cmd_help)
# end of command template


#
# template for adding command into CLI
def time():
    t = datetime.datetime.now()
    print(f"Current time is: {t}")
cmd_str = "time"
cmd_action = time
n_params = 0
cmd_help = "Print current time"
cli.add_command(cmd_str, cmd_action, n_params, cmd_help)
# end of command template

#
# template for adding command into CLI
def print_symb(symbol,n_times):
    n_times = int(n_times)
    for z in range(n_times):
        print(f"{symbol}")
cmd_str = "print"
cmd_action = print_symb
n_params = 2
cmd_help = "[>print A B] Print symbol A, times B "
cli.add_command(cmd_str, cmd_action, n_params, cmd_help)
# end of command template


while True:
    cmd = input("Enter your command:")
    if cmd != "\n":  # Check if there's any data available to read
        cmd_with_params = cmd.strip()  # Read the command with parameters from UART and decode it
        # print(cmd_with_params)
        cli.process_command(cmd_with_params)  # Process the command