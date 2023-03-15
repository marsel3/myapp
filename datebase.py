import pymysql

# database connection
#connection = pymysql.connect(host="localhost", port=8889, user="root", passwd="root", database="SELECTION_DB")
connection = pymysql.connect(host="192.168.30.20",
                             user="root@192.168.30.20",
                             passwd="")

cursor = connection.cursor()
# some other statements  with the help of cursor
connection.close()