"""
Contains basic code for creating new projects.
"""
import sys

from project.c_project import C_Project
from project.cpp_project import CPP_Project
from project.ssp_project import SSP_Project


def create_project(name, lang, opt = None):
	"""
	Creates a template project of the specified language with the specified name.
	"""
	#Branch based on language type
	new_project = None
	if lang.lower() in ['c']:
		new_project = C_Project(name)
	elif lang.lower() in ['cpp', 'c++']:
		new_project = CPP_Project(name)
	elif lang.lower() in ['ssp', 'system-script-python']:
		new_project = SSP_Project(name, exec_names = opt)
	#TODO: Add more elifs
	
	if new_project != None:
		new_project.create()
	else:
		print "No available project templates for language '{}'.".format(lang)


def __create_project__(args):
	if len(args) < 3:
		print "Invalid System Arguments."
		print "Please use the sytax:"
		print "new-project [language] [project name] [opt]"
		return
	project_name = args[2]
	project_lang = args[1]
	if len(args) > 3:
		opt = args[3:]
	else:
		opt = None
	create_project(project_name, project_lang, opt)


if __name__ == '__main__':
	__create_project__(sys.argv)
