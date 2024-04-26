class simplePyCLI:
    def __init__(self, cli_symbol="~"):
        self.commands = {}  # Dictionary to store commands and their corresponding actions
        self._cursor = cli_symbol
        self._debug = False
        self._error_msg = "ERROR"
        self._ok_msg = "OK"
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
        '''
        Enable/Disable extended error messages
        :param val: bool could be  True or False
        :return: None
        '''
        self._debug = bool(val)

    @property
    def error_msg(self):
        return self._error_msg
    @error_msg.setter
    def error_msg(self, txt):
        '''
        Setting short message in case of Error
        :param txt: string with short message for error, typically "ERROR"
        :return: None
        '''
        self._error_msg = f"{txt}"

    @property
    def ok_msg(self):
        return self._ok_msg

    @ok_msg.setter
    def ok_msg(self, txt):
        '''
        Setting short confirmation message.
        It confirms that command founded in list
        and proper number of parameters provided
        :param txt: string with short message for error, typically "OK"
        :return: None
        '''
        self._ok_msg = f"{txt}"

    def add_command(self, command, action, max_params=3, description=""):
        '''
        Adding command into memory
        :param command: string that will bre recognised as command
        :param action: function which will be called
        :param max_params:  maximum number of parameters function need to take
        :param description: text description for generating help
        :return: None
        '''
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
                        error_debug = f'{self._cursor}{in_var} -> Too many parameters. Given: {len(params)}, Requires: {max_params}'
                    else:
                        error_debug = f'{self._cursor}{in_var} -> Missing parameters. Given: {len(params)}, Requires: {max_params}'
                    self._print_debug_msg(self._error_msg, error_debug)
                else:
                    ok_debug = f"{self._cursor}{in_var}"
                    self._print_debug_msg(self.ok_msg, ok_debug)
                    # Execute the action with the provided parameters

                    try:
                        action(*params)
                    except Exception as e:
                        self._print_debug_msg(self._error_msg, e)

            # Print Help
            elif cmd == "help":
                self._print_help()
            else:
                error_debug = f'{self._cursor}{in_var} Unknown command. Use "help" to get supported commands list'
                self._print_debug_msg(self._error_msg, error_debug)
                # Respond if the command is not recognized

    def _print_debug_msg(self, short="ERROR", long=""):
        if self._debug:
            print(f"{short}, {long}")
        else:
            print(f"{short}")


    def _print_help(self, cmd=""):
        cmd_keys = list(self.commands.keys())
        n = 30
        print("-" * n, "HELP", "-" * n)
        for cmd in cmd_keys:
            action, params, help = self.commands[cmd]
            print(f"{self._cursor} {cmd}  {'X ' * params} ; Desc: {help}")
        print("-" * (2*n + 6))
