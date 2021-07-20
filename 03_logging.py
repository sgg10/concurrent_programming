import logging
from colorama import Fore

logging.basicConfig(
    level=logging.DEBUG,
    format=f'[%(levelname)s] - %(processName)s - %(message)s',
    #datefmt='%H:%M:%S',
    #filename='messages.log'
)

def messages():
    logging.debug(f"{Fore.CYAN}This is a debug message{Fore.RESET}")
    logging.info(f"{Fore.BLUE}This is an info message{Fore.RESET}")
    logging.warning(f"{Fore.YELLOW}This is a warning message{Fore.RESET}")
    logging.error(f"{Fore.RED}This is an error message{Fore.RESET}")
    logging.critical(f"{Fore.MAGENTA}This is a critical message{Fore.RESET}")

if __name__=="__main__":
    messages()