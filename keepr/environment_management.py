import os
import platform
import subprocess

from keepr.misc_functions import is_in_venv


def check_virtualenv_installation():
    try:
        if platform.system() == 'Windows':
            subprocess.Popen(["python", "-m", "venv", "env"])
        else:
            subprocess.Popen(["python3", "-m", "venv", "env"])
        return 1
    except Exception as e:
        print(
            "We were not able to create your environment.\
                 The issue might be due to a missing 'python3-venv' package. \
                     Install the package and try again!! "
            )
        return 0


def activate_env():
    if check_virtualenv_installation():
        
        if platform.system() == 'Windows':
            os.chdir(os.path.join('env','Scripts'))
            subprocess.Popen(["activate"])
            os.chdir('../..')
        else:
            subprocess.Popen(["python3", "-m", "venv", "env"])
        os.system('source env/bin/activate')
        print("Environment Activated.")
    else:
        pass
    


def deactivate_env():
    status = is_in_venv()
    if status:
        print("Deactivating environment...")
        if platform.system() == 'Windows':
            subprocess.run(["deactivate"])
        else:
            subprocess.run(["deactivate"])
        print("Environment Deactivated")
    else:
        print("No active environments")
        exit()
