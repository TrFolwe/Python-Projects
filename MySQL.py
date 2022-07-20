import mysql.connector

mysql = mysql.connector.connect(
  host="localhost",
  user="root",
  password="123456",
  database="py_test",
);

mysqlCursor = mysql.cursor()

def select(column = False):
    print("Sonuçlar listeleniyor...\n")
    if column is False:
        mysqlCursor.execute("SELECT * FROM users")
        for x in mysqlCursor:
            print('{0}: {1}'.format(x[1], x[2]))
    else:
        print("{0} Adlı sütun listeleniyor...".format(column))
        mysqlCursor.execute("SELECT {0} FROM users".format(column))
        for x in mysqlCursor:
            print('- {0}'.format(x[0]))

def insert():
    """print("Veritabanına eklemek istediğiniz bilgileri giriniz")
    userName = input("Kullanıcı adı: ").strip()
    password = input("{0} Şifresi: ".format(userName)).strip()
    if len(userName) == 0 or len(password) == 0:
        print("Bilgileri boş bırakmayınız!")
        return False"""
    sqlValues = [
        ("Semih", "semih123"),
        ("Ali", "ali123"),
        ("Veli","veli123")
    ]
    #return False
    mysqlCursor.executemany("INSERT INTO users(userName, userPassword) VALUES(%s, %s)",sqlValues)
    mysql.commit()
    print("Yeni kayıtlar eklendi\n\n{0}".format("\n".join(map(lambda i: "{0}: {1}".format(i[0], i[1]), sqlValues))))

select("userPassword")