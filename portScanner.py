"""
TCP Port Scanner with general OS detection and
banner grabbing.
By: Michael Cosmadelis
"""
import socket
import sys
import subprocess

def main():
	try:
		ip = sys.argv[1]
		lport = int(sys.argv[2])
		uport = int(sys.argv[3])
		pingResult = subprocess.check_output("ping -c 1 %s" % ip, shell=True)

		if "ttl=128" in pingResult:
			print "Target is running Windows."
		elif "ttl=64" in pingResult:
			print "Target is running Linux."
		elif "ttl=255" in pingResult:
			print "Target is running BSD."


		for port in range(lport, uport):
			try:
				s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
				s.settimeout(1) #socket times out after 1 second

				result = s.connect((ip, port))
					if result == 0:
						print "Port %i is open on %s" % (port ,ip)
				banner = s.recv(4096)
				if not banner == "":
					print"\t%s" % banner
				s.close()

			except socket.error:
				print "Port %i is closed on %s" % (port, ip)

			except socket.timeout:
				print "Port %i is filtered on %s" % (port, ip)
				
			except KeyboardInterrupt:
				print "Scan stopped."
						sys.exit()
	except (NameError, IndexError) as e:
		print "Usage: python banner.py [ip] [start port] [end port]"

if __name__ == '__main__':
	sys.exit(main())