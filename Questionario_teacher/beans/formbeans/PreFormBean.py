class PreFormBean:
	def __init__(self, request):
		self.n_alunni = int(request.get('n_alunni', 1))