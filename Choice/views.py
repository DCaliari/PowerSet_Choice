import os
import random

from django.shortcuts import redirect
from django.template.response import TemplateResponse

from Choice.custom_moduli import modulo_database
from Choice.custom_moduli import util

from Moduli import modulo_system
from Moduli import modulo_functions

# These are the ENDPOINT, because you can call them from outside
IMAGES_POWERSET = modulo_functions.powerset(util.IMAGES)[len(util.IMAGES) + 1:]
random.shuffle(IMAGES_POWERSET)


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


def index(request, template_name='index.html'):  # create the function custom
	global id_utente  # if the variable has been create outside the function (global) then it must be recalled inside
	
	connection_database = apri_connessione_db()
	connection_database.insert_utente()  # run the function insert_utente from modulo_database
	connection_database.conn_db.commit()
	id_utente = connection_database.cursor_db.lastrowid  # get the last id created in the database
	connection_database.close_conn()
	
	model_map = {
		'page_title': 'Start'
		
	}
	return TemplateResponse(request, template_name, model_map)


def choice_image(request, template_name='choice_image.html'):
	num_page = int(request.GET.get('page', ''))

	# the second parameter is needed because if "choice" is empty then '' is passed
	
	connection_database = apri_connessione_db()
	if 'choice' in request.GET:  # if the parameter 'choice' exists then insert in the database, otherwise nothing
		choice = int(request.GET.get('choice', ''))
		connection_database.insert_scelte(id_utente, choice)
	
	'''  to insert pages in between choice pages
	if num_page == 5:
		response = redirect('test')
		return response
	'''
	
	if num_page > len(IMAGES_POWERSET):  # when the pages are finished go to final page
		response = redirect('final_page')
		return response
	
	next_page = num_page + 1
	images = list(IMAGES_POWERSET[num_page - 1])  # fix the list
	random.shuffle(images)
	
	connection_database.conn_db.commit()
	connection_database.close_conn()
	
	model_map = {
		'page_title': 'Round ' + str(num_page),
		'next_page': next_page,
		'images': images
	}
	return TemplateResponse(request, template_name, model_map)


def final_page(request, template_name='final_page.html'):
	final_images = util.IMAGES
	model_map = {
		'images': final_images
	}
	return TemplateResponse(request, template_name, model_map)
