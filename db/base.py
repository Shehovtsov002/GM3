import sqlite3
from pathlib import Path


def path(genre, title_id):
    return f"src/titles/{genre}/{title_id}/preview.jpg"


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
                type TEXT,
                url TEXT,
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
        self.cursor.execute('''
                    CREATE TABLE IF NOT EXISTS houses ( 
                        id INTEGER PRIMARY KEY AUTOINCREMENT, 
                        title TEXT,
                        url TEXT,
                        address TEXT,
                        price TEXT
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
            INSERT INTO titles (genre, name, description, image, url, type) VALUES  
            ("1", "Naruto", "Something about Naruto", :1, "https://mangalib.me/naruto?section=info&ui=3825976", "Манга"),
            ("4", "Guren Lagan", "Something about Guren Lagan", :2, "https://mangalib.me/tengen-toppa-gurren-lagann?bid=16892&section=info&ui=3825976", "Манга"),
            ("1", "Доктор Стоун", "Something about Доктор Стоун", :3, "https://mangalib.me/dr-stone?section=info&ui=3825976", "Манга"),
            ("1", "Ван Пис", "Something about Ван Пис", :4, "https://mangalib.me/one-piece?section=info&ui=3825976", "Манга"),
            ("1", "О моём перерождении в слизь", "Something about О моём перерождении в слизь", :5, "https://mangalib.me/tensei-shitara-slime-datta-ken?section=info&ui=3825976", "Манга"),
            ("1", "Невероятные Приключения ДжоДжо", "Something about Невероятные Приключения ДжоДжо", :6, "https://mangalib.me/phantom-blood-colored?section=info&ui=3825976", "Манга"),
            ("4", "Код Гиас", "Something about Код Гиас", :7, "https://mangalib.me/code-geass-soubou-no-oz?section=info&ui=3825976", "Манга"),
            ("4", "Истинный Мазингер Зеро", "Something about Истинный Мазингер Зеро", :8, "https://mangalib.me/shin-mazinga-zero?section=info&ui=3825976", "Манга")
        ''', {
            '1': path('adventures', 1),
            '2': path('mecha', 2),
            '3': path('adventures', 3),
            '4': path('adventures', 4),
            '5': path('adventures', 5),
            '6': path('adventures', 6),
            '7': path('mecha', 7),
            '8': path('mecha', 8)
        })
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

    def add_house(self, data: dict):
        sql = """
                INSERT INTO houses (title, url, address, price)
                VALUES (:title, :link, :address, :price)
            """
        self.cursor.execute(sql, data)
        self.connection.commit()

    def get_user(self, id):
        self.cursor.execute('''SELECT * FROM users WHERE id = :id''', {'id': id})
        return self.cursor.fetchone()

    def get_titles(self, genre='%'):
        self.cursor.execute('''
                SELECT titles.type, titles.name, titles.description, titles.image, titles.url, genres.title
                FROM titles
                INNER JOIN genres ON titles.genre = genres.id
                WHERE genres.title LIKE :genre
                ''', {'genre': genre})
        titles = self.cursor.fetchall()
        data = []
        for title in titles:
            data.append({
                'type': title[0],
                'name': title[1],
                'description': title[2],
                'image': title[3],
                'genre': title[5],
                'url': title[4]
            })
        return data


if __name__ == "__main__":
    db = DB()
    db.create_tables()
    db.populate_tables()
