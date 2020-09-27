from Moduli import modulo_django

IMAGES = [
	'apple.jpg',
	'ice-cream.jpg',
	'pear.jpg',
	'pizza.jpeg'
]

# THIS CONSTANT DEALS WITH THE ID_UTENTE RECORD IN ANY SESSION. SEE VIEWS.PY.
SESSION_KEY__ID_UTENTE = 'id_utente'


def init_modelmap(request):
	model_map = {
		'is_localhost': modulo_django.is_localhost(request)
	}
	return model_map
