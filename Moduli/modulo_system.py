import os
import subprocess


def dimensione_file(nomefile):
	try:
		statinfo = os.stat(nomefile)
		return statinfo.st_size
	except:
		return -1
