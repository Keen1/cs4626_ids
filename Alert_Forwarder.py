#!/usr/bin/python3

import socket
import sys
import argparse
import os
import ctypes
from snort import Alertpkt
from scapy.all import *
#constant socket path
S_PATH = "/var/log/snort/snort_alert"
ALERT_MSG_LEN = 256
SNAP_LEN = 1514


def get_socket(path):
	#create the socket
	srv_sock = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)
	#verify new socket?
	try:
		os.remove(path)
		print(f"Path {path} removed.") 
	except OSError:
		pass
	#bind to path
	try:
		srv_sock.bind(path)
		print(f"Bind on {path} successful.")
		
	except OSError:
		print(f"error. unable to find to {path}")
		sys.exit(1)
	#return the socket binded to path
	return srv_sock

#validate that the path for the socket exists
def validate_socket(path):
	if not os.path.exists(path):
		return False
	
	return True
	
if __name__ == "__main__":
	
	sock = get_socket(S_PATH)
	alert = Alertpkt()
	
	try:
		while True:
			if sock.recv_into(alert) != ctypes.sizeof(alert):
				break
			print("{:3d} {:%H:%M:%S}".format(alert.val, datetime.fromtimestamp(alert.data)))
	except KeyboardInterrupt:
		pass
	finally:
		sock.close()
	
		
		
		
	
	
	
		