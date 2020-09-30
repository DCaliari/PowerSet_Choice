from Moduli import modulo_django

QUESTIONNAIRE_LEFT = [
	'...is messy'
]

QUESTIONNAIRE_RIGHT = [
	'...is neat'
]

QUESTIONNAIRE_INTENSITY = 10

IMAGES = [
	'apple.jpg',
	'ice-cream.jpg',
	'pear.jpg',
	'pizza.jpeg'
]

SHAPES = [
	'Cerchio.png',
	'Quadrato.png',
	'Triangolo.png'
]

# THIS CONSTANT DEALS WITH THE ID_UTENTE RECORD IN ANY SESSION. SEE VIEWS.PY.
SESSION_KEY__ID_UTENTE = 'id_utente'


def init_modelmap(request):
	model_map = {
		'is_localhost': modulo_django.is_localhost(request),
		'is_index': modulo_django.is_index(request)
	}
	return model_map

