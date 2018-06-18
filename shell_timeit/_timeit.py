import sys
from subprocess import check_output
from IPython import get_ipython


def entry():
    ipython = get_ipython()
    cmd = " ".join(sys.argv[1:])

    def run_cmd():
        check_output(cmd, shell=True)

    ipython.magic("timeit run_cmd()")
