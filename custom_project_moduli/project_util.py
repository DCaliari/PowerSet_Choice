import os

from PowerSet import settings
from Moduli import modulo_django

FULLPATH_DB = os.path.join(settings.BASE_DIR, "RecordChoice.db")

# THIS CONSTANT DEALS WITH THE ID_UTENTE RECORD IN ANY SESSION. SEE VIEWS.PY.
SESSION_KEY__ID_UTENTE = 'id_utente'


def init_modelmap(request, app_title, app_logo):
	model_map = {
		'is_localhost': modulo_django.is_localhost(request),
		'is_index': modulo_django.is_index(request),
		'app_title': app_title,
		'app_logo': app_logo
	}
	return model_map

