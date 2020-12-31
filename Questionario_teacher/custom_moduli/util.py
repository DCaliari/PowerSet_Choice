import os

from moduli_custom_project import project_util

APP_TITLE = 'Questionario'
APP_LOGO = os.path.join(project_util.CARTELLA_FAVICONS, 'favicon_questionario.png')

TEMPLATE_NAME__INDEX = 'index.html'
TEMPLATE_NAME__QUESTIONARIO_TEACHER = 'questionnaire_teacher.html'
TEMPLATE_NAME__NUMERO_ALUNNI = 'numero_alunni.html'
TEMPLATE_NAME__FINAL_PAGE = 'final_page.html'


QUESTIONNAIRE = [
	['...interagisce molto', '...molto silenzioso'],
	['...molto disordinato', '...molto preciso'],
	['...molto sereno', '...molto irritabile'],
	['...molto disinteressato', '...molto curioso di apprendere'],
	['...molto sicuro di se`', '...molto insicuro'],
	['...molto introverso', '...molto estroverso'],
	['...molto focalizzato', '...molto distratto'],
	['...molto disobbediente', '...molto obbediente'],
	['...apprende rapidamente', '...e` lento ad apprendere'],
	['...molto timido', '...molto incosciente']
]

QUESTIONNAIRE_INTENSITY = 10


def init_modelmap(request, formBean):
	return project_util.init_modelmap(request, APP_TITLE, APP_LOGO, formBean)
