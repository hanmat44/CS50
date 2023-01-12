import sqlite3


# Add a new item to the database
def new_item_db(item):
    try:
        sqliteConnection = sqlite3.connect('data.db')
        cursor = sqliteConnection.cursor()
    
        query="INSERT INTO items (item) VALUES ('{}')".format(item)
        cursor.execute(query)
        sqliteConnection.commit()

        cursor.close()

    except sqlite3.Error as error:
        print("Error while connecting to sqlite", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("The SQLite connection is closed")


new_item_db("scissors")