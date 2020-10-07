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
create table utenti(
	id					integer primary key autoincrement not null,
	nome				text not null,
	cognome				text not null,
	classe_alunno		text,
	data_nascita		date,
	insert_date			timestamp not null
);
create table personality_traits(
	id_utente			integer not null,
	trait				integer not null,
	num_trait			integer not null,
	insert_date			timestamp not null,
	foreign key(id_utente) references utenti(id)
		ON UPDATE NO ACTION
		ON DELETE RESTRICT
);
"""
		# id is the name of the column. 'primary key' = always different. 'not null' = not empty
		# 'timestamp' = memorize day, month, year and hours.
		super().schema(sql)
	
	####################################################################################################
	def insert_utenti(self, nome, cognome, classe_alunno, data_nascita):
		sql = """
INSERT INTO utenti(
	nome, cognome, classe_alunno, data_nascita, insert_date
) VALUES(
	:nome, :cognome, :classe_alunno, :data_nascita, """ + modulo_sqlite.DATE_TIME_NOW + """
);
"""
		self.cursor_db.execute(sql, {
			'nome': nome,
			'cognome': cognome,
			'classe_alunno': classe_alunno,
			'data_nascita': data_nascita,
		})
	
	####################################################################################################
	def insert_personality_traits(self, id_utente, trait, num_trait):
		sql = """
INSERT INTO personality_traits(
	id_utente, trait, num_trait, insert_date
) VALUES(
	:id_utente, :trait, :num_trait, """ + modulo_sqlite.DATE_TIME_NOW + """
);
"""
		self.cursor_db.execute(sql, {
			'id_utente': id_utente,
			'trait': trait,
			'num_trait': num_trait
		})
