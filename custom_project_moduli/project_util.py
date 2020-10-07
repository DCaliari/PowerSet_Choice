import os

from PowerSet import settings
from Moduli import modulo_django

CARTELLA_DATABASE = 'databases'

FULLPATH_DB_CHOICE = os.path.join(settings.BASE_DIR, CARTELLA_DATABASE, "RecordChoice.db")
FULLPATH_DB_QUESTION_TEACHER = os.path.join(settings.BASE_DIR, CARTELLA_DATABASE, "RecordQuestionTeacher.db")

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

