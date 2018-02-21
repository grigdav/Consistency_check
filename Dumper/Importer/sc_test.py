import pymysql.cursors
from xmlParser import rootParser

Node_info = rootParser()

connection = pymysql.connect (host='localhost', user='root', password='091686423', db='Consistency_check',charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)

try:
    with connection.cursor() as cursor:
        sql= "INSERT INTO `t_f4ge_enodeb_m`(`field_enodeb_id`) VALUES ()"
        cursor.execute(sql,(Node_info.Node_info_Parser()))
    
    connection.commit()    

    with connection.cursor() as cursor:
        # Read a single record
        sql = "SELECT `field_enodeb_id` FROM `t_f4ge_enodeb_m`"
        cursor.execute(sql)
        result = cursor.fetchall()
        print(result)
finally:
    connection.close()