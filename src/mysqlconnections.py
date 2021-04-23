import pymysql

class DataBase:
    def __init__(self):
        self.connection = pymysql.connect(
            host = 'localhost',#ip
            user='root',
            password = '12',
            db='py'
        )
        self.cursor = self.connection.cursor()
    def select_all_user(self):
        sql = 'SELECT iduser, user, password FROM user'
        try:
            self.cursor.execute(sql)
            users = self.cursor.fetchall()
            for user in users:
                print("id ", user[0])
                print("User", user[1])
        except Exception as e:
            raise
    def insert_data(self, data):
        sql ="INSERT INTO `py`.`user` (`user`) VALUES ('{}')".format(data)
        try:
            self.cursor.execute(sql)
            self.connection.commit()
            print('Se ha guardado exitosamente')
        except Exception as e:
            raise
    def close_connection(self):
        self.connection.close()
database=DataBase()
database.select_all_user()
database.insert_data("u151")