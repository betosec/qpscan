#!/usr/bin/python

class colorTexto:
	
	def __init__(self, tipoMsg, texto):
		
		self.tipoMsg = tipoMsg
		self.texto = texto

		if self.tipoMsg == 'alerta':	#YELLOW
			self.texto = '\033[1;33m' + self.texto + '\033[1;m' 
			print self.texto
		
		elif self.tipoMsg == 'error':		# RED
			self.texto = '\033[1;31m' + self.texto + '\033[1;m' 
			print self.texto
		
		elif self.tipoMsg == 'info':		# GREEN
			self.texto = '\033[1;32m' + self.texto + '\033[1;m' 
			print self.texto
		
		elif self.tipoMsg == 'debug':		# BLUE
			self.texto = '\033[1;34m' + self.texto + '\033[1;m' 
			print self.texto
		
		elif self.tipoMsg == 'normal':	# WHITE
			self.texto = '\033[1;37m' + self.texto + '\033[1;m' 
			print self.texto

