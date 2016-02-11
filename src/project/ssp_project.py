"""
Profile for projects involving scripts which live in /bin/ that call python
code.
"""
import os, shutil
import os.path as pth


IGNORE_EXTENSIONS = ['*.pyc', '*~']
TEMPLATE_DIR = pth.join(pth.dirname(pth.realpath(__file__)), "ssp_templates")

class SSP_Project(object):
	"""
	Basic object for a python/shell scripting project
	"""
	
	def __init__(self, script_name, exec_names = None):
		"""
		script_name: the name of the script project
		exec_names: a list of names of commands.  If none are provided, use
					one executable with the same name as the project
		"""
		self.name = script_name
		if exec_names == None:
			self.exec_names = [script_name.lower(),]
		else:
			self.exec_names = exec_names
	
	
	def create(self):
		"""
		Creates the template project in the current directory.
		"""
		
		#first make directory structure
		rootdir = self.name
		os.mkdir(rootdir)
		os.chdir(rootdir)
		print "Creating SSP project in {}.".format(os.getcwd())
		
		os.mkdir("bin")
		os.mkdir("src")
		os.mkdir("test-dir")
		
		#gitignore files
		with open(".gitignore", 'w') as gitignore_file:
			for rule in IGNORE_EXTENSIONS:
				gitignore_file.write("{}\n".format(rule))
		with open("test-dir/.gitignore", 'w') as gitignore_file:
			gitignore_file.write("!.gitignore\n*/")
		
		#meta-info file
		with open("meta.py", 'w') as meta_file:
			meta_file.write('SCRIPT_NAME = "{}"\n'.format(self.name))
			meta_file.write('EXEC_NAMES = [')
			for name in self.exec_names:
				meta_file.write('"{}",'.format(name))
			meta_file.write(']\n')
		
		#setup script
		setup_template = os.path.join(TEMPLATE_DIR, 'setup.py')
		shutil.copyfile(setup_template, 'setup.py')
		
		#makefile
		makefile_template = os.path.join(TEMPLATE_DIR, 'Makefile')
		with open(makefile_template, 'r') as template:
			file_string = template.read().format(self.exec_names[0])
			with open("Makefile", 'w') as makefile:
				makefile.write(file_string)
		
		#main python file
		main_template = os.path.join(TEMPLATE_DIR, 'main.py')
		
		#function inserts
		functions = '\n'
		for command in self.exec_names:
			modcommand = command.replace('-', '_')
			newfunction = "def __command_{}__():\n\tpass\n\n".format(modcommand)
			functions = "{}\n{}".format(functions, newfunction)
		
		#branch inserts
		n = self.exec_names[0]
		nm = n.replace('-', '_')
		com = '__()\n\t\treturn\n'
		branches = "\n\tif args[1] == '{0}':\n\t\t__command_{2}{1}".format(n, com, nm)
		for i in range(1, len(self.exec_names)):
			n = self.exec_names[i]
			nm = n.replace('-', '_')
			ef = "\telif args[1] == '{0}':\n\t\t__command_{2}{1}".format(n, com, nm)
			branches += ef
		
		
		with open(main_template, 'r') as template:
			file_string = template.read()
			#inserts
			file_string = file_string.format(functions, branches)
			
			with open("src/main.py", 'w') as outfile:
				outfile.write(file_string)
		
		#bin scripts
		script_template = os.path.join(TEMPLATE_DIR, 'script')
		with open(script_template, 'r') as template:
			file_string = template.read()
			
			#make files for each command
			for command in self.exec_names:
				outname = os.path.join("bin", command)
				with open(outname, 'w') as outfile:
					out_string = file_string.format(command, self.name)
					outfile.write(out_string)
			

