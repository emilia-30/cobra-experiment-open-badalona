import sqlite3
from sqlite3 import Error


def wrap_in_quotes(phrase):
    return "'" + phrase + "'"


"""
 should collect per trial:

 from stims:
     prime -> sentence type, eg "predictable", or beep
     stim -> some key to represent the image shown
 
 Todo
 merge with trial results:
     speaker_response -> speech to text of participant response to image
     speaker_response_time -> interval between image appearing and start of speech articulation
     listener_response -> speech to text of participant response to previous speech
     listener_response_time -> interval between end of first response articulation and start of second speech articulation
"""

DB_KEYS = {
    "STIM": "stim",
    "PRIME": "prime",
    # "SPEAKER_RESPONSE": "speaker_response",
    # "SPEAKER_RESPONSE_TIME": "speaker_response_time",
    # "LISTENER_RESPONSE": "listener_response",
    # "LISTENER_RESPONSE_TIME": "listener_response_time",
}


def prepare_data_for_db(data):
    print(data)
    row_for_db = []

    for key in DB_KEYS.values():
        row_for_db.append(wrap_in_quotes(str(data[key])))

    return ", ".join(row_for_db)


def get_save_to_db(cursor):
    return lambda data: cursor.execute(
        "INSERT INTO trial VALUES (" + prepare_data_for_db(data) + ")"
    )


def get_all(cursor):
    cursor.execute("SELECT * from trial")
    rows = cursor.fetchall()
    # print all to csv
    for row in rows:
        print(row)


def create_connection(path):
    connection = None
    try:
        connection = sqlite3.connect(path)
        print("Connection to SQLite DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")

    cursor = connection.cursor()
    db_keys = ", ".join(DB_KEYS.values())

    cursor.execute(
        """CREATE TABLE IF NOT EXISTS trial
             ("""
        + db_keys
        + """)"""
    )

    def finish():
        connection.commit()
        connection.close()
        print('db done')

    return {"cursor": cursor, "finish": finish}
