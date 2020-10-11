from django import forms

from moduli.django import modulo_validator

class QuestionarioTeacherFormBean(forms.Form):
	nome = forms.CharField(error_messages=modulo_validator.DEFAULT_ERRORS, initial='', required=True)
	cognome = forms.CharField(error_messages=modulo_validator.DEFAULT_ERRORS, initial='', required=True,)
	classe_alunno = forms.CharField(error_messages=modulo_validator.DEFAULT_ERRORS, initial='', required=True,)
	data_nascita = forms.DateField(error_messages=modulo_validator.DEFAULT_ERRORS, initial='', required=True, validators = [modulo_validator.chack_field_date_not_future, ])
	#TODO: aggiungere campi questionario
