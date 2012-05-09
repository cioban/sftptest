#!/usr/bin/env python
# -*- encoding: utf-8 -*-
#############################################
# Sergio Cioban Filho - 05/08/2011 07:13:23 AM
#############################################
from optparse import OptionParser, OptionGroup

class CFG:
	def __init__(self):
		global args
		usage = "%prog --destinattion=HOST --instances=NUMBER --destination=IP --username=USER --password=PASS""\nATENCAO: Este software nao faz a validacao dos dados informados, entao, seja inteligente e nao faca besteiras... ;)"
		parser = OptionParser(usage=usage, version="%prog 1.0")
		parser.add_option("-i", "--instances", type="int", help="Define o numero de instancias SFTP que serao executadas")
		parser.add_option("-d", "--destination", help="Endereco IP: define o endereco de IP do servidor SFTP Ex.: 192.166.100.1")
		parser.add_option("-u", "--username", help="USER: username")
		parser.add_option("-p", "--password", help="PASS: password")
		parser.add_option("-v", "--verbose", action="store_true", default=False, help="Ativa debugna tela")

		#group = OptionGroup(parser, "Opcoes de Debug")
		#group.add_option("-d", "--debug", action="store_true", dest="set_debug", default=False, help="Ativa debug na tela (O mesmo LG que vai para o arquivo)")
		#group.add_option("-l", "--log", action="store_true", dest="set_log", default=False, help="Ativa LOG no arquivo /axs/traces/ipsecadm.trace")
		#parser.add_option_group(group)


		(options, args) = parser.parse_args()

		#if options.set_master and options.set_slave:
		#	parser.error("Nao se pode usar --master e --slave ao mesmo tempo")
		if not options.destination:
			parser.error("Informe o IP do servidor SFTP. --destination=IP")
		if not options.instances or options.instances < 1:
			parser.error("Informe um numero valido de instancias. --instances=NUMBER")
		if not options.username:
			parser.error("Informe um usuário. --username=teste")
		if not options.password:
			parser.error("Informe a senha do usuario. --password=teste")
		self.options = options


	def getOptions(self):
		return self.options

