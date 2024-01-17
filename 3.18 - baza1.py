import sqlite3

try:
    sql_connection = sqlite3.connect('sqlite_python.db')
    cursor = sql_connection.cursor()
    print("Baza danych zostałą podłaczona")
except sqlite3.Error as e:
    print("Bład podczas podłączania bazy danych", e)
finally:
    if sql_connection:
        sql_connection.close()
        print("Baza danch została zamknieta")

# hackerrank
