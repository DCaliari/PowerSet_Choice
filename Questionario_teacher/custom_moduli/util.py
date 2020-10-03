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


def init_modelmap(request):
	model_map = {
		'is_localhost': modulo_django.is_localhost(request),
		'is_index': modulo_django.is_index(request)
	}
	return model_map

