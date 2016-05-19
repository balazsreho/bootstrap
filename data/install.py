#! /usr/bin/env/python

"""
#TODO write me
"""

# OS packages
import subprocess
# Third-party packages
# Custom imports
from apt_packages import *

__author__ = "Balazs Reho"
__copyright__ = "Copyright 2016, Balazs Reho"
__credits__ = ["Balazs Reho"]
__license__ = "MIT license"
__version__ = "0.1.0"
__maintainer__ = "Balazs Reho"
__email__ = "reho.balazs@gmail.com"


HEADER = '\033[95m'
QUESTION = '\033[94m'
COMMAND = '\033[92m'
WARNING = '\033[93m'
FAIL = '\033[91m'
ENDC = '\033[0m'
BOLD = "\033[1m"


def install_apt():
    command_base = "apt-get install -y"
    command = command_base + " ".join(APT_PACKAGES)
    print(COMMAND + " > {}".format(command) + ENDC)


if __name__ == '__main__':
    print(QUESTION + BOLD + "Do you want to install all default apps?" + ENDC)
    for item in APT_PACKAGES:
        print(" * {}".format(item))

    ans = raw_input(QUESTION + "(y/N): " + ENDC)
    if not ("y" in str(ans) or "Y" in str(ans)):
        exit()

    install_apt()
