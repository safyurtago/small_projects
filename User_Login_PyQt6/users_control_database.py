import mysql.connector


class Employees:
    __db = "sfr_users_db"
    __table = "users"

    def __init__(self) -> None:
        self.__connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Qwerty!2345"
        )
        self.__create_database()
        self.__create_table()
    
    def __create_database(self):
        self.__connection.cursor().execute(f"CREATE DATABASE IF NOT EXISTS {self.__db};")
        self.__connection.cursor().execute(f"USE {self.__db}")

    def __create_table(self):
        query = f'''CREATE TABLE IF NOT EXISTS {self.__table} (
            id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
            first_name VARCHAR(16),
            last_name VARCHAR(16),
            login VARCHAR(20) UNIQUE NOT NULL,
            password VARCHAR(20) DEFAULT "qwerty"
        );
        '''
        self.__connection.cursor().execute(query)

    def create_user(self, first, last, login, pswd):
        query1 = f'''INSERT INTO {self.__table} (first_name, last_name, login)
        VALUES ("{first}", "{last}", "{login}");
        '''
        query = f'''INSERT INTO {self.__table} (first_name, last_name, login, password)
        VALUES ("{first}", "{last}", "{login}", "{pswd}");
        '''        
        if len(pswd) < 1:
            self.__connection.cursor().execute(query1)
        else:
            self.__connection.cursor().execute(query)
        self.__connection.commit()
    
    def list_all_users(self):
        query = "SELECT * FROM users;"
        cursor = self.__connection.cursor()
        cursor.execute(query)
        return cursor.fetchall()

    def edit_user(self, id, f_name, l_name, login, password):
        query = f'''UPDATE {self.__table} SET first_name = '{f_name}',
        last_name = '{l_name}', login = '{login}', password = '{password}'
        WHERE id = {str(id)};
        '''
        cursor = self.__connection.cursor()
        cursor.execute(query)
        self.__connection.commit()

    def search_user(self, name):
        query = f"SELECT * FROM users WHERE first_name = '{name}';"
        cursor = self.__connection.cursor()
        cursor.execute(query)
        return cursor.fetchall()

    def close(self):
        self.__connection.close()

emp1 = Employees()

