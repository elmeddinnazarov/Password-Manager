import sqlite3 as sql


# ************************************************************************
#   Functions associated to Database
# ************************************************************************


def create_db():
    conn = sql.connect("default.db")
    cursor = conn.cursor()
    query_users = """ CREATE TABLE IF NOT EXISTS users(
        id INTEGER UNIQUE PRIMARY KEY,
        first_name VARCHAR(100) NOT NULL,
        last_name VARCHAR(100) NOT NULL,
        phone_number VARCHAR(130) NOT NULL,
        email VARCHAR(130) UNIQUE NOT NULL,
        password VARCHAR(130) NOT NULL,
        secret_key VARCHAR(130) NOT NULL
        ) 
        """   
    cursor.execute(query_users)
    close_db(conn)


def close_db(conn):
    conn.commit()
    conn.close()

# ************************************************************************


# ************************************************************************
#   Functions associated to users
# ************************************************************************

# example: data_dict = {
#     "first_name": "elmeddin",
#     "last_name": "nazarov",
#     "phone_number": "559777767",
#     "email": "elmeddin222@hotmail.com",
#     "password": "adadada",
#     "secret_key": "safari",
# }
# islem basarili bitibse True return edir. data deyisdirilmiyibse False return edir
def add_user(data_dict):
    datas = tuple(data_dict.values())
    keys = tuple(data_dict.keys())
    conn = sql.connect("default.db")
    cursor = conn.cursor()
    command = f"""INSERT INTO users {keys} VALUES (?, ?, ?, ?, ?, ?)"""
    try:
        cursor.execute(command, datas)
        close_db(conn)
        return True
    except sql.IntegrityError:
        print('This email address you entered is associated with an existing account.')
        close_db(conn)
        return False


# user_id = current user id, column_name = verinin oldugu column, new_data = elave edilen data
# islem basarili bitibse True return edir. data deyisdirilmiyibse False return edir
def update_user_info(user_id, column_name, new_data):
    conn = sql.connect("default.db")
    cursor = conn.cursor()
    command = f"""UPDATE users SET {column_name} = ? WHERE id = ?"""
    if not user_not_exist(user_id):
        cursor.execute(command, (new_data, user_id))
        close_db(conn)
        return True
    close_db(conn)
    return False


# user_id = current user id
# islem basarili bitibse True return edir. data deyisdirilmiyibse False return edir
def remove_user(user_id):
    conn = sql.connect("default.db")
    cursor = conn.cursor()
    command = f"""DELETE from users WHERE id = ?"""
    if not user_not_exist(user_id):
        cursor.execute(command, (user_id,))
        close_db(conn)
        return True
    close_db(conn)
    return False


# user_id = current user id
# islem basarili bitibse True return edir. data deyisdirilmiyibse False return edir
def user_not_exist(user_id):
    conn = sql.connect("default.db")
    cursor = conn.cursor()
    
    search_user_query = "SELECT id FROM users WHERE id = ?"
    cursor.execute(search_user_query, (user_id,))
    user_result = cursor.fetchone()
    
    if user_result is None:
        print("User with the given ID does not exist.")
        close_db(conn)
        return False
        

# ************************************************************************


# ************************************************************************
#   Functions associated to platforms
# ************************************************************************


def create_platform():
    conn = sql.connect("default.db")
    cursor = conn.cursor()
    query_platforms = f""" CREATE TABLE IF NOT EXISTS platforms(
    id INTEGER UNIQUE PRIMARY KEY,
    pl_name VARCHAR(100) NOT NULL,
    pl_username VARCHAR(100) NOT NULL,
    pl_email VARCHAR(130) NOT NULL,
    pl_password VARCHAR(130) NOT NULL,
    pl_type VARCHAR(130) NOT NULL,
    user_id INTEGER NOT NULL,
    FOREIGN KEY(user_id) REFERENCES users(id)
    ) 
    """
    cursor.execute(query_platforms)
    close_db(conn)



# data_pl = pl_name, pl_username, pl_email, pl_password, pl_type, user_id
# example: data_pl = {
#     "pl_name": "instagram",
#     "pl_username": "elmeddin.nazarov",
#     "pl_email": "elmeddin222@hotmail.com",
#     "pl_password": "asd12345",
#     "pl_type": "social",
#     "user_id": user_id
# }
# islem basarili bitibse True return edir. data deyisdirilmiyibse False return edir
def add_platform(data_pl):
    datas = tuple(data_pl.values())
    keys = tuple(data_pl.keys())
    conn = sql.connect("default.db")
    cursor = conn.cursor()
    user_id = data_pl["user_id"]

    if not user_not_exist(user_id):
        search_platform_query = "SELECT * FROM platforms WHERE pl_name=? AND pl_username=? AND pl_email=? AND pl_password=? AND pl_type=? AND user_id=?"
        cursor.execute(search_platform_query, datas)
        platform_result = cursor.fetchone()
        
        if platform_result:
            print("This platform information is already added.")
        else:
            insert_platform_query = f"""INSERT INTO platforms {keys} VALUES (?, ?, ?, ?, ?, ?)"""
            cursor.execute(insert_platform_query, datas)
            close_db(conn)
            return True
    close_db(conn)
    return False


# user_id = current user id, pl_name = platformanin adi column_name = verinin oldugu column, new_data = elave edilen data
# islem basarili bitibse True return edir. data deyisdirilmiyibse False return edir
def update_platform_info(user_id, pl_name, column_name, new_data):
    conn = sql.connect("default.db")
    cursor = conn.cursor()
    command = f"""UPDATE platforms SET {column_name} = ? WHERE user_id = ? AND pl_name = ?"""
    if not user_not_exist(user_id) and not pl_not_exist(user_id):
        cursor.execute(command, (new_data, user_id, pl_name))
        close_db(conn)
        return True
    close_db(conn)
    return False


# islem basarili bitibse True return edir. data deyisdirilmiyibse False return edir
def remove_platform(user_id, pl_name):
    conn = sql.connect("default.db")
    cursor = conn.cursor()
    command = f"""DELETE FROM platforms WHERE user_id = ? AND pl_name = ?"""
    
    if not user_not_exist(user_id) and not pl_not_exist(user_id):
        cursor.execute(command, (user_id, pl_name))
        close_db(conn)
        return True
    close_db(conn)
    return False


# islem basarili bitibse True return edir. data deyisdirilmiyibse False return edir
def remove_all_platforms(user_id):
    conn = sql.connect("default.db")
    cursor = conn.cursor()
    command = f"""DELETE FROM platforms WHERE user_id = ?"""
    
    if not user_not_exist(user_id) and not pl_not_exist(user_id):   
        cursor.execute(command, (user_id,))
        close_db(conn)
        return True
    close_db(conn)
    return False

    
# user hecbir platform eleve etmeyibsa False return edir. onun xaricinde True return edir
def pl_not_exist(user_id):
    conn = sql.connect("default.db")
    cursor = conn.cursor()
    
    search_user_query = "SELECT user_id FROM platforms WHERE user_id = ?"
    cursor.execute(search_user_query, (user_id,))
    user_result = cursor.fetchone()
    
    if user_result is None:
        print("User not add any platform before.")
        close_db(conn)
        return False
    close_db(conn)
    return True


# user_id = current user id
def show_all_platforms(user_id):
    conn = sql.connect("default.db")
    cursor = conn.cursor()
    if not user_not_exist(user_id) and not pl_not_exist(user_id):
        cursor.execute(f"""SELECT * FROM  platforms WHERE user_id = {user_id}""")
        data_tuples = cursor.fetchall()
        pl_datas = []
        for data_tuple in data_tuples:
            pl_data = {
            'id': data_tuple[0],
            'pl_name': data_tuple[1],
            'pl_username': data_tuple[2],
            'pl_email': data_tuple[3],
            'pl_password': data_tuple[4],
            'pl_type': data_tuple[5],
            'user_id': data_tuple[6],
            }
            pl_datas.append(pl_data)
            close_db(conn)
            return pl_datas
    close_db(conn)


# user_id = current user id, pl_name = platform name
# necite tapilsa list return eliyir. tapilmasa False return edir
def list_platforms_by_name(user_id, pl_name):
    conn = sql.connect("default.db")
    cursor = conn.cursor()
    if not user_not_exist(user_id) and not pl_not_exist(user_id):
        cursor.execute(f"""SELECT * FROM  platforms WHERE user_id = {user_id} AND pl_name = '{pl_name}'""")
        data_tuples = cursor.fetchall()
        pl_datas = []
        if not len(data_tuples) == 0:
            for data_tuple in data_tuples:
                pl_data = {
                'id': data_tuple[0],
                'pl_name': data_tuple[1],
                'pl_username': data_tuple[2],
                'pl_email': data_tuple[3],
                'pl_password': data_tuple[4],
                'pl_type': data_tuple[5],
                'user_id': data_tuple[6],
                }
                pl_datas.append(pl_data)
            close_db(conn)
            return pl_datas
        close_db(conn)
        return False
    
# ************************************************************************
