from click.testing import CliRunner
from pkg_scripts.main import run_application

def test_activate_env():
    runner = CliRunner()
    result = runner.invoke(run_application,['activate'])
    assert 'Environment Activated' in result.output 
    assert result.exit_code == 0

def test_install_package():
	runner = CliRunner()
	result = runner.invoke(run_application,['install','click'])
	assert result.exit_code == 0

def test_install_package_req():
	runner = CliRunner()
	result = runner.invoke(run_application,['install','-r', 'requirements_test.txt'])
	assert result.exit_code == 0
 
def test_uninstall_package():
    runner = CliRunner()
    result = runner.invoke(run_application,['uninstall', 'click'])
    assert result.exit_code == 0
    
def test_update_package():
    runner = CliRunner()
    result = runner.invoke(run_application,['install','-u', 'click'])
    assert result.exit_code == 0
    
def test_deactivate():
    runner = CliRunner()
    result = runner.invoke(run_application,['deactivate'])
    assert 'Environment Deactivated' in result.output
    assert result.exit_code == 0
    assert 'No active environments' in result.output