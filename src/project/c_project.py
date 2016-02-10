"""
Functions for setting up a project in C
"""
#TODO: make supertype and improve organization
import os, shutil
import os.path as pth


IGNORE_EXTENSIONS = ['*.o', '*.out', 'exe', '*~']
TEMPLATE_DIR = pth.join(pth.dirname(pth.realpath(__file__)), "c_templates")

class C_Project(object):
	"""
	Basic object for a C project
	"""
	
	def __init__(self, name):
		self.name = name
	
	
	def create(self):
		"""
		Creates Template Files.
		Assumes that we are already in the relevant directory
		"""
		#first make directory structure
		rootdir = self.name
		os.mkdir(rootdir)
		os.chdir(rootdir)
		os.mkdir("bin")
		os.mkdir("src")
		
		#make gitignore files
		with open(".gitignore", 'w') as gitignore_file:
			for rule in IGNORE_EXTENSIONS:
				gitignore_file.write("{}\n".format(rule))
		with open("bin/.gitignore", 'w') as gitignore_file:
			gitignore_file.write("!.gitignore")
		
		#copy makefile template
		makefile_template = os.path.join(TEMPLATE_DIR, 'Makefile')
		shutil.copyfile(makefile_template, 'Makefile')
		
		#copy main.c template
		main_template = os.path.join(TEMPLATE_DIR, 'main.c')
		shutil.copyfile(main_template, 'src/main.c')
		
