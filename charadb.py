import pymysql
import config

def get_all_characters():

	connector = pymysql.connect(
		host = config.host,
		user = config.user,
		passwd = config.passwd,
		db = config.db,
		charset = config.charset,
		cursorclass = pymysql.cursors.DictCursor)

	with connector.cursor() as cursor:
		sql = "select * from characters;"
		cursor.execute(sql)
		result = cursor.fetchall()

		response_list = []

		for i in range(len(result)):
			response_list.append(result[i])

		json_response = { "character_data" : response_list }			
		
		return json_response

	
			

