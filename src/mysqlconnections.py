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
        print("Se ha realizado la conexion")
    def select_all_user(self):
        sql = 'SELECT id, user, password FROM user'
        try:
            self.cursor.execute(sql)
            users = self.cursor.fetchall()
            return users
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
    def update_date(self, data,iduser):
        sql ="UPDATE `py`.`user` SET `user` = '{}' WHERE (`id` = '{}')".format(data, iduser)
        try:
            self.cursor.execute(sql)
            self.connection.commit()
            print('Se ha actualizado exitosamente')
        except Exception as e:
            raise
    def delete_date(self, iduser):
        sql ="DELETE FROM `py`.`user` WHERE (`id` = '{}')".format(iduser)
        try:
            self.cursor.execute(sql)
            self.connection.commit()
            print('Se ha actualizado exitosamente')
        except Exception as e:
            raise
    def close_connection(self):
        self.connection.close()
