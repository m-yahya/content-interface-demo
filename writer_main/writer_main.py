
import atexit

import writer_main.writer_pkg as pkg


def init():
    pkg.init()


@atexit.register
def main():
    pkg.get_vars()

