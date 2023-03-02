import datetime


class cols:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def colorize(text, color):
    return f"{color}{text}{cols.ENDC}"


def timeout(ms_before_timeout, start_time):
    return (datetime.datetime.now() - start_time).total_seconds() > ms_before_timeout / 1000
