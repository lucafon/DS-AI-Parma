import sys

def check_arguments(arguments):
	if len(arguments) < 2:
		raise Exception('utilizzo: {} nome'.format(arguments[0]))

def main(arguments):
	check_arguments(arguments)
	print('Hello {}'.format(arguments[1]))

if __name__ == '__main__':
	main(sys.argv)
