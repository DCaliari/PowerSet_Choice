import os

from moduli_custom_project import project_util

APP_TITLE = 'Esperimento'
APP_LOGO = os.path.join(project_util.CARTELLA_FAVICONS, 'favicon_choice.png')

IMAGES = [
	'apple.jpg',
	'ice-cream.jpg',
	'pear.jpg',
	'pizza.jpeg'
]

IMAGES2 = [
	'coca.jpg',
	'fanta.jpg',
	'the.jpg',
	'acqua.jpeg'
]

IMAGES3 = [
	'coca.jpg',
	'fanta.jpg',
	'the.jpg',
	'acqua.jpeg'
]

NUMBERS = [
	'Zero.png',
	'Uno.png',
	'Due.png',
	'Tre.png',
	'Quattro.png',
	'Cinque.png',
	'Sei.png',
	'Sette.png',
	'Otto.png',
	'Nove.png'
]

DICES = [
	'One.png',
	'Two.png',
	'Three.png',
	'Four.png',
	'Five.png',
	'Six.png'
]

SHAPES = [
	'Cerchio.png',
	'Quadrato.png',
	'Triangolo.png'
]

PENCILS = [
	'Matita1.png',
	'Matita2.png'
]

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
		'pic_1.jpg',
		'pic_2.jpg',
		'pic_3.jpg',
		'pic_4.jpg',
		'pic_5.jpg',
		'pic_6.jpg'
	],
	[
		'pic_7.jpg',
		'pic_8.jpg',
		'pic_9.jpg',
		'pic_10.jpg',
		'pic_11.jpg',
		'pic_12.jpg'
	],
	[
		'pic_1.jpg',
		'pic_2.jpg',
		'pic_3.jpg',
		'pic_4.jpg',
		'pic_5.jpg',
		'pic_6.jpg'
	],
	[
		'pic_1.jpg',
		'pic_2.jpg',
		'pic_3.jpg',
		'pic_4.jpg',
		'pic_5.jpg',
		'pic_6.jpg'
	],
	[
		'pic_1.jpg',
		'pic_2.jpg',
		'pic_3.jpg',
		'pic_4.jpg',
		'pic_5.jpg',
		'pic_6.jpg'
	],
	[
		'pic_1.jpg',
		'pic_2.jpg',
		'pic_3.jpg',
		'pic_4.jpg',
		'pic_5.jpg',
		'pic_6.jpg'
	],
]


def init_modelmap(request):
	return project_util.init_modelmap(request, APP_TITLE, APP_LOGO)