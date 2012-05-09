#!/usr/bin/python
#############################################
#
# Libs
from _dutil import *
import paramiko
#############################################

class SFTP:
	def end(self):
		#doDebug(self.TAG+"Desconectando")
		if self.sftp is not None:
			self.sftp.close()
		if self.transport is not None:
			self.transport.close()

	#def __del__(self):
	#	doDebug("DESTROY SFTP CONN")

	def __init__(self, host, port, user, passwd, TAG=''):
		self.transport = None
		self.sftp	  = None
		self.TAG	  = TAG

		try:
			#doDebug(TAG+"Conectando no servidor: "+host)
			self.transport = paramiko.Transport((host, port))
		except Exception, e:
			raise Exception('Erro: '+str(e))

		try:
			#doDebug(TAG+"Realizando autenticacao user["+user+"] pass["+passwd+"]")
			self.transport.connect(username=user, password=passwd)
		except Exception, e:
			self.end()
			raise Exception('Erro: '+str(e))

		try:
			#doDebug(TAG+"Criando o cliente SFTP")
			self.sftp = paramiko.SFTPClient.from_transport(self.transport)
		except Exception, e:
			self.end()
			raise Exception('Erro: '+str(e))

################################################################################
