import os

from PowerSet import settings
from moduli import modulo_django

CARTELLA_DATABASE = 'databases'
CARTELLA_FAVICONS = 'favicons'

FULLPATH_DB_POWERSET = os.path.join(settings.BASE_DIR, CARTELLA_DATABASE, "RecordPowerset.db")

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

def from_tipo_test_to_cartella_immagini(tipo_test):
	if tipo_test == 0:
		return "images_choice"
	if tipo_test == 1:
		return "images_bibite"
	if tipo_test == 2:
		return "images_snack"
	return None