from colorama import init, Fore, Style
init()

def yellow(colored, text):
	print(Fore.YELLOW + colored + Style.RESET_ALL + text)

def green(colored, text):
	print(Fore.GREEN + colored + Style.RESET_ALL + text)

def red(colored, text):
	print(Fore.RED + colored + Style.RESET_ALL + text)