import os

from moduli_custom_project import project_util

APP_TITLE = 'Questionario'
APP_LOGO = os.path.join(project_util.CARTELLA_FAVICONS, 'favicon_questionario.png')

TEMPLATE_NAME__INDEX = 'index.html'
TEMPLATE_NAME__QUESTIONARIO_TEACHER = 'questionnaire_teacher.html'
TEMPLATE_NAME__NUMERO_ALUNNI = 'numero_alunni.html'
TEMPLATE_NAME__FINAL_PAGE = 'fine.html'#TODO: rinominare in final_page


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


def init_modelmap(request, formBean):
	return project_util.init_modelmap(request, APP_TITLE, APP_LOGO, formBean)
