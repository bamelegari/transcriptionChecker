#!/usr/bin/python

def answerYes():
	ans = raw_input()
	if ans == 'y' or ans == 'Y' or ans == 'yes':
		return True
	elif ans == 'n' or ans == 'N' or ans == 'no':
		return False
	else:
		print("invalid answer...")
		return answerYes()

#arguments alternate between menu names and functions tied to those names
def menu(msg, *args):
	print msg
	for i in range(len(args)):
		if i % 2 == 0:
			print i + ')  ' + args[i]


menu("test", "t1", "t2", "t3", "t4", "t5", "t6")
#menuResponse = raw_input("Select transcript type:\n 	1) Full Verbatim\n 		2) Clean Verbatim")
