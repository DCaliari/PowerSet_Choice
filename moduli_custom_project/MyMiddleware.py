import os

from django.utils.deprecation import MiddlewareMixin


class MyMiddleware:
	
	def __init__(self, get_response):
		self.get_response = get_response
	
	def __call__(self, request):
		response = self.get_response(request)
		# allow iframe to be inserted in webpages
		response['X-Frame-Options'] = 'SAMEORIGIN'
		return response
	
