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
	id				integer primary key autoincrement not null,
	insert_date		timestamp not null
);
create table dati_bambino(
	id_utente		integer not null,
	nome			text,
	cognome			text,
	classe			text,
	peso			integer,
	altezza			integer,
	sesso			text,
	insert_date		timestamp not null,
	foreign key(id_utente) references utenti(id)
		ON UPDATE NO ACTION
		ON DELETE RESTRICT
);
create table choices_menu(
	id 				integer primary key autoincrement not null,
	id_utente  		integer not null,
	choice			integer,
	menu			text,
	insert_date		timestamp not null,
	foreign key(id_utente) references utenti(id)
		ON UPDATE NO ACTION
		ON DELETE RESTRICT
);
create table choices_slider(
	id 				integer primary key autoincrement not null,
	id_utente  		integer not null,
	slider			text,
	insert_date		timestamp not null,
	foreign key(id_utente) references utenti(id)
		ON UPDATE NO ACTION
		ON DELETE RESTRICT
);

"""
		# id is the name of the column. 'primary key' = always different. 'not null' = not empty
		# 'timestamp' = memorize day, month, year and hours.
		# foreign key connect the two tables via id_utente.
		super().schema(sql)
	
	####################################################################################################
	def select_choices_menu(self, id_utente):
		sql = """
SELECT *
FROM choices_menu
WHERE id_utente=:id_utente
;
"""
		# SELECT * means give me all the columns
		# id_utente=: id_utente --- the first is the name of column, the second name of variable SQL
		self.cursor_db.execute(sql, {
			'id_utente': id_utente
		})
		# collegamento variable SQL con python
		return self.cursor_db.fetchall()
	
	def insert_choices_menu(self, id_utente, choice, menu):
		# parameters id_utente, choice are compulsory cuz defined "not null"
		# in the database
		
		sql = """
INSERT INTO choices_menu(
	id_utente, choice, menu, insert_date
) VALUES(
	:id_utente, :choice, :menu, """ + modulo_sqlite.DATE_TIME_NOW + """
);
"""
		# Through insert_scelte I receive id_utente and choice,
		# with self.cursor_db.execute I pass id_utente to dictionary
		# with VALUES I insert id_utente into the database
		self.cursor_db.execute(sql, {
			'id_utente': id_utente,
			'choice': choice,
			'menu': menu
		})
	
	####################################################################################################
	def insert_choices_slider(self, id_utente, slider):
		sql = """
INSERT INTO choices_slider(
	id_utente, slider, insert_date
) VALUES(
	:id_utente, :slider, """ + modulo_sqlite.DATE_TIME_NOW + """
);
"""
		self.cursor_db.execute(sql, {
			'id_utente': id_utente,
			'slider': slider
		})
	
	####################################################################################################
	def insert_utenti(self):
		sql = """
INSERT INTO utenti(
	insert_date
) VALUES(
	""" + modulo_sqlite.DATE_TIME_NOW + """
);
"""
		self.cursor_db.execute(sql, {
		})
	
	####################################################################################################
	def insert_dati_bambino(self, id_utente, nome, cognome, classe, peso, altezza, sesso):
		sql = """
INSERT INTO dati_bambino(
	id_utente, nome, cognome, classe, peso, altezza, sesso, insert_date
) VALUES(
	:id_utente, :nome, :cognome, :classe, :peso, :altezza, :sesso, """ + modulo_sqlite.DATE_TIME_NOW + """
);
"""
		self.cursor_db.execute(sql, {
			'id_utente': id_utente,
			'nome': nome,
			'cognome': cognome,
			'classe': classe,
			'peso': peso,
			'altezza': altezza,
			'sesso': sesso
		})
