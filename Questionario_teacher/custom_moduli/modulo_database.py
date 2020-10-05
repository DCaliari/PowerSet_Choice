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
	id					integer primary key autoincrement not null,
	nome				text not null,
	cognome				text not null,
	classe_alunno		text,
	data_nascita		date,
	trait1				integer,
	trait2				integer,
	trait3				integer,
	trait4				integer,
	trait5				integer,
	trait6				integer,
	trait7				integer,
	trait8				integer,
	trait9				integer,
	trait10 			integer,
	insert_date			timestamp not null
);

"""
		# id is the name of the column. 'primary key' = always different. 'not null' = not empty
		# 'timestamp' = memorize day, month, year and hours.
		super().schema(sql)
	
	####################################################################################################
	def insert_questionario_teacher(self, nome, cognome, classe_alunno, data_nascita, trait1, trait2, trait3, trait4,
									trait5, trait6, trait7, trait8, trait9, trait10):
		sql = """
INSERT INTO questionario_teacher(
	nome, cognome, classe_alunno, data_nascita, trait1, trait2, trait3, trait4,
									trait5, trait6, trait7, trait8, trait9, trait10, insert_date
) VALUES(
	:nome, :cognome, :classe_alunno, :data_nascita, :trait1, :trait2, :trait3, :trait4,
									:trait5, :trait6, :trait7, :trait8, :trait9, :trait10, """ + modulo_sqlite.DATE_TIME_NOW + """
);
"""
		self.cursor_db.execute(sql, {
			'nome': nome,
			'cognome': cognome,
			'classe_alunno': classe_alunno,
			'data_nascita': data_nascita,
			'trait1': trait1,
			'trait2': trait2,
			'trait3': trait3,
			'trait4': trait4,
			'trait5': trait5,
			'trait6': trait6,
			'trait7': trait7,
			'trait8': trait8,
			'trait9': trait9,
			'trait10': trait10,
		})
