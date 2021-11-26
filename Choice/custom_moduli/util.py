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
TEMPLATE_NAME__LOGIC_TEST = 'logic_test.html'
TEMPLATE_NAME__FINAL_PAGE = 'final_page_C.html'

PAGES_NUMERICAL_TEST = 7

IMAGES = os.listdir(project_util.FULLPATH_CARTELLA_IMG_CHOICE)

IMAGES2 = os.listdir(project_util.FULLPATH_CARTELLA_IMG_BIBITE)
IMAGES3 = os.listdir(project_util.FULLPATH_CARTELLA_IMG_SNACK)

NUMBERS = os.listdir(project_util.FULLPATH_CARTELLA_IMG_NUMBERS)
DICES = os.listdir(project_util.FULLPATH_CARTELLA_IMG_DICES)
SHAPES = os.listdir(project_util.FULLPATH_CARTELLA_IMG_SHAPES)
PENCILS = os.listdir(project_util.FULLPATH_CARTELLA_IMG_PENCILS)

EMOJI = os.listdir(project_util.FULLPATH_CARTELLA_IMG_EMOJI)

VIDEOS = [
	'video1.mp4',
	'video2.mp4',
	'video3.mp4',
	'video4.mp4',
	'video5.mp4',
	'video6.mp4',
	'video7.mp4',
	'video8.mp4',
	'video9.mp4',
	'video10.mp4',
	'video11.mp4',
	'video12.mp4',
	'video13.mp4'
]

LOGIC_IMAGES = [os.listdir(project_util.FULLPATH_CARTELLA_IMG_LOGIC1),
				os.listdir(project_util.FULLPATH_CARTELLA_IMG_LOGIC2),
				os.listdir(project_util.FULLPATH_CARTELLA_IMG_LOGIC3),
				os.listdir(project_util.FULLPATH_CARTELLA_IMG_LOGIC4),
				os.listdir(project_util.FULLPATH_CARTELLA_IMG_LOGIC5),
				os.listdir(project_util.FULLPATH_CARTELLA_IMG_LOGIC6),
				os.listdir(project_util.FULLPATH_CARTELLA_IMG_LOGIC7),
				os.listdir(project_util.FULLPATH_CARTELLA_IMG_LOGIC8),
				os.listdir(project_util.FULLPATH_CARTELLA_IMG_LOGIC9),
				os.listdir(project_util.FULLPATH_CARTELLA_IMG_LOGIC10),
				os.listdir(project_util.FULLPATH_CARTELLA_IMG_LOGIC11),
				os.listdir(project_util.FULLPATH_CARTELLA_IMG_LOGIC12),
				os.listdir(project_util.FULLPATH_CARTELLA_IMG_LOGIC13),
				os.listdir(project_util.FULLPATH_CARTELLA_IMG_LOGIC14)]


def init_modelmap(request, formBean):
	return project_util.init_modelmap(request, APP_TITLE, APP_LOGO, formBean)
