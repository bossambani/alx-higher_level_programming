#!/usr/bin/python3
import sys
import MySQLdb
"""script that takes in an argument and displays all values in the state
   table of hbtn_0e_0_usa where name matches the argument.
"""


def list_state_name_searched(username, password, dbname, searched_state):
    """connects to the database"""

    connection = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=dbname
            )

    cursor = connection.cursor()

    query = "SELECT * FROM states WHERE name = %s"

    value = f"{searched_state}"

    cursor.execute(query, (value,))

    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    connection.close()


if __name__ == "__main__":

    username = sys.argv[1]
    password = sys.argv[2]
    dbname = sys.argv[3]
    searched_state= sys.argv[4]

    list_state_name_searched(username, password, dbname, searched_state)

