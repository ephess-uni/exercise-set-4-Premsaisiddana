""" ex_4_1.py """
import os

try:
    from src.ex_4_0 import get_shutdown_events
    from src.util import get_data_file_path
except ImportError:
    from ex_4_0 import get_shutdown_events
    from util import get_data_file_path

FILENAME = get_data_file_path('messages.log')

def num_shutdowns(logfile):
    shutdown_lines = get_shutdown_events(logfile)
    num_shutdowns = 0
    for line in shutdown_lines:
        if "Shutdown initiated" in line or "Shutdown complete" in line:
            num_shutdowns += 1
    return num_shutdowns

if __name__ == "__main__":
    print(f'{num_shutdowns(FILENAME)=}')
