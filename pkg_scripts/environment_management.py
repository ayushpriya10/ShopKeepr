import os

from pkg_scripts.misc_functions import is_in_venv


def check_virtualenv_installation():
    try:
        # subprocess.Popen(["python3", "-m", "venv", "env"])
        os.system('python3 -m venv env')
    except Exception as e:
        print(
            "We were not able to create your environment. The issue might be due to a missing 'python3-venv' package. "
            "To install the package, run the following command as root:\n\nsudo apt-get install python3-venv\n\nThen "
            "try again.")
        print("The error message we received is as follows:\n\n")
        print(e)


def activate_env():
    check_virtualenv_installation()
    # subprocess.run(["source", "env/bin/activate"])
    os.system('source env/bin/activate')
    print("Environment Activated.")


def deactivate_env():
    status = is_in_venv()
    if status:
        print("Deactivating environment...")
        os.system('deactivate')
        print("Environment Deactivated")
    else:
        print("No active environments")
        exit()
