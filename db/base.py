import sqlite3
from pathlib import Path


class DB:
    def __init__(self):
        '''Инициализация соединения с БД'''
        # .db, .db3, .sqlite, .sqlite3
        self.connection = sqlite3.connect(Path(__file__).parent.parent / 'db.sqlite3')
        self.cursor = self.connection.cursor()

    def create_tables(self):
        '''Создание таблиц'''
        self.cursor.execute('DROP TABLE IF EXISTS genres')
        self.cursor.execute('DROP TABLE IF EXISTS titles')
        self.cursor.execute(''' 
            CREATE TABLE IF NOT EXISTS genres ( 
                id INTEGER PRIMARY KEY AUTOINCREMENT, 
                title TEXT, 
                description TEXT
            ) 
        ''')
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS titles ( 
                id INTEGER PRIMARY KEY AUTOINCREMENT, 
                genre INTEGER,
                name TEXT, 
                description TEXT,
                image TEXT,
                FOREIGN KEY(genre) REFERENCES genre(id)
            ) 
        ''')
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS users ( 
                id INTEGER PRIMARY KEY,
                name TEXT,  
                age INTEGER,
                comics_type TEXT,
                favorite_genres TEXT
            ) 
        ''')

    def populate_tables(self):
        '''Заполнение таблиц'''
        self.cursor.execute(''' 
            INSERT INTO genres (title, description) VALUES  
            ("Приключения", "Что-то о жанре Приключения"),  
            ("Фэнтези", "Что-то о жанре Фэнтези"),  
            ("Исекай", "Что-то о жанре Исекай"),  
            ("Меха", "Что-то о жанре Меха"),
            ("Драма", "Что-то о жанре Драма"),  
            ("Комедия", "Что-то о жанре Комедия"),  
            ("Ужасы", "Что-то о жанре Ужасы")
        ''')
        self.cursor.execute('''
            INSERT INTO titles (genre, name, description, image) VALUES  
            ("1", "Naruto", "Something about Naruto", "images/Naruto.jpg"),
            ("4", "Guren Lagan", "Something about Guren Lagan", "images/Guren_Lagan.jpg")
        ''')
        self.connection.commit()

    def get_genres(self):
        self.cursor.execute('SELECT title FROM genres')
        return [genre[0] for genre in self.cursor.fetchall()]

    def add_user(self, id: int, name: str, age: int, comics_type: str, favorite_genres: set):
        genres = ",".join(favorite_genres)
        data = {
            "id": id,
            "name": name,
            "age": age,
            "comics_type": comics_type,
            "favorite_genres": genres,
        }
        sql = """
                INSERT INTO users (id, name, age, comics_type, favorite_genres)
                VALUES (:id, :name, :age, :comics_type, :favorite_genres)
            """
        self.cursor.execute(sql, data)
        self.connection.commit()

    def get_user(self, id):
        self.cursor.execute('''SELECT * FROM users WHERE id = :id''', {'id': id})
        return self.cursor.fetchone()

    def get_titles(self, genre):
        self.cursor.execute('''
                SELECT titles.id, titles.name, titles.description, titles.image
                FROM titles
                INNER JOIN genres ON titles.genre = genres.id
                ''', {'genre': genre})
        titles = self.cursor.fetchall()
        data = {}
        for title in titles:
            data[title[0]] = {
                'name': title[1],
                'description': title[2],
                'image': title[3]
            }
        return data


if __name__ == "__main__":
    db = DB()
    db.create_tables()
    db.populate_tables()
