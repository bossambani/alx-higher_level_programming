#!/usr/bin/python3
"""script that takes in the name of a state as an argument and
   lists all cities of that state, using the database hbtn_0e_4_usa
"""

if __name__ == "__main__":
    import sys
    import MySQLdb

    connection = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3]
            )

    cursor = connection.cursor()

    cursor.execute("""SELECT a.id, a.name, b.name
            FROM cities a
            INNER JOIN states b
            ON a.state_id = b.id ORDER BY a.id ASC
            """)

    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    connection.close()
