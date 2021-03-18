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


def get_specified_color_characters(color):

	connector = pymysql.connect(
		host = config.host,
		user = config.user,
		passwd = config.passwd,
		db = config.db,
		charset = config.charset,
		cursorclass = pymysql.cursors.DictCursor)

	with connector.cursor() as cursor:
		sql = 'select * from characters where color = "%s";'% (color)
		cursor.execute(sql)
		result = cursor.fetchall()

		response_list = []

		for i in range(len(result)):
			response_list.append(result[i])

		json_response = { "character_data" : response_list }

		return json_response


def get_skill_characters(type, cut, flag):

	connector = pymysql.connect(
		host = config.host,
		user = config.user,
		passwd = config.passwd,
		db = config.db,
		charset = config.charset,
		cursorclass = pymysql.cursors.DictCursor)

	with connector.cursor() as cursor:

		if flag == 0:

			sql = 'select characters.stars, characters.color, characters.name, skills.type, skills.cut, skills.target, characters_skill.quantity from characters inner join characters_skill on characters.character_id = characters_skill.character_id inner join skills on characters_skill.skill_id = skills.skill_id where skills.type = "%s" and skills.cut = %s;'% (type, cut)
			cursor.execute(sql)
			result = cursor.fetchall()

			response_list = []

			for i in range(len(result)):
				response_list.append(result[i])

			json_response = { "character_data" : response_list }

			return json_response

		else:
	
			sql = 'select characters.stars, characters.color, characters.name, skills.type, skills.cut, skills.target, characters_skill.quantity from characters inner join characters_skill on characters.character_id = characters_skill.character_id inner join skills on characters_skill.skill_id = skills.skill_id where skills.type = "%s"'% (type)
			cursor.execute(sql)
			result = cursor.fetchall()

			response_list = []

			for i in range(len(result)):
				response_list.append(result[i])

			json_response = { "character_data" : response_list }

			return json_response




	
			

