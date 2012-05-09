#!/usr/bin/env python
#############################################
# Sergio Cioban Filho - 05/08/2011 21:22:10
#############################################
from threading import Timer, Thread
from time import sleep
from os import path
import os
import sys
from time import sleep
from time import strftime


# Bibliotecas locais
from _dutil import *
from _config import CFG
from _sftp import *



#############################################






def testSftp(threadId):
	TAG = '[THREAD_SFTP: '+str(threadId)+' ] '
	doDebug(TAG+'Nova thread instanciada')
	while True:
		global threadList
		global options
		global total_curr

		#doDebug(TAG,"MARK")
		sftp_conn = None
		data = threadList[threadId]
		couters = data[0]

		if data[1] == queue_status['REMOVED']:
			doDebug(TAG+'Thread marcada como REMOVED. Saindo...')
			del threadList[threadId]
			break

		try:
			total_curr = total_curr + 1
			couters['tries'] = couters['tries'] + 1
			if options.verbose: doDebug(TAG+'==== THREAD: '+str(threadId))
			#sftp_conn = SFTP(options.destination,22,options.username,options.password,TAG)
			sftp_conn = SFTP(options.destination,443,options.username,options.password,TAG)
			if options.verbose: doDebug(TAG+'==== Aguardando tempo de teste')
			if len(threadList) != options.instances:
				sleep(2)
			else:
				sleep(5)
			sftp_conn.end()
			del sftp_conn

			total_curr = total_curr - 1


		except Exception, e:
			doDebug(TAG+'ERRO: '+str(e))
			total_curr = total_curr - 1
			couters['errors'] = couters['errors'] + 1
			if sftp_conn is not None:
				sftp_conn.end()
				del sftp_conn

		sleep(1)
	return




def sftpLoop(instances):
	aux = 0
	while aux != instances:
		if not aux in threadList:
			threadList[aux] = [ {'tries': 0, 'errors': 0 }, queue_status['PROCESSING'] ]
			thread = Thread( target=testSftp, args = ( aux, ))
			thread.daemon=True
			thread.start()
			sleep(0.3)
		aux = aux + 1




def getInfo():
	global total_tries
	global total_errors
	total_tries = 0
	total_errors = 0

	for threadId, data in threadList.iteritems():
		counters = data[0]
		total_tries = total_tries + counters['tries']
		total_errors = total_errors + counters['errors']

	return [total_tries, total_errors]


def showInfo():
	global total_curr
	counters = getInfo()
	doDebug('### Threads: '+str(options.instances)+' - Current Conn: '+str(total_curr)+' - Total conn: '+str(counters[0])+' - Total errors: '+str(counters[1]))



def safe_kill():
	global threadList
	global options
	doDebug('### Solicitacao de encerramento')
	counters = getInfo()

	for threadId, data in threadList.iteritems():
		old_counters = data[0]
		status = queue_status['REMOVED']
		threadList[threadId] = [old_counters, status]
		status = threadList[threadId][1]
		doDebug('### Aguardando o encerrando da thread: '+str(threadId))


	sleep(5)
	timeout = 20
	while len(threadList) != 0:
		sleep(1)
		timeout = timeout - 1
		if timeout <= 0:
			doDebug('### Estouro de timeout. Encerrando...')
			break

	doDebug('### Todas as threads sairam... Encerrando ;) ')
	doDebug('\n### Informacoes finais:')
	doDebug('### Threads: '+str(options.instances)+' - Total conn: '+str(counters[0])+' - Total errors: '+str(counters[1]))

	sys.exit(1)




if __name__ == "__main__":
	threadList	= {}
	options = None
	total_tries = 0
	total_errors = 0
	total_curr = 0

	config = CFG()
	options = config.getOptions()
	sys.stdout.write("#############################################\n")
	sys.stdout.write("# SFTPTEST INIT\n")
	sys.stdout.write("#############################################\n")

	try:
		while True:
			sftpLoop(options.instances)
			sleep(10)
			showInfo()

	except KeyboardInterrupt:
		safe_kill()
	except Exception,e:
		print "---", str(e),  "---"
		sys.exit(1)




