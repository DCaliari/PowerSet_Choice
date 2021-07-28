import os

from moduli_custom_project import project_util

APP_TITLE = 'Esperimento'
APP_LOGO = os.path.join(project_util.CARTELLA_FAVICONS, 'favicon_choice.png')

TEMPLATE_NAME__INDEX = 'index.html'
TEMPLATE_NAME__QUESTIONARIO_KIDS = 'questionnaire_kids.html'
TEMPLATE_NAME__VIDEO = 'video.html'
TEMPLATE_NAME__CHOICE = 'choice_image.html'
TEMPLATE_NAME__SLIDER = 'slider.html'
TEMPLATE_NAME__NUMERICAL_TEST = 'numerical_test.html'
TEMPLATE_NAME__LANGUAGE_TEST = 'language_test.html'
TEMPLATE_NAME__LOGIC_TEST = 'logic_test.html'
TEMPLATE_NAME__FINAL_PAGE = 'final_page_C.html'

PHASE_CQ = 0
PHASE_CHOICE_IMAGE = 1

PAGES_NUMERICAL_TEST = 7

IMAGES_CQ = os.listdir(project_util.FULLPATH_CARTELLA_IMG_CQ)

IMAGES = os.listdir(project_util.FULLPATH_CARTELLA_IMG_CHOICE)

IMAGES2 = os.listdir(project_util.FULLPATH_CARTELLA_IMG_BIBITE)
IMAGES3 = os.listdir(project_util.FULLPATH_CARTELLA_IMG_SNACK)

NUMBERS = os.listdir(project_util.FULLPATH_CARTELLA_IMG_NUMBERS)
DICES = os.listdir(project_util.FULLPATH_CARTELLA_IMG_DICES)
SHAPES = os.listdir(project_util.FULLPATH_CARTELLA_IMG_SHAPES)
PENCILS = os.listdir(project_util.FULLPATH_CARTELLA_IMG_PENCILS)

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

LANGUAGE_IMAGES = [os.listdir(project_util.FULLPATH_CARTELLA_IMG_L1),
				os.listdir(project_util.FULLPATH_CARTELLA_IMG_L2),
				os.listdir(project_util.FULLPATH_CARTELLA_IMG_L3),
				os.listdir(project_util.FULLPATH_CARTELLA_IMG_L4),
				os.listdir(project_util.FULLPATH_CARTELLA_IMG_L5),
				os.listdir(project_util.FULLPATH_CARTELLA_IMG_L6),
				os.listdir(project_util.FULLPATH_CARTELLA_IMG_L7)]

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
