import colorama

colorama.init(autoreset=True)

print(colorama.Fore.RED + "Fore")
print(colorama.Back.GREEN + "Fore")
# print(colorama.Style.RESET_ALL)

print('=========')
print('\033[32;1m' + "foreground" + '\033[0m')
print('\033[41m' + "background" + '\033[0m')
print('\033[0m' + 'reset')
print('---------')
