cmd_with_params = "add 1 2 3"
print(cmd_with_params.split())
cmd, *params = cmd_with_params.split()
print(cmd)
print(*params)