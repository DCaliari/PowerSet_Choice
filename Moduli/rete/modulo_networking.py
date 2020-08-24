import socket


# this function get the ip from the compute hardware and therefore avoid to modify settings.py everytime the ip changes
# nonetheless, the server from command prompt has to run with the correct ip

def get_ip():
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	# doesn't even have to be reachable
	try:
		s.connect(('10.255.255.255', 1))
		ip = s.getsockname()[0]
	except Exception:
		ip = None
	finally:
		s.close()
	return ip
