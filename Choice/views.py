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
	database = modulo_database.Database(path_db)  # crea l'oggetto e apre la connessione
	if is_db_new:
		database.schema()
	return database


#################################################################################################

id_utente = None
last_page = 0


def index(request, template_name='index.html'):  # create the function custom
	global id_utente, last_page,IMAGES_POWERSET  # if the variable has been create outside the function (global) then it must be recalled inside
	
	last_page = 0
	
	connection_database = apri_connessione_db()
	connection_database.insert_utente()  # run the function insert_utente from modulo_database
	connection_database.conn_db.commit()
	id_utente = connection_database.cursor_db.lastrowid  # get the last id created in the database
	connection_database.close_conn()
	
	IMAGES_POWERSET = modulo_functions.shuffle_powerset(IMAGES_POWERSET)
	
	model_map = {
		'page_title': 'Start'
		
	}
	return TemplateResponse(request, template_name, model_map)


def choice_image(request, template_name='choice_image.html'):
	global last_page
	
	num_page = int(request.GET.get('num_page', ''))
	# the second parameter is needed because if "choice" is empty then '' is passed
	
	if num_page < last_page:
		num_page = last_page
		response = redirect('{}?num_page={}'.format(reverse('choice_image'), num_page))
		return response
	last_page = num_page
	
	'''  to insert pages in between choice pages
	if num_page == 5:
		response = redirect('test')
		return response
	'''
	
	images = IMAGES_POWERSET[num_page-1]
	
	model_map = {
		'page_title': 'Round ' + str(num_page),
		'num_page': num_page,
		'images': images
	}
	return TemplateResponse(request, template_name, model_map)


def save_choice(request):
	num_page = int(request.GET.get('num_page', ''))
	
	if num_page >= len(IMAGES_POWERSET):  # when the pages are finished go to final page
		response = redirect('drag_drop')
		return response
	
	if id_utente is None:
		response = redirect('index')
		return response
	
	connection_database = apri_connessione_db()
	if 'choice' in request.GET:  # if the parameter 'choice' exists then insert in the database, otherwise nothing
		choice = int(request.GET.get('choice', ''))
		menu = json.dumps(IMAGES_POWERSET[num_page-1])
		# json handle objects (like lists) when they are in the dataset
		# using json.loads I can transform data from the table into list or other objects again
		
		connection_database.insert_scelte(id_utente, choice, menu, None)

	connection_database.conn_db.commit()
	connection_database.close_conn()
	
	next_page = num_page + 1
	
	# the function reverse give the URL of the view: choice_image, the URL is http://192.168.1.9:8000/Choice/choice_image
	# we concatenate the parameter num_page with the value next_page
	response = redirect('{}?num_page={}'.format(reverse('choice_image'), next_page))
	return response


def drag_drop(request, template_name='drag_drop.html'):
	dd_images = util.IMAGES
	positions = range(100)
	
	model_map = {
		'page_title': 'Rank',
		'images': dd_images,
		'positions': positions
	}
	return TemplateResponse(request, template_name, model_map)


def slider(request, template_name='slider.html'):
	slider_images = util.IMAGES
	
	model_map = {
		'page_title': 'Slider',
		'images': slider_images
	}
	return TemplateResponse(request, template_name, model_map)


def slider_save(request):
	slider_images = util.IMAGES
	
	connection_database = apri_connessione_db()
	
	if 'store_slider' in request.POST:  # in the if loop enter the name from html file
		for image in slider_images:
			slider_value = request.POST.get(image, '')
			slider_list = [image, slider_value]
			slider_json = json.dumps(slider_list)
			connection_database.insert_scelte(id_utente, None, None, slider_json)
	
	connection_database.conn_db.commit()
	connection_database.close_conn()
	
	response = redirect('final_page')
	return response
	
	
def final_page(request, template_name='final_page.html'):
	final_images = util.IMAGES
	model_map = {
		'page_title': 'Final Page',
		'images': final_images
	}
	return TemplateResponse(request, template_name, model_map)
