""" Install Script """
import sys, os, shutil

import git

from meta import *


def __install__():
	"""
	Runs the actual installation process.
	"""
	print "Preparing to install {} script.".format(SCRIPT_NAME)
	
	#make sure git is fine
	if not __git_status__():
		print "Cannot Install.  There are uncommitted changes."
		sys.exit(1)
	
	#make sure there is a place to install the script to.
	if not "SCRIPTS" in os.environ:
		print "Please set SCRIPTS environment variable."
		sys.exit(1)
	
	script_dir = os.environ["SCRIPTS"]
	
	#check to see if already installed
	if __is_already_installed__(script_dir):
		print "A version of {} is already installed.".format(SCRIPT_NAME)
		print "Do you wish to overwrite it? [Y,n]"
		if raw_input() != 'Y':
			print "Cancelling installation of {}.".format(SCRIPT_NAME)
			sys.exit(0)
		else:
			print "Overwritting previously installed script {}.".format(SCRIPT_NAME)
			__uninstall__()
	
	#copy python sources into script directory
	new_dir = os.path.join(script_dir, SCRIPT_NAME)
	shutil.copytree("src", new_dir)
	
	#copy executable and add permissions
	os.system("sudo cp bin/{0} /bin/{0}".format(EXEC_NAME))
	os.system("sudo chmod +x /bin/{}".format(EXEC_NAME))
	


def __uninstall__():
	"""
	Removes Python sources from the script directory and removes the executable
	from /bin/.
	"""
	if not "SCRIPTS" in os.environ:
		print "Please set SCRIPTS environment variable."
		sys.exit(1)
	
	script_dir = os.environ["SCRIPTS"]
	
	if SCRIPT_NAME in os.listdir(script_dir):
		shutil.rmtree(os.path.join(script_dir, SCRIPT_NAME))
	if EXEC_NAME in os.listdir("/bin/"):
		os.system("sudo rm -f /bin/{}".format(EXEC_NAME))


def __is_already_installed__(script_dir):
	"""Checks to see if there is a version already installed"""
	#first check the bin folder
	if SCRIPT_NAME in os.listdir(script_dir):
		return True
	if EXEC_NAME in os.listdir("/bin/"):
		return True
	
	return False


def __git_status__():
	"""
	Checks to see if there are uncommitted changes.
	"""
	#TODO: For now, just always returns true.
	
	return True


if __name__ == '__main__':
	if(len(sys.argv) < 2):
		print "Please specify a setup command.  (e.g. 'install' or 'uninstall'"
	cmd = sys.argv[1]
	
	if cmd == 'install':
		__install__()
	elif cmd == 'uninstall':
		__uninstall__()
	else:
		print "Setup command '{}' not recognized.".format(cmd)
	
