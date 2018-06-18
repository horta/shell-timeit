import sys
from subprocess import check_output
from IPython.terminal.embed import InteractiveShellEmbed

ipshell = InteractiveShellEmbed()
ipshell.dummy_mode = True


def entry():
    cmd = " ".join(sys.argv[1:])

    def run_cmd():
        check_output(cmd, shell=True)

    print("Estimating running time...")
    ipshell.magic("timeit run_cmd()")
