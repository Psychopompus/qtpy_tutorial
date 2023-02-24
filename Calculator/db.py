import pymysql
import json


class Mariadb:
    def __init__(self):
        self.abrv = None
        self.word = None
        self.cur = None
        self.conn = None

        self.conf = {}
        self.host = None
        self.user = None
        self.password = None
        self.db = None
        self.file = None

        self.j_dict = {}
        self.initConfig()
        self.connect()
        self.readData()

    def initConfig(self):
        with open('database.config.json', 'r', encoding='UTF-8') as file:
            conf = json.load(file)
        self.host = conf.get("host")
        self.user = conf.get("user")
        self.password = conf.get("password")
        self.db = conf.get("db")
        self.file = conf.get("file")

    def connect(self):
        try:
            self.conn = pymysql.connect(host=self.host, user=self.user, password=self.password, db=self.db, charset='utf8mb4')

        except Exception as e:
            self.conn = None

    def readData(self):
        i = 0

        if self.conn is None:
            print('json mode')
            with open(self.file, 'r', encoding='UTF-8') as file:
                self.j_dict = json.load(file)
            print(self.j_dict)
            pass
        else:
            print('database mode')
            sql = "SELECT word, abrv FROM abbreviation"
            self.cur = self.conn.cursor()
            self.cur.execute(sql)
            for row in self.cur:
                self.j_dict[i] = {'word': row[0], 'abrv': row[1]}
                i = i + 1
            with open(self.file, 'w', encoding='UTF-8') as file:
                json.dump(self.j_dict, file, indent=4, ensure_ascii=False)

    def insertData(self, word, abrv):
        self.word = word
        self.abrv = abrv

        if self.conn is None:
            print('json mode')
            pass
        else:
            print('database mode')
            sql = "INSERT INTO abbreviation VALUES('" + word + "','" + abrv + "')"
            self.cur.execute(sql)
            self.conn.commit()

    def disconnect(self):
        self.conn.commit()
        self.conn.close()

    def find(self, word):
        i = 0
        value = ''
        for dic in self.j_dict.values():
            value = dic.get('word')
            if value == word:
                return dic.get('abrv')
            else:
                pass

        return ''
