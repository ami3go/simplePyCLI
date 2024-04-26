class simplePyCLI:
    def __init__(self, cli_symbol="~"):
        self.commands = {}  # Dictionary to store commands and their corresponding actions
        self._cursor = cli_symbol
        self._debug = False
    @property
    def cursor(self):
        return self._cursor

    @cursor.setter
    def cursor(self, symbol):
        self._cursor = symbol

    @property
    def debug(self):
        return self._debug

    @debug.setter
    def debug(self, val):
        self._debug = val

    def add_command(self, command, action, max_params=3, description=""):
        self.commands[command] = (action, max_params, description)  # Store the action and maximum parameters for the command
        # print(self.commands)

    def process_command(self, cmd_with_params):
        if cmd_with_params != "":
            cmd, *params = cmd_with_params.split()
            in_var = cmd_with_params.split()
            if cmd in self.commands:
                # Retrieve the action and maximum parameters for the command
                action, max_params, help = self.commands[cmd]

                #print(in_var, "given:", len(params), "max:", max_params)
                if len(params) != max_params:
                    if len(params) > max_params:
                        print(
                            f'ERROR, {self._cursor}{in_var} -> Too many parameters. Given: {len(params)}, Requires: {max_params}')
                    else:
                        print(
                            f'ERROR, {self._cursor}{in_var} -> Missing parameters. Given: {len(params)}, Requires: {max_params}')
                else:
                    print(f"OK, {self._cursor}{in_var}")
                    # Execute the action with the provided parameters
                    try:
                        action(*params)
                    except Exception as e:
                        print("ERROR, ", e)

            # Print Help
            elif cmd == "help":
                self._print_help()
            else:
                print(f'ERROR, {self._cursor}{in_var} Unknown command. Use "help" to get supported commands list')
                # Respond if the command is not recognized

    def _print_help(self, cmd=""):
        cmd_keys = list(self.commands.keys())
        n = 30
        print("-" * n, "HELP", "-" * n)
        for cmd in cmd_keys:
            action, params, help = self.commands[cmd]
            print(f"{self._cursor} {cmd}  {'X ' * params} ; Desc: {help}")
        print("-" * (2*n + 6))
