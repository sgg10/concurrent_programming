import logging
from colorama import Fore

THREAD_FORMAT = "%(thread)s - %(threadName)s: %(message)s"

def debug(message):
    logging.debug(f"{Fore.GREEN}{message}{Fore.RESET}")

def info(message, normal=False):
    if normal:
        logging.info(message)
    else:
        logging.info(f"{Fore.CYAN}{message}{Fore.RESET}")

def warning(message):
    logging.warning(f"{Fore.YELLOW}{message}{Fore.RESET}")

def error(message):
    logging.error(f"{Fore.RED}{message}{Fore.RESET}")

def critical(message):
    logging.critical(f"{Fore.MAGENTA}{message}{Fore.RESET}")