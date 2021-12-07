from abc import ABC, abstractmethod
import sqlite3

TIMEOUT_CONNECTION = 20

# this variable store the command to get date, time and millis
DATE_TIME_NOW = "strftime('%Y-%m-%d %H:%M:%f', 'now')"


class Sqlite(ABC):
	# costruttore
	def __init__(self, nomefile_db, show_sql=False):
		self.conn_db = sqlite3.connect(nomefile_db, detect_types=sqlite3.PARSE_DECLTYPES, timeout=TIMEOUT_CONNECTION)
		# Give back the name of the column and not numerical index
		self.conn_db.row_factory = sqlite3.Row
		# creo il cursore
		self.cursor_db = self.conn_db.cursor()
		# setup iniziale
		# non puoi cancellare un record se e' referenziato da un'altra tabella
		self.cursor_db.executescript('''PRAGMA foreign_keys=ON;''')
		self.conn_db.commit()
		# mostra i comandi sql eseguiti
		if show_sql is True:
			self.conn_db.set_trace_callback(print)
		super().__init__()
	
	@abstractmethod
	def schema(self, sql_str):
		"""
		Inserire le istruzioni sql contenenti la dichiarazione delle tabelle (DDL)
		"""
		# execute more commands in one, I can create more tables without repeating execute
		self.cursor_db.executescript(sql_str)
		self.conn_db.commit()		# it does not save when I modify things, if there is an error it is very useful.
	
	def close_conn(self):
		self.cursor_db.close()
		self.conn_db.close()

# def paginazione(first_result,num_results):
# 	sql=("LIMIT "+str(num_results) if num_results!=None else "")
# 	sql+=(" OFFSET "+str(first_result) if first_result!=None else "")
# 	return sql
### scelgo quanti elementi "scaricare" dal db, ad esempio se mi servono 10 elementi non ha senso scaricarli tutti

# def add_param_list(lista,prefix):
# 	params={}
# 	for index,elem in enumerate(lista):
# 		params[prefix+str(index)]=elem
# 	return params
