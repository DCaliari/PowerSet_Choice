from django import forms

from moduli import modulo_date

DEFAULT_ERRORS = {
	'required': 'Questo campo è obbligatorio.',
	'invalid': 'Inserisci un valore valido.'
}

def chack_field_date_not_future(data):
	if data > modulo_date.today():
		raise forms.ValidationError("La data non può essere futura.")