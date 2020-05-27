import subprocess
import platform
import signal
import sys
import os

from .misc_functions import is_in_venv


def check_virtualenv_exists():
    try:
        process = subprocess.Popen(['virtualenv'], stdout=subprocess.PIPE,
                                   stderr=subprocess.PIPE)
        output, error = process.communicate()
        return 1
    except BaseException:
        return 0


def run_env_script(script_name, path):
    try:
        result = subprocess.run([os.path.join(os.path.dirname(__file__),
                                              'scripts', script_name), path],
                                stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE)
        return result
    except KeyboardInterrupt:
        result.send_signal(signal.SIGINT)


def activate_env():
    if not(is_in_venv()):
        if check_virtualenv_exists():
            if platform.system() == 'Windows':
                result = run_env_script('activate_env.bat', os.getcwd())
            else:
                result = run_env_script('activate_env.sh', os.getcwd())

            output = result.stdout.decode('utf-8')
            returncode = result.returncode
            if returncode == 0 or 'virtualenv' in output:
                print('Environment created!')

        else:
            print('virtualenv is not present on your system.\
                 To get this pip package follow this link https://pypi.org/project/virtualenv/')
            return
    else:
        print("Environment already activated!")


if __name__ == "__main__":
    activate_env()
