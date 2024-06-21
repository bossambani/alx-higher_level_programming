#!/usr/bin/python3
"""
 script that lists all states with a name starting with N (upper N)
 from the database
 """

if __name__ == "__main__":
    import sys
    import MySQLdb
    username = sys.argv[1]
    password = sys.argv[2]
    dbname = sys.argv[3]


def list_states(username, password, dbname):
    """connects to the database"""

    connection = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=dbname
            )

    cursor = connection.cursor()

    cursor.execute("SELECT * FROM states WHERE name LIKE %s", ('N%',))

    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    connection.close()


list_states(username, password, dbname)
