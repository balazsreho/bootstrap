#! /usr/bin/env/python

"""
#TODO write me
"""

# OS packages
import os
import pwd
import grp
import sys
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


USER = os.environ['SUDO_USER']
FILE_DIR = os.path.dirname(os.path.abspath(__file__))


def _chown_recursive(path, user):
    if os.path.isfile(path):
        os.chown(path, pwd.getpwnam(user).pw_uid, grp.getgrnam(user).gr_gid)
    elif os.path.exists(path):
        for root, dirs, files in os.walk(path):
            for momo in dirs:
                os.chown(os.path.join(root, momo), pwd.getpwnam(user).pw_uid, grp.getgrnam(user).gr_gid)
            for momo in files:
                os.chown(os.path.join(root, momo), pwd.getpwnam(user).pw_uid, grp.getgrnam(user).gr_gid)
            os.chown(root, pwd.getpwnam(user).pw_uid, grp.getgrnam(user).gr_gid)
    else:
        raise OSError("Targer directory not exists.")


def install_apt():
    print("Installing apt packages...")
    command = "apt-get update"
    print(COMMAND + " > {}".format(command) + ENDC)
    apt_update_process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    apt_update_process.wait()
    command_base = "apt-get install -y "
    command = command_base + " ".join(APT_PACKAGES)
    print(COMMAND + " > {}".format(command) + ENDC)
    apt_install_process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    apt_install_process.wait()


def install_oh_my_zsh():
    print("Installing oh-my-zsh...")
    back_dir = os.curdir
    os.chdir(os.path.join("/home", USER))
    git_url = "https://github.com/robbyrussell/oh-my-zsh.git"
    command = "git clone {}".format(git_url)
    print(COMMAND + " > {}".format(command) + ENDC)
    oh_my_install = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    oh_my_install.wait()
    os.rename(os.path.join("/home", USER, "oh-my-zsh"), os.path.join("/home", USER, ".oh-my-zsh"))
    os.chdir(back_dir)
    _chown_recursive(os.path.join("/home", USER, ".oh-my-zsh"), USER)


def configure_zsh_theme():
    print("Downloading zsh theme")
    try:
        os.makedirs(os.path.join("/home", USER, ".oh-my-zsh", "themes"))
    except OSError:
        pass
    back_dir = os.curdir
    os.chdir(os.path.join("/home", USER, ".oh-my-zsh", "themes"))
    git_url = "https://github.com/bhilburn/powerlevel9k.git"
    command = "git clone {}".format(git_url)
    print(COMMAND + " > {}".format(command) + ENDC)
    p_gitclone = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    p_gitclone.wait()
    os.chdir(back_dir)
    _chown_recursive(os.path.join("/home", USER, ".oh-my-zsh", "themes", "powerlevel9k"), USER)


def install_z():
    print("Downloading z.sh")
    back_dir = os.curdir
    os.chdir(os.path.join("/home", USER))
    git_url = "https://github.com/rupa/z.git"
    command = "git clone {}".format(git_url)
    print(COMMAND + " > {}".format(command) + ENDC)
    p_gitclone = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    p_gitclone.wait()
    os.rename(os.path.join("/home", USER, "z"), os.path.join("/home", USER, ".z"))
    os.chdir(back_dir)
    _chown_recursive(os.path.join("/home", USER, ".z"), USER)


def install_zsh_syntax():
    print("Downloading zsh-syntax")
    back_dir = os.curdir
    os.chdir(os.path.join("/home", USER))
    git_url = "https://github.com/zsh-users/zsh-syntax-highlighting.git"
    command = "git clone {}".format(git_url)
    print(COMMAND + " > {}".format(command) + ENDC)
    p_gitclone = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    p_gitclone.wait()
    os.chdir(back_dir)
    _chown_recursive(os.path.join("/home", USER, "zsh-syntax-highlighting"), USER)


def configure_oh_my_zsh():
    print("Configuring oh-my-zsh...")
    with open(os.path.join("/home", USER, ".zshrc"), 'w') as zsh_file:
        custom_export = "export ZSH=/home/{}/.oh-my-zsh".format(USER)
        zsh_file.write(custom_export + "\n")
        with open(os.path.join(FILE_DIR, ".zshrc"), 'r') as template_file:
            for line in template_file.read():
                zsh_file.write(line)
    _chown_recursive(os.path.join("/home", USER, ".zshrc"), USER)


def enable_zsh():
    command = "chsh -s /usr/bin/zsh {}".format(USER)
    print(COMMAND + " > {}".format(command) + ENDC)
    p_gitclone = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    p_gitclone.wait()


if __name__ == '__main__':
    print(QUESTION + BOLD + "Do you want to install all default apps?" + ENDC)
    for item in APT_PACKAGES:
        print(" * {}".format(item))

    ans = raw_input(QUESTION + "(y/N): " + ENDC)
    if not ("y" in str(ans) or "Y" in str(ans)):
        exit()

    install_apt()
    install_oh_my_zsh()
    configure_zsh_theme()
    configure_oh_my_zsh()
    install_z()
    install_zsh_syntax()
    enable_zsh()
