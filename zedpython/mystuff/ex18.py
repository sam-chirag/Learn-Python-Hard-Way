def two_argv(*argv):
	first, second = argv
	print " Values are %r % r" %(first, second)
	
def two_argv_again(argv1, argv2):
	first = argv1
	second = argv2
	print " Values are %r % r" %(first, second)

	
def no_argv():
	print " I got nothing"
	
def one_argv(argv):
	print " I am only one %r" %argv

two_argv("Sam", "Shekhar")
two_argv_again("Sam", "Shekhar")
no_argv()
one_argv("Shekhar")	
	