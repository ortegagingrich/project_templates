import sys


#Individual Command methods{0}


def main(args):
	if len(args) < 2:
		print 'Invalid arguments: no command specified.'
		exit(1)
	
	#Branch to call the correct function for the specified command{1}
	
	print 'Invalid arguments: %s is not a valid command.' % args[1]
	exit(1)


if __name__ == '__main__':
	main(sys.argv)
