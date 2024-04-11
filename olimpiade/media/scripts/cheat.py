"""Script for cheating."""
################### downloading packages ########################
import subprocess
install_requests = ['pip', 'install', 'requests',]
install_pyperclip = ['pip', 'install', 'pyperclip']
subprocess.call(install_requests)
subprocess.call(install_pyperclip)
#################################################################

import logging
import pyperclip
import requests
import time

ENDPOINT: str = 'https://hospitaltj.pythonanywhere.com/api/v1/'


def main() -> None:
    """Start actions."""
    try:
        while True:
            in_buffer = pyperclip.paste()
            task = requests.get(ENDPOINT).json()
            if in_buffer != task['question'] and in_buffer != task['answer']:
                requests.post(ENDPOINT, params={'question': in_buffer})
            pyperclip.copy(task['answer'])
            time.sleep(5)
    except Exception:
        logging.error("Something went wrong. Please run script again.")


if __name__ == '__main__':
    main()
