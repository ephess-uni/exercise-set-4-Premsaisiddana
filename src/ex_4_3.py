""" ex_4_3.py """
import os

try:
    from src.ex_4_0 import get_shutdown_events
    from src.ex_4_2 import logstamp_to_datetime
    from src.util import get_data_file_path
except ImportError:
    from ex_4_0 import get_shutdown_events
    from ex_4_2 import logstamp_to_datetime
    from util import get_data_file_path

FILENAME = get_data_file_path("messages.log")


def time_between_shutdowns(logfile):

    shutdown_entries = get_shutdown_events(logfile)
    if not shutdown_entries:
        return None  # Return None if no shutdown events are found

    first_shutdown = logstamp_to_datetime(shutdown_entries[0].split()[1])
    last_shutdown = logstamp_to_datetime(shutdown_entries[-1].split()[1])

    time_difference = last_shutdown - first_shutdown

    return time_difference
if __name__ == "__main__":
    print(f'{time_between_shutdowns(FILENAME)=}')


