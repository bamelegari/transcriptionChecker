#!/usr/bin/python

import sys

def answerYes():
	ans = raw_input()
	if ans == 'y' or ans == 'Y' or ans == 'yes':
		return True
	elif ans == 'n' or ans == 'N' or ans == 'no':
		return False
	else:
		print "invalid answer..."
		return answerYes()

def isInt(c):
	try:
		int(c)
		return True
	except ValueError:
		return False

#arguments alternate between menu names and functions tied to those names
def menu(msg, *args):
	print '\n' + msg + '\n'
	count = 1
	for i in range(len(args)):
		if i % 2 == 0:
			print str(count) + ')  ' + args[i]
			count += 1
	choice = raw_input()
	if isInt(choice):
		choice = int(choice)
		if choice > 0 and choice <= len(args) / 2:
			args[int(choice) * 2 - 1](sys.argv[1])
			return

	print "invalid answer..."
	menu(msg, *args)


def fullVerbatim(infile=''):
	print "full Verbatim called with " + infile


def cleanVerbatim(infile=''):
	print "clean verbatim called with " + infile




menu("Select a transcription type", "Full Verbatim", fullVerbatim, "Clean Verbatim", cleanVerbatim)

#menuResponse = raw_input("Select transcript type:\n 	1) Full Verbatim\n 		2) Clean Verbatim")
