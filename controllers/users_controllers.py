from controllers import db_connection

def check_creditnals(username, password_hash):
    conn = db_connection.get_conn()
    with conn.cursor() as cursor:
        conn.autocommit = True
        cursor.execute(
            "SELECT id FROM users WHERE username=%(username)s and password=%(password)s AND active;",
            {"username": username, "password": password_hash},
        )
        result = cursor.fetchone()
        if result != None:
            cursor.execute(
                "UPDATE users SET updated_at = NOW() + interval '2 hour' WHERE username=%(username)s;",
                {"username": username},
            )
            return True
        else:
            return False


def get_user_info(username):
    conn = db_connection.get_conn()
    with conn.cursor() as cursor:
        cursor.execute(
            """SELECT * FROM users WHERE username = %(username)s;""",
            {"username": username},
        )
        desc = cursor.description
        column_names = [col[0] for col in desc]
        data = [dict(zip(column_names, row)) for row in cursor.fetchall()][0]
    
    return data