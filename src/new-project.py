"""
Contains basic code for creating new projects.
"""
import sys

from project.c_project import C_Project


def create_project(name, lang):
	"""
	Creates a template project of the specified language with the specified name.
	"""
	#Branch based on language type
	new_project = None
	if lang in ['c', 'C']:
		new_project = C_Project(name)
	#TODO: Add elifs
	
	if new_project != None:
		new_project.create()
	else:
		print "No available project templates for language '{}'.".format(lang)


def __create_project__(args):
	if len(args) != 3:
		print "Invalid System Arguments."
		print "Please use the sytax:"
		print "new-project [language] [project name]"
		return
	project_name = args[2]
	project_lang = args[1]
	create_project(project_name, project_lang)


if __name__ == '__main__':
	__create_project__(sys.argv)
