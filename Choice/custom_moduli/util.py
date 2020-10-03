import os

from Moduli import modulo_django
from PowerSet import settings


FULLPATH_DB = os.path.join(settings.BASE_DIR, "RecordChoice.db")

QUESTIONNAIRE = [
	['...is rather talkative', '...is rather quiet'],
	['...is messy', '...is neat'],
	['...is good-natured', '...is irritable'],
	['...is disinterested', '...is curious to learn'],
	['...is self-confident', '...is insecure'],
	['...is withdrawn', '...is outgoing'],
	['...is focused', '...easily distracted'],
	['...is disobedient', '...is obedient'],
	['...is quick at learning new things', '...needs more time'],
	['...is timid', '...is fearless']
]

QUESTIONNAIRE_INTENSITY = 10

IMAGES = [
	'apple.jpg',
	'ice-cream.jpg',
	'pear.jpg',
	'pizza.jpeg'
]

IMAGES2 = [
	'coca.jpg',
	'fanta.jpg',
	'the.jpg',
	'acqua.jpeg'
]

IMAGES3 = [
	'coca.jpg',
	'fanta.jpg',
	'the.jpg',
	'acqua.jpeg'
]

NUMBERS = [
	'Zero.png',
	'Uno.png',
	'Due.png',
	'Tre.png',
	'Quattro.png',
	'Cinque.png',
	'Sei.png',
	'Sette.png',
	'Otto.png',
	'Nove.png'
]

DICES = [
	'One.png',
	'Two.png',
	'Three.png',
	'Four.png',
	'Five.png',
	'Six.png'
]

SHAPES = [
	'Cerchio.png',
	'Quadrato.png',
	'Triangolo.png'
]

PENCILS = [
	'Matita1.png',
	'Matita2.png'
]

VIDEOS = [
	'Video1.mp4',
	'Video2.mp4',
	'Video3.mp4',
	'Video4.mp4',
	'Video5.mp4',
	'Video6.mp4',
	'Video7.mp4',
	'Video8.mp4',
	'Video9.mp4',
	'Video10.mp4',
	'Video11.mp4',
	'Video12.mp4',
	'Video13.mp4'
]

# THIS CONSTANT DEALS WITH THE ID_UTENTE RECORD IN ANY SESSION. SEE VIEWS.PY.
SESSION_KEY__ID_UTENTE = 'id_utente'


def init_modelmap(request):
	model_map = {
		'is_localhost': modulo_django.is_localhost(request),
		'is_index': modulo_django.is_index(request)
	}
	return model_map

