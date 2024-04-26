
"""
File: simplePyCLI.py
Author: Aleksandr Chasnyk,
link: https://github.com/ami3go
Start Date: 27.04.24
Last update:

Description:
Simple CLI for micropython and python projects when
command line interface is required.
Tested on RP2040 MicroPython
"""
class simplePyCLI:

    def __init__(self, cli_symbol: str = "~"):
        self.commands = {}  # Dictionary to store commands and their corresponding actions
        self._cursor = cli_symbol
        self._debug = False
        self._error_msg = "ERROR"
        self._ok_msg = "OK"
        # add default command
        self.add_command("help", self._print_help, 0, "Print help")
        self.add_command("toggle_debug", self._toggle_debug, 0, "Toggle short/long replay messages")

    @property
    def cursor(self) -> None:
        return self._cursor

    @cursor.setter
    def cursor(self, symbol: str) ->None:
        self._cursor = symbol

    @property
    def debug(self) -> None:
        return self._debug

    @debug.setter
    def debug(self, val: bool) -> None:
        '''
        Enable/Disable extended error messages
        :param val: bool could be  True or False
        :return: None
        '''
        self._debug = bool(val)

    @property
    def error_msg(self) -> None:
        return self._error_msg

    @error_msg.setter
    def error_msg(self, txt: str) -> None:
        '''
        Setting short message in case of Error
        :param txt: string with short message for error, typically "ERROR"
        :return: None
        '''
        self._error_msg = f"{txt}"

    @property
    def ok_msg(self) -> None:
        return self._ok_msg

    @ok_msg.setter
    def ok_msg(self, txt: str) -> None:
        '''
        Setting short confirmation message.
        It confirms that command founded in list
        and proper number of parameters provided
        :param txt: string with short message for error, typically "OK"
        :return: None
        '''
        self._ok_msg = f"{txt}"

    def add_command(self, command: str, action, max_params: int = 3, description: str = ""):
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
            # checking first if command available in list
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

            # Respond if the command is not recognized
            else:
                error_debug = f'{self._cursor}{in_var} Unknown command. Use "help" to get supported commands list'
                self._print_debug_msg(self._error_msg, error_debug)


    def _toggle_debug(self) -> None:
        '''
        Toggling debug variable value. you can see incoming messages
        :return: None
        '''
        self.debug = not self.debug

    def _print_debug_msg(self, short: str ="ERROR", long: str ="") -> None:
        '''
        Print "error" or "Ok" messages based on value of debug variable
        if debug = True full message will be returned
        if debug  False only shor message will be returned
        :param short: string for short message
        :param long: string for log messages
        :return: None
        '''
        if self._debug:
            print(f"{short}, {long}")
        else:
            print(f"{short}")

    def _print_help(self) -> None:
        cmd_keys = list(self.commands.keys())
        n = 30
        print("-" * n, "HELP", "-" * n)
        for cmd in cmd_keys:
            action, params, help = self.commands[cmd]
            print(f"{self._cursor} {cmd}  {'X ' * params} ; Desc: {help}")
        print("-" * (2*n + 6))
