import time


def expires():
    """
    Generate a UNIX style timestamp representing 5 minutes from now
    """
    return int(time.time()+300)