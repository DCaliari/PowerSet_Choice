import os

from moduli_custom_project import project_util

APP_TITLE = 'Esperimento'
APP_LOGO = os.path.join(project_util.CARTELLA_FAVICONS, 'favicon_choice.png')

TEMPLATE_NAME__INDEX = 'index.html'
TEMPLATE_NAME__QUESTIONARIO_KIDS = 'questionnaire_kids.html'
TEMPLATE_NAME__VIDEO = 'video.html'
TEMPLATE_NAME__CHOICE = 'choice_image.html'
TEMPLATE_NAME__SLIDER = 'slider.html'
TEMPLATE_NAME__SLIDER2 = 'slider2.html'
TEMPLATE_NAME__LOGIC_TEST = 'logic_test.html'
TEMPLATE_NAME__FINAL_PAGE = 'final_page_C.html'

IMAGES_CHOICE = os.listdir(project_util.FULLPATH_CARTELLA_IMG_CHOICE)
IMAGES_CHOICE2 = os.listdir(project_util.FULLPATH_CARTELLA_IMG_BIBITE)
IMAGES_CHOICE3 = os.listdir(project_util.FULLPATH_CARTELLA_IMG_SNACK)

# This piece of code is for numerical and language tests
# TEMPLATE_NAME__NUMERICAL_TEST = 'numerical_test.html'
# PAGES_NUMERICAL_TEST = 7
# NUMBERS = os.listdir(project_util.FULLPATH_CARTELLA_IMG_NUMBERS)
# DICES = os.listdir(project_util.FULLPATH_CARTELLA_IMG_DICES)
# SHAPES = os.listdir(project_util.FULLPATH_CARTELLA_IMG_SHAPES)
# PENCILS = os.listdir(project_util.FULLPATH_CARTELLA_IMG_PENCILS)

EMOJI = os.listdir(project_util.FULLPATH_CARTELLA_IMG_EMOJI)

#l'estremo massimo non e' compreso
VIDEOS = ['video'+str(x)+'.mp4' for x in list(range(1, 25))]

LOGIC_IMAGES = [os.listdir(project_util.FULLPATH_CARTELLA_IMG_LOGIC1),
		os.listdir(project_util.FULLPATH_CARTELLA_IMG_LOGIC2),
		os.listdir(project_util.FULLPATH_CARTELLA_IMG_LOGIC3),
		os.listdir(project_util.FULLPATH_CARTELLA_IMG_LOGIC4),
		os.listdir(project_util.FULLPATH_CARTELLA_IMG_LOGIC5),
		os.listdir(project_util.FULLPATH_CARTELLA_IMG_LOGIC6),
		os.listdir(project_util.FULLPATH_CARTELLA_IMG_LOGIC7),
		os.listdir(project_util.FULLPATH_CARTELLA_IMG_LOGIC8)]


def init_modelmap(request, formBean):
	return project_util.init_modelmap(request, APP_TITLE, APP_LOGO, formBean)
