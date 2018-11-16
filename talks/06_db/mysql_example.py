import pymysql.cursors
import sys
login = "tp_user"
password = "tp_password"
db_name = "sys_base"

connection = pymysql.connect(host='localhost', user=login, password=password, db=db_name, charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
sql = 'SELECT first_name, last_name from users_user limit 5;'
cursor = connection.cursor()
cursor.execute(sql)
result = cursor.fetchall()
for user in result:
    print('{} {}'.format(user['first_name'], user['last_name']))
