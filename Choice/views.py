import os
import json
import random

from django.shortcuts import redirect
from django.template.response import TemplateResponse
from django.urls import reverse

from Choice.custom_moduli import modulo_database
from Choice.custom_moduli import util

from Moduli import modulo_system
from Moduli import modulo_functions

# These are the ENDPOINT, because you can call them from outside
IMAGES_POWERSET = modulo_functions.powerset(util.IMAGES)[len(util.IMAGES) + 1:]

# This is a global variable, it is created once at the start and never later.

###############################################################################################
# function to open the connection to the database


def apri_connessione_db():
	path_db = os.path.abspath("RecordChoice.db")
	is_db_new = modulo_system.dimensione_file(path_db) <= 0
	database = modulo_database.Database(path_db)		# crea l'oggetto e apre la connessione
	if is_db_new:
		database.schema()
	return database


#################################################################################################

PAGES_NUMERICAL_TEST = 7

last_page = 0


def index(request, template_name='index.html'):		# create the function custom
	global last_page, IMAGES_POWERSET
	# if the variable has been create outside the function (global) then it must be recalled inside
	# se devo leggere la variabile non serve, se invece devo modificarla serve global
	
	last_page = 0
	
	IMAGES_POWERSET = modulo_functions.shuffle_powerset(IMAGES_POWERSET)
	
	model_map = util.init_modelmap(request)
	return TemplateResponse(request, template_name, model_map)


def questionnaire_kids(request, template_name='questionnaire_kids.html'):
	model_map = util.init_modelmap(request)
	
	model_map['frasi'] = util.QUESTIONNAIRE
	model_map['intensity'] = range(util.QUESTIONNAIRE_INTENSITY)
	return TemplateResponse(request, template_name, model_map)


def questionnaire_kids_save(request):
	
	connection_database = apri_connessione_db()
	
	# in the if loop enter the name from html file
	nome = request.POST.get('nome', None)
	cognome = request.POST.get('cognome', None)
	classe = request.POST.get('classe', None)
	peso = request.POST.get('peso', None)
	altezza = request.POST.get('altezza', None)
	sesso = request.POST.get('sesso', None)
	
	connection_database.insert_utente_bambino(nome, cognome, classe, peso, altezza, sesso)

	# get the last id created in the database
	id_utente = connection_database.cursor_db.lastrowid
	# set the value in the session. Session in handled in settings.py.
	request.session[util.SESSION_KEY__ID_UTENTE] = id_utente
	
	connection_database.conn_db.commit()
	connection_database.close_conn()
	
	response = redirect('choice_image')
	return response


def choice_image(request, template_name='choice_image.html'):
	global last_page
	
	num_page = int(request.GET.get('num_page', '1'))
	# the second parameter is needed because if "choice" is empty then '' is passed
	
	if num_page < last_page:
		num_page = last_page
		response = redirect('{}?num_page={}'.format(reverse('choice_image'), num_page))
		return response
	last_page = num_page
	
	'''to insert pages in between choice pages
	if num_page == 5:
		response = redirect('test')
		return response
	'''
	
	images = IMAGES_POWERSET[num_page-1]
	
	model_map = util.init_modelmap(request)
	model_map['page_title'] = 'Scelta n ' + str(num_page)
	model_map['num_page'] = num_page
	model_map['images'] = images
	return TemplateResponse(request, template_name, model_map)


def save_choice(request):
	id_utente = request.session[util.SESSION_KEY__ID_UTENTE]
	num_page = int(request.GET.get('num_page', ''))
	
	connection_database = apri_connessione_db()
	# if the parameter 'choice' exists then insert in the database, otherwise nothing
	# the parameter "choice" comes from javascript code in choice_image.html - "&choice="
	if 'choice' in request.GET:
		choice = int(request.GET.get('choice', ''))
		menu = json.dumps(IMAGES_POWERSET[num_page-1])
		# json handle objects (like lists) when they are in the dataset
		# using json.loads I can transform data from the table into list or other objects again
		
		connection_database.insert_choices_menu(id_utente, choice, menu)

	connection_database.conn_db.commit()
	connection_database.close_conn()
	
	# when the pages are finished go to next problem
	if num_page >= len(IMAGES_POWERSET):
		response = redirect('slider')
		return response
	
	next_page = num_page + 1
	
	# the function reverse give the URL of the view: choice_image, the URL is http://192.168.1.9:8000/Choice/choice_image
	# we concatenate the parameter num_page with the value next_page
	response = redirect('{}?num_page={}'.format(reverse('choice_image'), next_page))
	return response


def slider(request, template_name='slider.html'):
	slider_images = util.IMAGES
	
	model_map = util.init_modelmap(request)
	model_map['images'] = slider_images

	return TemplateResponse(request, template_name, model_map)


def slider_save(request):
	id_utente = request.session[util.SESSION_KEY__ID_UTENTE]
	slider_images = util.IMAGES
	
	connection_database = apri_connessione_db()
	
	# in the if loop enter the name from html file
	if 'store_slider' in request.POST:
		for image in slider_images:
			slider_value = request.POST.get(image, '')
			slider_list = [image, slider_value]
			slider_json = json.dumps(slider_list)
			connection_database.insert_choices_slider(id_utente, slider_json)
	
	connection_database.conn_db.commit()
	connection_database.close_conn()
	
	response = redirect('numerical_test')
	return response


def numerical_test(request, template_name='numerical_test.html'):
	global last_page
	
	immagini = []
	last_page = 0
	
	num_page = int(request.GET.get('num_page', '1'))
	
	if num_page < 4:
		immagini = util.NUMBERS
	elif num_page == 4 or 5:
		immagini = util.DICES
	elif num_page == 6:
		immagini = util.SHAPES
	elif num_page == 7:
		immagini = util.PENCILS
		
	if num_page < last_page:
		num_page = last_page
		response = redirect('{}?num_page={}'.format(reverse('numerical_test'), num_page))
		return response
	last_page = num_page
	
	model_map = util.init_modelmap(request)
	model_map['num_page'] = num_page
	model_map['immagini'] = immagini
	if num_page == 1:
		model_map['page_title'] = 'Quale numero e` piu` vicino al 6?'
	elif num_page == 2:
		model_map['page_title'] = 'Quale numero viene prima del 3?'
	elif num_page == 3:
		model_map['page_title'] = 'Quale numero viene dopo il 4?'
	elif num_page == 4:
		model_map['page_title'] = 'Quale e` la somma dei puntini?'
	elif num_page == 5:
		model_map['page_title'] = 'Quale dado contiene piu` puntini?'
	elif num_page == 6:
		model_map['page_title'] = 'Trova il quadrato.'
	elif num_page == 7:
		model_map['page_title'] = 'Trova la matita piu` lunga.'
		
	return TemplateResponse(request, template_name, model_map)


def save_numerical_test(request):
	id_utente = request.session[util.SESSION_KEY__ID_UTENTE]
	
	num_page = int(request.GET.get('num_page', ''))

	connection_database = apri_connessione_db()
	
	# inserire il risultato del test
	if 'risultato' in request.GET:
		risultato = request.GET.get('risultato', '')
		connection_database.insert_numerical_test(id_utente, num_page, risultato)
	
	connection_database.conn_db.commit()
	connection_database.close_conn()
	
	# when the pages are finished go to next problem
	if num_page >= PAGES_NUMERICAL_TEST:
		response = redirect('final_page')
		return response
	
	next_page = num_page + 1
	
	# the function reverse give the URL of the view: choice_image, the URL is http://192.168.1.9:8000/Choice/choice_image
	# we concatenate the parameter num_page with the value next_page
	response = redirect('{}?num_page={}'.format(reverse('numerical_test'), next_page))
	return response


def final_page(request, template_name='final_page.html'):
	id_utente = request.session[util.SESSION_KEY__ID_UTENTE]
	# leggo dal db
	connection_database = apri_connessione_db()
	choices = connection_database.select_choices_menu(id_utente)
	connection_database.close_conn()
	# elaboro le scelte
	images_payoff = []
	for choice in choices:
		# choice e' la riga della tabella, per selezionare una colonna usare le parentesi quadre come un array
		num_choice = choice['choice']
		menu = json.loads(choice['menu'])
		image_chosen = menu[num_choice]
		images_payoff.append(image_chosen)
	# scelgo un'immagine a caso
	image_payoff = random.choice(images_payoff)

	model_map = util.init_modelmap(request)
	model_map['image_payoff'] = image_payoff
	model_map['choices'] = images_payoff
	return TemplateResponse(request, template_name, model_map)
