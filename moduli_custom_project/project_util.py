import os

from PowerSet import settings
from moduli import modulo_django
from moduli.rete import modulo_networking

FULLPATH_DATABASE = os.path.join(settings.BASE_DIR, 'databases', "RecordPowerset.db")

FULLPATH_CARTELLA_STATIC = settings.STATICFILES_DIRS[0]
CARTELLA_FAVICONS = 'favicons'
FULLPATH_CARTELLA_IMG = os.path.join(FULLPATH_CARTELLA_STATIC, 'images')
FULLPATH_CARTELLA_IMG_CQ = os.path.join(FULLPATH_CARTELLA_IMG, 'images_cq')
FULLPATH_CARTELLA_IMG_CHOICE = os.path.join(FULLPATH_CARTELLA_IMG, 'images_choice')
FULLPATH_CARTELLA_IMG_BIBITE = os.path.join(FULLPATH_CARTELLA_IMG, 'images_bibite')
FULLPATH_CARTELLA_IMG_SNACK = os.path.join(FULLPATH_CARTELLA_IMG, 'images_snack')
FULLPATH_CARTELLA_IMG_NUMBERS = os.path.join(FULLPATH_CARTELLA_IMG, 'numbers')
FULLPATH_CARTELLA_IMG_DICES = os.path.join(FULLPATH_CARTELLA_IMG, 'dices')
FULLPATH_CARTELLA_IMG_SHAPES = os.path.join(FULLPATH_CARTELLA_IMG, 'shapes')
FULLPATH_CARTELLA_IMG_PENCILS = os.path.join(FULLPATH_CARTELLA_IMG, 'pencils')

FULLPATH_CARTELLA_IMG_LANGUAGE = os.path.join(FULLPATH_CARTELLA_IMG, 'language_images')
FULLPATH_CARTELLA_IMG_L1 = os.path.join(FULLPATH_CARTELLA_IMG_LANGUAGE, 'Language_0')
FULLPATH_CARTELLA_IMG_L2 = os.path.join(FULLPATH_CARTELLA_IMG_LANGUAGE, 'Language_1')
FULLPATH_CARTELLA_IMG_L3 = os.path.join(FULLPATH_CARTELLA_IMG_LANGUAGE, 'Language_2')
FULLPATH_CARTELLA_IMG_L4 = os.path.join(FULLPATH_CARTELLA_IMG_LANGUAGE, 'Language_3')
FULLPATH_CARTELLA_IMG_L5 = os.path.join(FULLPATH_CARTELLA_IMG_LANGUAGE, 'Language_4')
FULLPATH_CARTELLA_IMG_L6 = os.path.join(FULLPATH_CARTELLA_IMG_LANGUAGE, 'Language_5')
FULLPATH_CARTELLA_IMG_L7 = os.path.join(FULLPATH_CARTELLA_IMG_LANGUAGE, 'Language_6')


CARTELLA_VIDEO = "videos"

URL_FILE_STATICI_ESTERNI = 'http://' + modulo_networking.get_ip()
URL_VIDEO = URL_FILE_STATICI_ESTERNI + '/' + CARTELLA_VIDEO

# THIS CONSTANT DEALS WITH THE ID_UTENTE RECORD IN ANY SESSION. SEE VIEWS.PY.
SESSION_KEY__ID_UTENTE = 'id_utente'

SESSION_KEY__PHASE = 'phase'

SESSION_KEY__CHOICE_LAST_PAGE = 'choice_last_page'

SESSION_KEY__POWERSET = 'powerset'
SESSION_KEY__IMAGESCQ = 'images_cq'
SESSION_KEY__IMAGES2 = 'images2'
SESSION_KEY__IMAGES3 = 'images3'


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

