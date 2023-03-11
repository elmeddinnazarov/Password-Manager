import sqlite3 as sql

# def connect_db(db_name):
#     conn = sql.connect(f"{db_name}.db")
#     cursor = conn.cursor()
#     return cursor

def create_db():
    conn = sql.connect("default.db")
    cursor = conn.cursor()    
    cursor.execute(""" CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY,
        first_name VARCHAR(100),
        last_name VARCHAR(100),
        phone_number VARCHAR(130),
        email VARCHAR(130),
        password VARCHAR(130),
        secret_key VARCHAR(130),
        platforms VARCHAR(100)
        ) """)


# istifadeci datasi insert_bd fonksiyonuna tuple olaraq gelmelidir! data =()
# insert_db e elave olunmalidir: eger elave edilen data tablede varsa elve edib dbni sisirtmek olmaz.
# if ile yoxlanmali ve istifadeciye xeta mesaji gosterilmelidir. evvelkini saxla veya yenile deye
def insert_db(db_name, table_name, datas):
    conn = sql.connect(f"{db_name}.db")
    cursor = conn.cursor()
    command = f"""INSERT INTO {table_name} (first_name, last_name, phone_number, email, password, secret_key, platforms) 
                 VALUES (?, ?, ?, ?, ?, ?, ?)"""
    cursor.execute(command, datas)
    conn.commit()
    conn.close()
    
    
    
def update_db(db_name, table_name, user_id, column_name, new_data):
    conn = sql.connect(f"{db_name}.db")
    cursor = conn.cursor()
    command = f"""UPDATE {table_name} SET {column_name} = ? WHERE id = ?"""
    cursor.execute(command, (new_data, user_id))
    conn.commit()
    conn.close()


def set_null(db_name, table_name, user_id, column_name):
    conn = sql.connect(f"{db_name}.db")
    cursor = conn.cursor()
    command = f"""UPDATE {table_name} SET {column_name} = NULL WHERE id = ?"""
    cursor.execute(command, (user_id,))
    conn.commit()
    conn.close()


def remove_user(db_name, table_name, user_id):
    conn = sql.connect(f"{db_name}.db")
    cursor = conn.cursor()
    command = f"""DELETE from {table_name} WHERE id = ?"""
    cursor.execute(command, (user_id,))
    conn.commit()
    conn.close()
    


def show_user_info(db_name, table_name, user_id):
    conn = sql.connect(f"{db_name}.db")
    cursor = conn.cursor()
    cursor.execute(f"""SELECT * from {table_name} WHERE id = ?""", (user_id,))
    data_tuple = cursor.fetchone()
    conn.commit()
    conn.close()
    
    data_dict = {
        'id': data_tuple[0],
        'first_name': data_tuple[1],
        'last_name': data_tuple[2],
        'phone_number': data_tuple[3],
        'email': data_tuple[4],
        'password': data_tuple[5],
        'secret_key': data_tuple[6],
        'platforms': data_tuple[7],
    }

    return data_dict

    
db_name = "default"
user_id = 1
table_name = "users"
column_name = "email"
data = ("elmeddin", "nazarov", "559777767", "elmeddin222@hotmail.com", "adadada", "safari", "platform")



create_db()
insert_db(db_name, table_name, data)
print(show_user_info(db_name, table_name, user_id))
# remove_user(db_name, table_name, user_id)
