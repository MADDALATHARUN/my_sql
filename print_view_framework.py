# Print View table data from MySQL Database

import mysql.connector

db_connection = mysql.connector.connect(
host='138.68.140.83', 
user='tharun', 
password='Tharun@123', 
database='dbTharun')
db_cursor = db_connection.cursor()

def print_view():
	db_cursor.execute(f"SHOW COLUMNS FROM {framework_view}")
	fields = [field[0] for field in db_cursor.fetchall()]
	db_cursor.execute(f"SELECT * FROM {framework_view}")
	records = db_cursor.fetchall()
	for record in records:
		for counter, field in enumerate(fields):
			print(f"{field}: {record[counter]}")
		print("\n")

framework_view = "frame_work_view"
print_view()
