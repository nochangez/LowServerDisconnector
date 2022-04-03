# coding=utf-8


import os
import sys


def get_os_name() -> str:
    """
    returns system name (for requirements installing pkg)
    """

    os_data = sys.platform.lower()  # sys name
    
    if os_data in ("linux", "darwin", "os2", "os2emx"):
        return "unix"  # return that current system is a unix machine

    return "win"  # and id current system is a win machine


# get current machine os name
system_name = get_os_name()
system_name_message = f"your system is ", {system_name}

# show current os name
print(system_name_message)

# requirements dict
requirements_installing_dict = {
    "unix": ". ./data/unix_install_requirements.sh",
    "win": "start ./data/win_install_requirements.bat",
}

# print some \n chars
print('\n\n')

# start requirements installing file
os.system(requirements_installing_dict[system_name])

# print some \n chars
print('\n\n')
