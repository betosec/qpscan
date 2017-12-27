#!/usr/bin/python

class utils:
    
    def __init__(self):
        pass

    color = {
      "purple": "\033[95m",
      "purpleBold": "\033[01;95m",
      "cyan": "\033[36m",
      "cyanBold": "\033[01;36m",
      "blue": "\033[94m",
      "blueBold": "\033[01;34m",
      "red": "\033[91m",
      "redBold": "\033[01;31m",
      "green": "\033[92m",
      "greenBold": "\033[01;32m",
      "white": "\033[0m",
      "whiteBold": "\033[01;37m",
      "yellow": "\033[93m",
      "yellowBold": "\033[01;33m"
    }

    #---------------------------------------------------------------------------------------------------------


    def colorTexto(self, tipoMsg, texto):
        self.tipoMsg = tipoMsg
        self.texto = texto

        if self.tipoMsg == 'alerta':    #YELLOW
            self.texto = '\033[1;33m' + self.texto + '\033[1;m' 
            print self.texto
        
        elif self.tipoMsg == 'error':       # RED
            self.texto = '\033[1;31m' + self.texto + '\033[1;m' 
            print self.texto
        
        elif self.tipoMsg == 'info':        # GREEN
            self.texto = '\033[1;32m' + self.texto + '\033[1;m' 
            print self.texto
        
        elif self.tipoMsg == 'debug':       # BLUE
            self.texto = '\033[1;34m' + self.texto + '\033[1;m' 
            print self.texto
        
        elif self.tipoMsg == 'normal':  # WHITE
            self.texto = '\033[1;37m' + self.texto + '\033[1;m' 
            print self.texto

    #------------------------------------------------------------------------------------------------------------

    """
    def ask(self, msg):
        return "\033[1m[?] " + msg + "\033[0m"      #WHITE

    def notice(self, msg):
        return "\n\033[1m[i] " + msg + "\033[0m"    #WHITE

    def critical(self, msg):
        return "\n\033[91m[!] " + msg + "\033[0m"   #RED

    def warning(self, msg):
        return "\033[93m[i] " + msg + "\033[0m"     #YELLOW

    def info(mself, msg):
        return "\033[0m[+] " + msg + "\033[0m"      #WHITE

    def vulnerable(self, msg):
        return "\033[91m[!]" + msg + "\033[0m"      #RED

    def display(self, msg):
        return "\033[0m | " + msg + "\033[0m"       #WHITE
    """

    def purple(self, msg): 
        print "\033[95m" + msg + "\033[0m"

    def purpleBold(self,msg):
        print "\033[01;95m" + msg 

    def cyan (self,msg): 
        print "\033[36m" + msg + "\033[0m"

    def cyanBold (self, msg): 
        print "\033[01;36m" + msg + "\033[0m"

    def blue (self, msg): 
        print "\033[94m" + msg + "\033[0m"

    def blueBold(self, msg): 
        print "\033[01;34m" + msg + "\033[0m"

    def red(self, msg): 
        print "\033[91m" + msg + "\033[0m"

    def redBold(self, msg):
        print "\033[01;31m" + msg + "\033[0m"

    def green(self, msg): 
        print "\033[92m" + msg + "\033[0m"

    def greenBold(self, msg): 
        print "\033[01;32m" + msg + "\033[0m"

    def white(self, msg): 
        print "\033[0m" + msg + "\033[0m"

    def whiteBold(self, msg): 
        print "\033[01;37m" + msg + "\033[0m"

    def yellow(self, msg): 
        print "\033[93m" + msg + "\033[0m"

    def yellowBold(self, msg): 
        print "\033[01;33m" + msg + "\033[0m"
    

    def banner(self):
        msgColor = utils()
        msgColor.green("  [====================================================================================]")
        msgColor.green('  [==]                                                                              [==]')
        msgColor.green('  [==]                                                                              [==]')
        msgColor.green('  [==]                   \033[1;33m.,\033[1;m                                                         \033[92m[==]')
        msgColor.green('  [==]                \033[1;33m,*.\033[1;m                                                           \033[92m[==]')
        msgColor.green('  [==]             \033[1;33m,,,.\033[1;m  \033[1;34m.%,\033[1;m                                                        \033[92m[==]')
        msgColor.green('  [==]           \033[1;33m,,,,\033[1;m  \033[1;34m/##\033[1;m                                                          \033[92m[==]')
        msgColor.green('  [==]          \033[1;33m,.,.\033[1;m \033[1;34m.((/\033[1;m                                                           \033[92m[==]')
        msgColor.green('  [==]         \033[1;33m,,..\033[1;m \033[1;34m.((/\033[1;m   \033[1;31m(,\033[1;m      \033[1;33m,.\033[1;m                                               \033[92m[==]')
        msgColor.green('  [==]         \033[1;33m,,,.\033[1;m \033[1;34m///\033[1;m  \033[1;31m/(.\033[1;m        \033[1;33m,,\033[1;m                                              \033[92m[==]')
        msgColor.green('  [==]        \033[1;33m.,,,\033[1;m \033[1;34m*%/*\033[1;m \033[1;31m//,\033[1;m          \033[1;33m,*\033[1;m    \033[92m _____   _____                           [==]')
        msgColor.green('  [==]        \033[1;33m.,,,\033[1;m \033[1;34m*%%#.\033[1;m\033[1;31m%%\033[1;m           \033[1;33m,,,\033[1;m   \033[92m|  __ \ / ____|                          [==]')
        msgColor.green('  [==]         \033[1;33m,,,,\033[1;m \033[1;34m##%,\033[1;m\033[1;31m%%,\033[1;m          \033[1;33m,,,.\033[1;m  \033[92m| |__) | (___   ___ __ _ _ __            [==]')
        msgColor.green('  [==]          \033[1;33m,,,,\033[1;m\033[1;34m.###\033[1;m\033[1;31m%%%\033[1;m         \033[1;33m.,,..\033[1;m  \033[92m|  ___/ \___ \ / __/ _` | -_ \           [==]')
        msgColor.green('  [==]           \033[1;33m.,,,,\033[1;m\033[1;34m(##\033[1;m\033[1;31m%%%*\033[1;m      \033[1;33m,,,**,\033[1;m  \033[92m| |     ____) | (_| (_| | | | |          [==]')
        msgColor.green('  [==]               \033[1;33m.,,,\033[1;m\033[1;34m/###\033[1;m\033[1;31m%%%%\033[1;m\033[1;33m#(,,***. ,\033[1;m\033[92m|_|    |_____/ \___\__,_|_| |_|          [==]')
        msgColor.green('  [==]                                   \033[1;33m.\033[1;m                                          \033[92m[==] ')
        msgColor.green('  [==]                     Quipux Security Scanner by infoSegura                    [==] ')
        msgColor.green('  [==]                                                                              [==]')
        msgColor.green('  [==]                                                                              [==]')
        msgColor.green('  [====================================================================================]')
        msgColor.green('')
        msgColor.green('')
        msgColor.green('  <+---------------------------------------------------------------------------------+>')
        msgColor.green('                Pruebas de seguridad sobre el Sistema de Gestion Documental')
        msgColor.green('                  Busca documentos de Quipux que no deberian ser publicos             ')
        msgColor.green('  <+---------------------------------------------------------------------------------+>')
        msgColor.green('')
