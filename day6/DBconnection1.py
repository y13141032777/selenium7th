import  pymysql

class DBconncetion:
    def exe_sql(self):
        with pymysql.Connect(host='127.0.0.1', user="root",password="root",database='pirate',port=3306, charset='utf8') as conn:
            cursor = conn.cursor()
        sql = 'SELECT *  from hd_user;'
        cursor.execute(sql)
        first_result = cursor.fetchall()
        for raw in  first_result:
            print(raw)
        conn.commit()
        # return first_result

if __name__ == '__main__':
    DBconncetion().exe_sql()



