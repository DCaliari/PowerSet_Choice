from Moduli import modulo_sqlite


class Database(modulo_sqlite.Sqlite):
	'''
	select  # operations that I can do
	count
	insert
	update
	delete
	'''
	#costruttore -- richiama la classe superiore (Sqlite) e passa un parametro: nomefile_db.
	def __init__(self, nomefile_db):
		super().__init__(nomefile_db)
	
	#metodi
	def schema(self):
		sql="""
create table utenti(
	id				integer primary key autoincrement not null,
	insert_date		timestamp not null
);
create table choices(
	id 				integer primary key autoincrement not null,
	id_utente  		integer not null,
	choice			text not null,
	insert_date		timestamp not null,
	foreign key(id_utente) references utenti(id)
		ON UPDATE NO ACTION
		ON DELETE RESTRICT
);

"""
		# id is the name of the column. 'primary key' = always different. 'not null' = not empty
		# 'timestamp' = memorize day, month, year and hours.
		super().schema(sql)
	
	
	#############################################################################################################################
	def select_scelte(self, id_utente):

		sql = """
SELECT *
FROM scelte
WHERE id_utente=:id_utente
;
"""
		# SELECT * means give me all the columns
		# id_utente=: id_utente --- the first is the name of column, the second name of variable SQL
		self.cursor_db.execute(sql, {
			'id_utente':id_utente
		})
		# collegamento variable SQL con python
		return self.cursor_db.fetchone()
