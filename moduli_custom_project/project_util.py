import os

from PowerSet import settings
from moduli import modulo_django
from moduli.rete import modulo_networking


FULLPATH_DATABASE = os.path.join(settings.BASE_DIR, 'databases', "RecordPowerset.db")

FULLPATH_CARTELLA_STATIC = settings.STATICFILES_DIRS[0]
CARTELLA_FAVICONS = 'favicons'
FULLPATH_CARTELLA_IMG = os.path.join(FULLPATH_CARTELLA_STATIC, 'images')
FULLPATH_CARTELLA_IMG_CHOICE = os.path.join(FULLPATH_CARTELLA_IMG, 'images_choice')

CARTELLA_VIDEO = "video"

URL_FILE_STATICI_ESTERNI = 'http://' + modulo_networking.get_ip()
URL_VIDEO = URL_FILE_STATICI_ESTERNI + '/' + CARTELLA_VIDEO

# THIS CONSTANT DEALS WITH THE ID_UTENTE RECORD IN ANY SESSION. SEE VIEWS.PY.
SESSION_KEY__ID_UTENTE = 'id_utente'

SESSION_KEY__CHOICE_LAST_PAGE = 'choice_last_page'


def init_modelmap(request, app_title, app_logo, formBean):
	model_map = {
		'is_localhost': modulo_django.is_localhost(request),
		'is_index': modulo_django.is_index(request),
		'app_title': app_title,
		'app_logo': app_logo
	}
	if formBean is not None:
		model_map['formBean'] = formBean
	return model_map


def from_tipo_test_to_cartella_immagini(tipo_test):
	if tipo_test == 0:
		return "images_choice"
	if tipo_test == 1:
		return "images_bibite"
	if tipo_test == 2:
		return "images_snack"
	return None

