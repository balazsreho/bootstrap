#! /usr/bin/env/python

"""
#TODO write me
"""

# OS packages
import os
import sys
import time
import subprocess
# Third-party packages
# Custom imports

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

GIT_URL = "https://github.com/balazsreho/bootstrap.git"

LOGO = "\n\n"\
"    ____              __       __\n" \
"   / __ )____  ____  / /______/ /__________ _____\n" \
"  / __  / __ \/ __ \/ __/ ___/ __/ ___/ __ `/ __ \\\n" \
" / /_/ / /_/ / /_/ / /_(__  ) /_/ /  / /_/ / /_/ /\n" \
"/_____/\____/\____/\__/____/\__/_/   \__,_/ .___/\n" \
"                                         /_/     \n\n"

if __name__ == "__main__":
    sys.stdout = os.fdopen(sys.stdout.fileno(), 'w', 0)
    sys.stdout.write("The")
    time.sleep(0.5)
    sys.stdout.write(" ultimate")
    for _ in range(0, 3):
        time.sleep(0.3)
        sys.stdout.write(".")
    time.sleep(0.8)
    print(LOGO)
    time.sleep(0.8)
    print(BOLD + "You are going to install apps, configurations and more!" + ENDC)
    print("First, we have to download our special script to get started...")
    print(BOLD + QUESTION + "Proceed?" + ENDC)
    ans = raw_input(QUESTION + "(y/N): " + ENDC)
    if not (str(ans) in "y" or str(ans) in "Y"):
        exit()

    print("Checking git...")
    command = "which top"
    print(COMMAND + " > {}".format(command) + ENDC)
    git_check_process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    git_check_process.wait()
    if "git" not in git_check_process.stdout.read().strip(' \t\n\r'):
        command = "apt-get install -y git"
        git_install_process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        git_install_process.wait()

    filename = "/tmp/conftemp-" + str(int(time.time()))
    print(BOLD + "Cloning into \"{}\"...".format(filename) + ENDC)
    os.mkdir(filename)
    os.chdir(filename)
    command = "git clone {}".format(GIT_URL)
    print(COMMAND + " > {}".format(command) + ENDC)
    p_gitclone = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    p_gitclone.wait()
    print(BOLD + "Cloned!" + ENDC)
    os.chdir(os.path.join(filename, "bootstrap"))

    install_process = subprocess.Popen("python -d data/install.py", shell=True, stderr=sys.stderr,
                                       stdout=sys.stdout)
    install_process.wait()
    print(HEADER + BOLD + "Yay! All set, your are ready!" + ENDC)
