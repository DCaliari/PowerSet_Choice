from moduli import modulo_functions


def is_localhost(request):
	return modulo_functions.contains(get_full_url(request), 'localhost') or \
			modulo_functions.contains(get_full_url(request), '127.0.0.1')


def is_index(request):
	http_rel_path = request.path
	num_slash = http_rel_path.count('/')
	return num_slash == 2 and http_rel_path.endswith('/')
	

def get_full_url(request):
	return request.build_absolute_uri(request.path)
