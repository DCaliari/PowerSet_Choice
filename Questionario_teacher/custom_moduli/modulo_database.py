from Moduli import modulo_sqlite
from Moduli import modulo_strings


class Database(modulo_sqlite.Sqlite):
	'''
	select	# operations that I can do
	count
	insert
	update
	delete
	'''
	
	# costruttore -- richiama la classe superiore (Sqlite) e passa un parametro: nomefile_db.
	def __init__(self, nomefile_db):
		super().__init__(nomefile_db)
	
	# metodi
	def schema(self):
		sql = """
create table questionario_teacher(
	id				integer primary key autoincrement not null,
	nome			text not null,
	cognome			text not null,
	insert_date		timestamp not null
);

"""
		# id is the name of the column. 'primary key' = always different. 'not null' = not empty
		# 'timestamp' = memorize day, month, year and hours.
		super().schema(sql)
	
	####################################################################################################
	def insert_questionario_teacher(self, nome, cognome):
		sql = """
INSERT INTO questionario_teacher(
	nome, cognome, insert_date
) VALUES(
	:nome, :cognome, """ + modulo_sqlite.DATE_TIME_NOW + """
);
"""
		self.cursor_db.execute(sql, {
			'nome': nome,
			'cognome': cognome
		})