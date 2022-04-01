from moduli import modulo_sqlite


class Database(modulo_sqlite.Sqlite):
	'''
	operations that I can do:
	select
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
/*
choice
*/
create table utente_bambini(
	id				integer primary key autoincrement not null,
	nome			text not null,
	cognome			text not null,
	scuola			text,
	classe			text,
	peso			integer,
	altezza			integer,
	sesso			text,
	insert_date		timestamp not null
);
create table choices_menu(
	id 				integer primary key autoincrement not null,
	id_utente		integer not null,
	tipo_test		integer not null,
	choice			integer,
	menu			text,
	insert_date		timestamp not null,
	foreign key(id_utente) references utente_bambini(id)
		ON UPDATE NO ACTION
		ON DELETE RESTRICT
);
create table choices_slider(
	id 				integer primary key autoincrement not null,
	id_utente		integer not null,
	slider_marks	text,
	insert_date		timestamp not null,
	foreign key(id_utente) references utente_bambini(id)
		ON UPDATE NO ACTION
		ON DELETE RESTRICT
);
create table choices_slider2(
	id 				integer primary key autoincrement not null,
	id_utente		integer not null,
	slider_marks	text,
	insert_date		timestamp not null,
	foreign key(id_utente) references utente_bambini(id)
		ON UPDATE NO ACTION
		ON DELETE RESTRICT
);
create table logic_test(
	id 				integer primary key autoincrement not null,
	id_utente		integer not null,
	logic_test		integer not null,
	risultato		text,
	insert_date		timestamp not null,
	foreign key(id_utente) references utente_bambini(id)
		ON UPDATE NO ACTION
		ON DELETE RESTRICT
);
/*
questionario teacher
*/
create table utenti(
	id					integer primary key autoincrement not null,
	nome				text not null,
	cognome				text not null,
	classe_alunno		text,
	data_nascita		date,
	insert_date			timestamp not null
);
create table personality_traits(
	id 					integer primary key autoincrement not null,
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
	
	def insert_choices_menu(self, id_utente, tipo_test, choice, menu):
		# parameters id_utente, choice are compulsory cuz defined "not null"
		# in the database
		
		sql = """
INSERT INTO choices_menu(
	id_utente, tipo_test, choice, menu, insert_date
) VALUES(
	:id_utente, :tipo_test, :choice, :menu, """ + modulo_sqlite.DATE_TIME_NOW + """
);
"""
		# Through insert_scelte I receive id_utente and choice,
		# with self.cursor_db.execute I pass id_utente to dictionary
		# with VALUES I insert id_utente into the database
		self.cursor_db.execute(sql, {
			'id_utente': id_utente,
			'tipo_test': tipo_test,
			'choice': choice,
			'menu': menu
		})
	
	####################################################################################################
	def insert_choices_slider(self, id_utente, slider_marks):
		sql = """
INSERT INTO choices_slider(
	id_utente, slider_marks, insert_date
) VALUES(
	:id_utente, :slider_marks, """ + modulo_sqlite.DATE_TIME_NOW + """
);
"""
		self.cursor_db.execute(sql, {
			'id_utente': id_utente,
			'slider_marks': slider_marks
		})
		
		####################################################################################################
	def insert_choices_slider2(self, id_utente, slider_marks):
		sql = """
INSERT INTO choices_slider2(
	id_utente, slider_marks, insert_date
) VALUES(
	:id_utente, :slider_marks, """ + modulo_sqlite.DATE_TIME_NOW + """
);
"""
		self.cursor_db.execute(sql, {
			'id_utente': id_utente,
			'slider_marks': slider_marks
		})
	
	####################################################################################################
	def insert_utente_bambino(self, nome, cognome, scuola, classe, peso, altezza, sesso):
		sql = """
INSERT INTO utente_bambini(
	nome, cognome, scuola, classe, peso, altezza, sesso, insert_date
) VALUES(
	:nome, :cognome, :scuola, :classe, :peso, :altezza, :sesso, """ + modulo_sqlite.DATE_TIME_NOW + """
);
"""
		self.cursor_db.execute(sql, {
			'nome': nome,
			'cognome': cognome,
			'scuola': scuola,
			'classe': classe,
			'peso': peso,
			'altezza': altezza,
			'sesso': sesso
		})
	
		####################################################################################################
		
	def insert_logic_test(self, id_utente, logic_test, risultato):
		sql = """
	INSERT INTO logic_test(
		id_utente, logic_test, risultato, insert_date
	) VALUES(
		:id_utente, :logic_test, :risultato, """ + modulo_sqlite.DATE_TIME_NOW + """
	);
	"""
		self.cursor_db.execute(sql, {
			'id_utente': id_utente,
			'logic_test': logic_test,
			'risultato': risultato
		})
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
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
	