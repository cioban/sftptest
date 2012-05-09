#!/usr/bin/env python
#############################################
# Sergio Cioban Filho - 14/02/2011 15:22:10
#############################################
import sys
from time import strftime

queue_status = {
	'QUEUED'		: 0,
	'PROCESSING'	: 1,
	'ERROR'			: 2,
	'OK'			: 3,
	'REMOVED'		: 4,
	'CLOSED'		: 5,
}

def doDebug(msg, type=None, level='INFO'):
	#if ( debug == 1 ):
	if ( type == "MARK" ):
		sys.stdout.write("------------------------------------------------------------\n")
		sys.stdout.flush()
	else:
		timestr = strftime("%d/%m/%Y %H:%M:%S")
		sys.stdout.write("["+timestr+"] --- "+str(msg)+"\n")
		sys.stdout.flush()

	"""
	if ( haveLog == 1 ):
		if ( type == "MARK" ):
			msg="------------------------------------------------------------"

		case = {
			'INFO': logger.info,
			'ERROR': logger.error,
			'WARNING': logger.warning
		}
		case[level](msg)

def doDebug(msg):
	timestr = strftime("%d/%m/%Y %H:%M:%S")
	sys.stdout.write("["+timestr+"] --- "+str(msg)+"\n")
	sys.stdout.flush()

	"""




def printList(List):
	print("# PRINT LIST ################################################################################")
	for dn, data in List.iteritems():
		doDebug("["+dn+"] -"+str(data))

	print("# PRINT LIST ################################################################################\n ")

