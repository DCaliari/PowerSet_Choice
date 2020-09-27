from Moduli import modulo_functions


def is_localhost(request):
	return modulo_functions.contains(request.path, 'localhost') or modulo_functions.contains(request.path, '127.0.0.1')