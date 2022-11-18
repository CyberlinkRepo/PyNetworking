'''
FTPServer by: JOR
Listen for FTP access on every interface

Alpha: 13FEB22
'''

from pyftpdlib import servers
from pyftpdlib.handlers import FTPHandler
# Open on every IP address, port 21
address = ("0.0.0.0", 21)  
server = servers.FTPServer(address, FTPHandler)
server.serve_forever()