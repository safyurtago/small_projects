import mysql.connector


class Dictionary:
    __db = "add_dictionary"
    __table = "words"

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
            uzbek VARCHAR(16) NOT NULL,
            english VARCHAR(16) NOT NULL
        );
        '''
        self.__connection.cursor().execute(query)  

    def show_all(self):
        query = f'''SELECT * FROM {self.__table};
        '''
        cursor = self.__connection.cursor()
        cursor.execute(query)
        return cursor.fetchall()

    def add_word(self, uzbek, english):
        query = f'''INSERT INTO {self.__table} (uzbek, english) VALUES ("{uzbek}", "{english}")
        ;
        '''
        self.__connection.cursor().execute(query)
        self.__connection.commit()

    def search_word(self, wrd):
        temp = self.show_all()
        temp1 = []
        for lst in temp:
            for l in lst:
                if wrd in str(l):
                    temp1.append(lst)
                    break
        return temp1

d1 = Dictionary()

