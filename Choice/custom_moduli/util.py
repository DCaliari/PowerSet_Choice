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
TEMPLATE_NAME__FINAL_PAGE = 'final_page.html'

PAGES_NUMERICAL_TEST = 7

IMAGES = os.listdir(project_util.FULLPATH_CARTELLA_IMG_CHOICE)

IMAGES2 = os.listdir(project_util.FULLPATH_CARTELLA_IMG_BIBITE)
IMAGES3 = os.listdir(project_util.FULLPATH_CARTELLA_IMG_SNACK)

NUMBERS = os.listdir(project_util.FULLPATH_CARTELLA_IMG_NUMBERS)
DICES = os.listdir(project_util.FULLPATH_CARTELLA_IMG_DICES)
SHAPES = os.listdir(project_util.FULLPATH_CARTELLA_IMG_SHAPES)
PENCILS = os.listdir(project_util.FULLPATH_CARTELLA_IMG_PENCILS)

# TODO: adeguare il codice come la riga qui sotto
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

LANGUAGE_IMAGES = [
	[
		'matita.png',
		'treno.png',
		'forbice.png',
		'tv.png',
		'gelato.png',
		'mela.png'
	],
	[
		'orologio.png',
		'bandiera.png',
		'scopa.png',
		'pane.png',
		'nastro.png',
		'scarpa.png'
	],
	[
		'scala.png',
		'stagno.png',
		'freccia.png',
		'cannocchiale.png',
		'pinguino.png',
		'scatola.png'
	],
	[
		'serratura.png',
		'lampada.png',
		'pigna.png',
		'spiga.png',
		'pentola.png',
		'steccato.png'
	],
	[
		'ciabatte.png',
		'astronauta.png',
		'pallone.png',
		'lucchetto.png',
		'imbuto.png',
		'paracadute.png'
	],
	[
		'nave.png',
		'telefono.png',
		'gomma.png',
		'giornale.png',
		'ferrodastiro.png',
		'sedia.png'
	],
	[
		'topo.png',
		'quadro.png',
		'ombrello.png',
		'uva.png',
		'occhiali.png',
		'mucca.png'
	],
]


def init_modelmap(request, formBean):
	return project_util.init_modelmap(request, APP_TITLE, APP_LOGO, formBean)

