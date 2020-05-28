from keepr.__main__ import run_application
from click.testing import CliRunner

import sys
sys.path.append('..')


def test_install_package():
    runner = CliRunner()
    result = runner.invoke(run_application, ['install', 'click'])
    assert result.exit_code == 0


def test_install_package_req():
    runner = CliRunner()
    result = runner.invoke(
        run_application, [
            'install', '-r', 'requirements_test.txt'])
    assert result.exit_code == 0


def test_uninstall_package():
    runner = CliRunner()
    result = runner.invoke(run_application, ['uninstall', 'click'])
    assert result.exit_code == 0


def test_update_package():
    runner = CliRunner()
    result = runner.invoke(run_application, ['install', '-u', 'click'])
    assert result.exit_code == 0
